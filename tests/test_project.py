# SPDX-License-Identifier: Apache-2.0
"""Offline tests. No test in this module evaluates a language-model response."""
from __future__ import annotations

import hashlib
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from project import (ROOT, HEADER_KEYS, ProjectError, load_yaml, read_json, read_kf, local_context,
                     selected_documents, validate_repository, load_questions, safe_file, public_files, write_json)
from build_bundle import build_bundle
from package_release import package_release
from prepare_evaluation import plan

SOURCE_COPY_IGNORE = shutil.ignore_patterns("dist", ".local", ".git", ".venv", "__pycache__", ".pytest_cache")


class TestSourceValidation(unittest.TestCase):
    def test_valid_repository(self):
        self.assertEqual(validate_repository()["knowledge_documents"], len(selected_documents(ROOT)))

    def test_headers_identical_everywhere(self):
        paths = [p for folder in ("knowledge", "local_templates", "evaluation/scenarios") for p in (ROOT / folder).rglob("KF-*.md")]
        self.assertGreater(len(paths), 0)
        for path in paths:
            with self.subTest(path=path.name):
                self.assertEqual(tuple(read_kf(path)[0]), HEADER_KEYS)

    def test_profiles_restricted_to_researcher(self):
        for _, meta, _ in selected_documents(ROOT):
            self.assertEqual(meta["profiles"], ["researcher"])

    def test_statuses_are_explicit(self):
        statuses = [m["status"] for _, m, _ in selected_documents(ROOT)]
        self.assertTrue(all(status in {"draft", "approved"} for status in statuses))

    def test_evaluation_not_runtime(self):
        ids = {m["id"] for _, m, _ in selected_documents(ROOT)}
        self.assertNotIn("KF-15", ids)
        self.assertNotIn("KF-04a", ids)
        self.assertNotIn("KF-04b", ids)

    def test_no_unsupported_kf_references(self):
        self.assertGreaterEqual(validate_repository()["all_kf_files"], len(selected_documents(ROOT)))

    def test_duplicate_yaml_key_rejected(self):
        with self.assertRaises(ProjectError):
            load_yaml("id: one\nid: two\n")

    def test_unsafe_yaml_tag_rejected(self):
        with self.assertRaises(ProjectError):
            load_yaml("!!python/object:builtins.str {}")

    def test_traversal_rejected(self):
        with self.assertRaises(ProjectError):
            safe_file(ROOT, "../outside.md")

    def test_absolute_path_rejected(self):
        with self.assertRaises(ProjectError):
            safe_file(ROOT, str(ROOT / "README.md"))

    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "real.txt").write_text("data", encoding="utf-8")
            try:
                (root / "link.txt").symlink_to(root / "real.txt")
            except OSError:
                self.skipTest("Symlink not available in this environment")
            with self.assertRaises(ProjectError):
                safe_file(root, "link.txt")

    def test_duplicate_json_key_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.json"
            p.write_text('{"a":1,"a":2}', encoding="utf-8")
            with self.assertRaises(ProjectError):
                read_json(p)

    def test_licence_and_attribution_present(self):
        licence = (ROOT / "LICENSE").read_text(encoding="utf-8")
        self.assertIn("Apache License", licence)
        self.assertIn("END OF TERMS AND CONDITIONS", licence)
        self.assertIn("Nina Felgen", (ROOT / "NOTICE").read_text(encoding="utf-8"))

    def test_new_scope_cases_exist(self):
        ids = {q["id"] for q in load_questions(ROOT)}
        self.assertTrue({"scope_001", "scope_007", "scope_015", "scope_016"} <= ids)

    def test_test_plan_not_results(self):
        result = plan(ROOT)
        self.assertEqual(len(result["cases"]), len(load_questions(ROOT)))
        self.assertEqual(result["execution_status"], "not_run")
        self.assertTrue(all(c["result"] == "not_run" for c in result["cases"]))

    def test_conversation_chain_preserved(self):
        cases = {c["id"]: c for c in plan(ROOT)["cases"]}
        self.assertEqual(cases["dialog_004"]["predecessor_chain"], ["dialog_001", "dialog_002", "dialog_003"])
        self.assertEqual(cases["scope_012"]["predecessor_chain"], ["scope_005"])


class TestLocalContext(unittest.TestCase):
    def setUp(self):
        self.fixture = read_json(ROOT / "evaluation/fixtures/institution.test.json")

    def test_unconfigured_safe(self):
        context, state = local_context(None)
        self.assertFalse(state["facts_reviewed"])
        self.assertIn("unknown", context)
        self.assertNotIn("@", context)

    def test_example_placeholders_not_exposed(self):
        example = read_json(ROOT / "config/institution.example.json")
        context, _ = local_context(example)
        self.assertNotIn("{{", context)
        self.assertNotIn("INSTITUTION_NAME", context)

    def test_unreviewed_values_not_exposed(self):
        self.fixture["facts_reviewed"] = False
        context, _ = local_context(self.fixture)
        self.assertNotIn("example.invalid", context)
        self.assertNotIn("Person A", context)

    def test_reviewed_values_exact(self):
        context, state = local_context(self.fixture, allow_test_fixture=True)
        self.assertTrue(state["facts_reviewed"])
        self.assertTrue(state["synthetic_test_context"])
        self.assertIn("ISOLATED_SYNTHETIC_TEST_CONTEXT: true", context)
        self.assertIn("not real institutional contacts", context)
        self.assertNotIn("### Authoritative local facts", context)
        self.assertIn("exportkontrolle@example.invalid", context)
        self.assertIn("https://example.invalid/exportkontrolle", context)
        self.assertIn("Person A", context)

    def test_reviewed_placeholder_rejected(self):
        self.fixture["contacts"][0]["url"] = "{{EXPORT_CONTROL_URL}}"
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)

    def test_missing_review_date_rejected(self):
        self.fixture["facts_reviewed_on"] = None
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)

    def test_future_review_date_rejected(self):
        self.fixture["facts_reviewed_on"] = "2999-01-01"
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)

    def test_invalid_email_rejected(self):
        self.fixture["contacts"][0]["email"] = "not-an-email"
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)

    def test_unsafe_url_scheme_rejected(self):
        self.fixture["contacts"][0]["url"] = "javascript:alert(1)"
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)

    def test_credentials_in_url_rejected(self):
        self.fixture["contacts"][0]["url"] = "https://user:password@example.invalid/"
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)

    def test_person_without_role_rejected(self):
        self.fixture["contacts"][0]["people"][0]["role"] = ""
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)

    def test_review_flags_must_be_boolean(self):
        self.fixture["facts_reviewed"] = "false"
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)

    def test_procedures_separately_reviewed(self):
        self.fixture["procedures"] = ["UNREVIEWED_PROCESS_SENTINEL"]
        context, _ = local_context(self.fixture, allow_test_fixture=True)
        self.assertNotIn("UNREVIEWED_PROCESS_SENTINEL", context)
        self.fixture["procedures_reviewed"] = True
        self.fixture["procedures_reviewed_on"] = "2026-10-22"
        context, state = local_context(self.fixture, allow_test_fixture=True)
        self.assertIn("UNREVIEWED_PROCESS_SENTINEL", context)
        self.assertTrue(state["procedures_reviewed"])

    def test_procedures_require_reviewed_facts(self):
        self.fixture["facts_reviewed"] = False
        self.fixture["procedures_reviewed"] = True
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)

    def test_example_contacts_not_production(self):
        with self.assertRaises(ProjectError):
            local_context(self.fixture, mode="production")

    def test_fixture_requires_explicit_test_mode(self):
        with self.assertRaisesRegex(ProjectError, "allow-test-fixture"):
            local_context(self.fixture)

    def test_fixture_flag_never_allows_production(self):
        with self.assertRaisesRegex(ProjectError, "only allowed in review"):
            local_context(self.fixture, mode="production", allow_test_fixture=True)

    def test_reserved_hosts_need_explicit_fixture_mode(self):
        self.fixture["contacts"][0]["email"] = ""
        for host in ("example.com", "sub.example.org", "example.net", "school.invalid", "campus.test", "campus.example", "localhost"):
            with self.subTest(host=host):
                self.fixture["contacts"][0]["url"] = "https://" + host + "/exportkontrolle"
                with self.assertRaisesRegex(ProjectError, "allow-test-fixture"):
                    local_context(self.fixture)

    def test_partial_contact_allowed(self):
        self.fixture["contacts"][0]["email"] = ""
        self.fixture["contacts"][0]["people"] = []
        context, _ = local_context(self.fixture, allow_test_fixture=True)
        self.assertNotIn('"email"', context)
        self.assertNotIn("Person A", context)

    def test_unexpected_field_rejected(self):
        self.fixture["api_key"] = "not-a-real-secret"
        with self.assertRaises(ProjectError):
            local_context(self.fixture, allow_test_fixture=True)


class TestBuildAndPackage(unittest.TestCase):
    def test_review_build_contents(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "review"
            result = build_bundle(ROOT, out, mode="review")
            self.assertEqual(result["knowledge_documents"], len(selected_documents(ROOT)))
            self.assertEqual(len(list((out / "knowledge").glob("*.md"))), len(selected_documents(ROOT)))
            self.assertFalse((out / "knowledge/KF-15.md").exists())
            prompt = (out / "System.compiled.md").read_text(encoding="utf-8")
            self.assertIn("Scope Gate", prompt)
            self.assertIn("no more than three", prompt)
            self.assertIn("No authoritative local facts", prompt)
            self.assertNotIn("{{", prompt)

    def test_fixture_build_is_explicitly_synthetic(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "fixture"
            build_bundle(ROOT, out, mode="review", config=ROOT / "evaluation/fixtures/institution.test.json",
                         allow_test_fixture=True)
            self.assertIn("exportkontrolle@example.invalid", (out / "System.compiled.md").read_text(encoding="utf-8"))
            self.assertFalse((out / "institution.test.json").exists())
            self.assertTrue(read_json(out / "build-manifest.json")["synthetic_test_context"])
            self.assertTrue(read_json(out / "model-settings.reference.json")["synthetic_test_context"])
            self.assertIn("SYNTHETIC FIXTURE", (out / "READ_ME_FIRST.txt").read_text(encoding="utf-8"))

    def test_fixture_build_rejects_implicit_or_production_use(self):
        fixture = ROOT / "evaluation/fixtures/institution.test.json"
        variants = (
            {"mode": "review", "config": fixture},
            {"mode": "production", "config": fixture, "allow_test_fixture": True},
            {"mode": "review", "allow_test_fixture": True},
        )
        with tempfile.TemporaryDirectory() as tmp:
            for index, kwargs in enumerate(variants):
                with self.subTest(variant=index):
                    out = Path(tmp) / str(index)
                    with self.assertRaises(ProjectError):
                        build_bundle(ROOT, out, **kwargs)
                    self.assertFalse(out.exists())

    def test_production_rejects_drafts_before_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
            first_path = selected_documents(root)[0][0]
            first_path.write_text(first_path.read_text(encoding="utf-8").replace('status: "approved"', 'status: "draft"', 1), encoding="utf-8")
            out = Path(tmp) / "production"
            with self.assertRaisesRegex(ProjectError, "not approved"):
                build_bundle(root, out, mode="production")
            self.assertFalse(out.exists())

    def test_existing_output_never_overwritten(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "review"; out.mkdir()
            sentinel = out / "keep.txt"; sentinel.write_text("preserve", encoding="utf-8")
            with self.assertRaises(ProjectError):
                build_bundle(ROOT, out, mode="review")
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve")

    def test_source_directory_not_output(self):
        with self.assertRaises(ProjectError):
            build_bundle(ROOT, ROOT / "knowledge/new-output", mode="review")

    def test_manifest_hashes_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "review"
            build_bundle(ROOT, out, mode="review")
            manifest = read_json(out / "build-manifest.json")
            expected = {p.relative_to(out).as_posix() for p in out.rglob("*") if p.is_file()}
            self.assertEqual(set(manifest["files_sha256"]), expected - {"build-manifest.json"})
            for relative, checksum in manifest["files_sha256"].items():
                self.assertNotIn("\\", relative)
                self.assertEqual(hashlib.sha256((out / relative).read_bytes()).hexdigest(), checksum)
            self.assertTrue(all("\\" not in path for path in manifest["source_sha256"]))
            self.assertFalse(manifest["live_deployed"])
            self.assertFalse(manifest["model_tested"])

    def test_source_archive_excludes_local_and_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
            (root / ".local").mkdir(); (root / ".local/private.json").write_text('{"private":"sentinel"}', encoding="utf-8")
            (root / "dist").mkdir(); (root / "dist/private.txt").write_text("private-build", encoding="utf-8")
            for directory in (".git", ".venv", "__pycache__", ".pytest_cache"):
                (root / directory).mkdir()
                (root / directory / "private.txt").write_text("not-public", encoding="utf-8")
            archive = Path(tmp) / "release.zip"
            package_release(root, archive)
            with zipfile.ZipFile(archive) as z:
                names = z.namelist()
                self.assertFalse(any("/.local/" in n or "/dist/" in n or "__pycache__" in n for n in names))
                self.assertIn("ki-companion-exportkontrolle/LICENSE", names)
                self.assertIn("ki-companion-exportkontrolle/NOTICE", names)
                allowed = read_json(root / "config/public-files.json")["files"]
                self.assertEqual(set(names), {"ki-companion-exportkontrolle/" + name for name in allowed})
                self.assertIsNone(z.testzip())

    def test_source_archive_rejects_unknown_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
            unexpected = ("private.txt", "docs/fallakte.txt", "config/institution.json")
            for relative in unexpected:
                (root / relative).write_text("SYNTHETIC_PRIVATE_SENTINEL", encoding="utf-8")
            archive = Path(tmp) / "release.zip"
            with self.assertRaisesRegex(ProjectError, "outside public allowlist") as error:
                package_release(root, archive)
            self.assertTrue(all(relative in str(error.exception) for relative in unexpected))
            self.assertFalse(archive.exists())

    def test_source_archive_rejects_locally_approved_knowledge(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
            path = selected_documents(root)[0][0]
            path.write_text(path.read_text(encoding="utf-8").replace('status: "draft"', 'status: "approved"', 1), encoding="utf-8")
            archive = Path(tmp) / "release.zip"
            with self.assertRaisesRegex(ProjectError, "Public release requires draft"):
                package_release(root, archive)
            self.assertFalse(archive.exists())

    def test_public_allowlist_rejects_duplicate_missing_and_private_entries(self):
        for variant in ("duplicate", "missing", "private"):
            with self.subTest(variant=variant), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp) / "repo"
                shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
                manifest_path = root / "config/public-files.json"
                manifest = read_json(manifest_path)
                if variant == "duplicate":
                    manifest["files"].append(manifest["files"][0])
                elif variant == "missing":
                    manifest["files"].append("missing-public-file.md")
                else:
                    (root / ".local").mkdir()
                    (root / ".local/private.json").write_text("{}", encoding="utf-8")
                    manifest["files"].append(".local/private.json")
                write_json(manifest_path, manifest)
                with self.assertRaises(ProjectError):
                    public_files(root)

    def test_source_archive_is_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / "a.zip", Path(tmp) / "b.zip"
            package_release(ROOT, a); package_release(ROOT, b)
            self.assertEqual(a.read_bytes(), b.read_bytes())

    def test_all_approved_simulation_builds_production(self):
        # This test modifies a disposable copy, never the source repository or its approvals.
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
            for path, meta, _ in selected_documents(root):
                if meta["status"] == "draft":
                    path.write_text(path.read_text(encoding="utf-8").replace('status: "draft"', 'status: "approved"', 1), encoding="utf-8")
            out = Path(tmp) / "production"
            result = build_bundle(root, out, mode="production")
            self.assertEqual(result["draft_documents"], 0)
            self.assertNotIn("REVIEW / TEST ONLY", (out / "System.compiled.md").read_text(encoding="utf-8"))



class TestPlatformNeutralRelease(unittest.TestCase):
    def test_public_check_accepts_draft_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
            for folder in ("knowledge", "local_templates", "evaluation/scenarios"):
                for path in (root / folder).rglob("KF-*.md"):
                    path.write_text(path.read_text(encoding="utf-8").replace('status: "approved"', 'status: "draft"', 1), encoding="utf-8")
            result = validate_repository(root, public_release=True)
            self.assertEqual(result["all_kf_statuses"]["approved"], 0)
            self.assertTrue(result["public_release_check"])

    def test_public_check_rejects_locally_approved_kf(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
            path = selected_documents(root)[0][0]
            path.write_text(path.read_text(encoding="utf-8").replace('status: "draft"', 'status: "approved"', 1), encoding="utf-8")
            # Ordinary local validation still allows documented institutional approval.
            validate_repository(root)
            with self.assertRaisesRegex(ProjectError, "Public release requires draft"):
                validate_repository(root, public_release=True)

    def test_public_check_includes_local_templates(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
            path = next((root / "local_templates").glob("KF-*.md"))
            path.write_text(path.read_text(encoding="utf-8").replace('status: "draft"', 'status: "approved"', 1), encoding="utf-8")
            with self.assertRaisesRegex(ProjectError, "Public release requires draft"):
                validate_repository(root, public_release=True)

    def test_public_check_includes_evaluation_material(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=SOURCE_COPY_IGNORE)
            path = next((root / "evaluation/scenarios").glob("KF-*.md"))
            path.write_text(path.read_text(encoding="utf-8").replace('status: "draft"', 'status: "approved"', 1), encoding="utf-8")
            with self.assertRaisesRegex(ProjectError, "Public release requires draft"):
                validate_repository(root, public_release=True)

    def test_bundle_has_no_required_platform(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "review"
            build_bundle(ROOT, out, mode="review")
            for filename in ("READ_ME_FIRST.txt", "model-settings.reference.json", "System.compiled.md"):
                with self.subTest(filename=filename):
                    self.assertNotIn("open webui", (out / filename).read_text(encoding="utf-8").lower())
            settings = read_json(out / "model-settings.reference.json")
            self.assertTrue(settings["documentation_only_not_an_import_format"])
            self.assertIsNone(settings["base_model"])
            self.assertFalse(settings["web_search"])
            self.assertFalse(settings["live_sanctions_screening"])

    def test_setup_is_primary_documentation(self):
        self.assertTrue((ROOT / "docs/setup.md").is_file())
        self.assertIn("(docs/setup.md)", (ROOT / "README.md").read_text(encoding="utf-8"))
        self.assertIn("option", (ROOT / "docs/openwebui.md").read_text(encoding="utf-8").lower())

    def test_platform_neutral_evaluation_protocol(self):
        text = (ROOT / "evaluation/TEST_PROTOCOL.md").read_text(encoding="utf-8")
        self.assertNotIn("Open-WebUI-Version", text)
        self.assertIn("KI-Plattform", text)


if __name__ == "__main__":
    unittest.main()
