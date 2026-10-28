# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 Universitaet Kassel
"""Offline validation and packaging primitives for the public researcher edition."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]
HEADER_KEYS = (
    "id", "title", "version", "status", "last_reviewed", "review_cycle",
    "profiles", "scope", "document_type", "related", "knowledge_area", "purpose", "binding",
)
PUBLIC_DIRS = ("bot", "config", "knowledge", "local_templates", "templates", "evaluation", "scripts", "tests", "docs", ".github")
PUBLIC_ROOT_FILES = (
    "README.md", "LICENSE", "NOTICE", "CREDITS.md", "CITATION.cff", "CHANGELOG.md",
    "CONTRIBUTING.md", "SECURITY.md", "DEPENDENCIES.md", "VERSION", "requirements.txt",
    ".gitignore", ".gitattributes", ".editorconfig", ".gitlab-ci.yml",
)
PUBLIC_FILE_MANIFEST = "config/public-files.json"
PRIVATE_ROOT_PATHS = frozenset({".local", "dist", ".git", ".venv"})
LOCAL_CACHE_DIRS = frozenset({"__pycache__", ".pytest_cache"})
REQUIRED_IDS = {"KF-00", "KF-00b", "KF-01", "KF-02", "KF-04", "KF-05", "KF-06", "KF-08", "KF-13", "KF-14", "KF-98", "KF-99"}
PLACEHOLDER = re.compile(r"\{\{[^{}]+\}\}|\[\[(?:[^\]]+)\]\]")


class ProjectError(ValueError):
    """An unsafe or inconsistent input; never silently skipped."""


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML loader which also rejects duplicate mapping keys."""


def _mapping(loader: UniqueSafeLoader, node: yaml.Node, deep: bool = False) -> dict:
    out = {}
    for keynode, valnode in node.value:
        key = loader.construct_object(keynode, deep=deep)
        if key in out:
            raise ProjectError(f"Duplicate YAML key: {key!r}")
        out[key] = loader.construct_object(valnode, deep=deep)
    return out


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def load_yaml(text: str) -> Any:
    try:
        return yaml.load(text, Loader=UniqueSafeLoader)
    except yaml.YAMLError as exc:
        raise ProjectError(f"Invalid YAML: {exc}") from exc


def _json_pairs(pairs: list) -> dict:
    out = {}
    for key, value in pairs:
        if key in out:
            raise ProjectError(f"Duplicate JSON key: {key}")
        out[key] = value
    return out


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_json_pairs)
    except (OSError, json.JSONDecodeError) as exc:
        raise ProjectError(f"Cannot read JSON {path.name}: {exc}") from exc


def write_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def safe_file(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ProjectError("Expected a nonempty POSIX relative path")
    rel = Path(relative)
    if rel.is_absolute() or ".." in rel.parts or rel.as_posix() != relative:
        raise ProjectError(f"Unsafe path: {relative}")
    p = root / rel
    if p.is_symlink() or any(parent.is_symlink() for parent in p.parents if parent != root.parent):
        raise ProjectError(f"Symlink not allowed: {relative}")
    if not p.resolve().is_relative_to(root.resolve()) or not p.is_file():
        raise ProjectError(f"Missing or unsafe file: {relative}")
    return p


def read_kf(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ProjectError(f"Missing YAML front matter: {path.name}")
    meta = load_yaml(match.group(1))
    if not isinstance(meta, dict) or tuple(meta) != HEADER_KEYS:
        raise ProjectError(f"Header fields/order differ: {path.name}")
    for name in ("id", "title", "version", "status", "scope", "document_type"):
        if not isinstance(meta[name], str) or not meta[name].strip():
            raise ProjectError(f"Invalid {name}: {path.name}")
    if not re.fullmatch(r"KF-\d{2}[a-z]?", meta["id"]):
        raise ProjectError(f"Invalid KF id: {path.name}")
    if not re.fullmatch(r"\d+\.\d+(?:\.\d+)?(?:-public\.\d+)?", meta["version"]):
        raise ProjectError(f"Invalid version: {path.name}")
    if f'_v{meta["version"]}.md' not in path.name:
        raise ProjectError(f"Filename/version mismatch: {path.name}")
    if meta["status"] not in {"approved", "draft"}:
        raise ProjectError(f"Invalid status: {path.name}")
    if meta["profiles"] not in (["researcher"], ["evaluation"]):
        raise ProjectError(f"Unsupported profile: {path.name}")
    if not isinstance(meta["related"], list) or not all(isinstance(s, str) for s in meta["related"]):
        raise ProjectError(f"Invalid related list: {path.name}")
    reviewed = meta["last_reviewed"]
    if reviewed is not None:
        if not isinstance(reviewed, str) or not re.fullmatch(r"\d{4}-\d{2}(?:-\d{2})?", reviewed):
            raise ProjectError(f"Invalid review date precision: {path.name}")
        try:
            dt.date.fromisoformat(reviewed if len(reviewed) == 10 else reviewed + "-01")
        except ValueError as exc:
            raise ProjectError(f"Invalid review date: {path.name}") from exc
    cycle = meta["review_cycle"]
    if cycle not in (None, "monthly", "quarterly", "semiannual", "annual", "event_driven"):
        raise ProjectError(f"Invalid review cycle: {path.name}")
    return meta, text[match.end():].strip() + "\n"


def selected_documents(root: Path) -> list[tuple[Path, dict, str]]:
    manifest = read_json(root / "config/knowledge-manifest.json")
    if set(manifest) != {"schema_version", "edition", "documents"} or (type(manifest["schema_version"]) is not int or manifest["schema_version"] != 1) or manifest["edition"] != "researcher":
        raise ProjectError("Invalid knowledge manifest schema")
    if not isinstance(manifest["documents"], list) or not manifest["documents"]:
        raise ProjectError("Knowledge manifest is empty")
    result, ids, paths = [], set(), set()
    for entry in manifest["documents"]:
        if not isinstance(entry, dict) or set(entry) != {"id", "path"}:
            raise ProjectError("Invalid manifest entry")
        if not entry["path"].startswith("knowledge/"):
            raise ProjectError("Only knowledge/ is allowed in the runtime manifest")
        path = safe_file(root, entry["path"])
        meta, body = read_kf(path)
        if meta["id"] != entry["id"] or meta["profiles"] != ["researcher"]:
            raise ProjectError(f"Manifest id/profile mismatch: {entry['path']}")
        if meta["id"] in ids or entry["path"] in paths:
            raise ProjectError("Duplicate id or file in knowledge manifest")
        ids.add(meta["id"]); paths.add(entry["path"])
        result.append((path, meta, body))
    expected = {p.relative_to(root).as_posix() for p in (root / "knowledge").rglob("KF-*.md")}
    if paths != expected:
        raise ProjectError(f"Manifest/file mismatch: {sorted(paths ^ expected)}")
    if not REQUIRED_IDS <= ids:
        raise ProjectError(f"Essential knowledge missing: {sorted(REQUIRED_IDS - ids)}")
    return result


def _private_or_generated(relative: Path) -> bool:
    return (relative.parts[0] in PRIVATE_ROOT_PATHS
            or any(part in LOCAL_CACHE_DIRS for part in relative.parts)
            or relative.suffix.lower() in {".pyc", ".pyo"})


def public_files(root: Path) -> list[Path]:
    """Require an explicit file allowlist; never discover extra files for publication."""
    manifest = read_json(safe_file(root, PUBLIC_FILE_MANIFEST))
    if (not isinstance(manifest, dict) or set(manifest) != {"schema_version", "files"}
            or type(manifest["schema_version"]) is not int or manifest["schema_version"] != 1
            or not isinstance(manifest["files"], list) or not manifest["files"]):
        raise ProjectError("Invalid public-files manifest schema")
    allowed, resolved, paths = set(), set(), []
    for relative in manifest["files"]:
        path = safe_file(root, relative)
        if relative in allowed or path.resolve() in resolved:
            raise ProjectError(f"Duplicate public file: {relative}")
        if _private_or_generated(Path(relative)):
            raise ProjectError(f"Private/generated path is not publishable: {relative}")
        if path.suffix.lower() in {".pdf", ".zip", ".pem", ".key"}:
            raise ProjectError(f"Unexpected binary/private material: {relative}")
        allowed.add(relative)
        resolved.add(path.resolve())
        paths.append(path)
    required = set(PUBLIC_ROOT_FILES) | {PUBLIC_FILE_MANIFEST, ".github/workflows/validate.yml"}
    if not required <= allowed:
        raise ProjectError(f"Essential public files missing from allowlist: {sorted(required - allowed)}")
    for folder in PUBLIC_DIRS:
        base = root / folder
        if not base.is_dir() or base.is_symlink():
            raise ProjectError(f"Missing or unsafe public directory: {folder}")
    unexpected = []
    for directory, subdirs, filenames in os.walk(root, followlinks=False):
        base = Path(directory)
        kept = []
        for name in subdirs:
            path = base / name
            relative = path.relative_to(root)
            if _private_or_generated(relative):
                continue
            if path.is_symlink():
                raise ProjectError(f"Symlink in public source tree: {relative.as_posix()}")
            kept.append(name)
        subdirs[:] = kept
        for name in filenames:
            path = base / name
            relative = path.relative_to(root)
            if _private_or_generated(relative):
                continue
            if path.is_symlink():
                raise ProjectError(f"Symlink in public source tree: {relative.as_posix()}")
            if relative.as_posix() not in allowed:
                unexpected.append(relative.as_posix())
    if unexpected:
        raise ProjectError("Files outside public allowlist; move private material to .local/ or "
                           "explicitly review the source manifest: " + ", ".join(sorted(unexpected)))
    return sorted(paths, key=lambda p: p.relative_to(root).as_posix())


def load_questions(root: Path) -> list[dict]:
    result, global_ids = [], set()
    for path in sorted((root / "evaluation/golden_questions").glob("*.yml")):
        doc = load_yaml(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or set(doc) != {"questions"} or not isinstance(doc["questions"], list):
            raise ProjectError(f"Invalid question file: {path.name}")
        local_ids = set()
        for q in doc["questions"]:
            if not isinstance(q, dict) or not all(key in q for key in ("id", "question", "expected_behavior")):
                raise ProjectError(f"Incomplete question: {path.name}")
            if q["id"] in global_ids:
                raise ProjectError(f"Duplicate question id: {q['id']}")
            if q.get("follows") and q["follows"] not in local_ids:
                raise ProjectError(f"Missing, future or cross-file predecessor: {q['id']}")
            if q.get("fixture") not in (None, "institution.test", "unconfigured"):
                raise ProjectError(f"Unknown fixture: {q['id']}")
            for key in ("expected_behavior", "must_not"):
                values = q.get(key, [])
                if not isinstance(values, list) or not all(isinstance(x, str) and x for x in values):
                    raise ProjectError(f"Invalid test criteria: {q['id']}")
            local_ids.add(q["id"]); global_ids.add(q["id"])
            result.append(dict(q, source_file=path.relative_to(root).as_posix()))
    if not result:
        raise ProjectError("No evaluation cases")
    return result


def validate_repository(root: Path = ROOT, *, public_release: bool = False) -> dict:
    docs = selected_documents(root)
    all_kfs = [p for folder in ("knowledge", "local_templates", "evaluation/scenarios") for p in (root / folder).rglob("KF-*.md")]
    metas = [read_kf(p)[0] for p in all_kfs]
    if public_release:
        non_drafts = [m["id"] for m in metas if m["status"] != "draft"]
        if non_drafts:
            raise ProjectError("Public release requires draft status for every KF; non-draft: " + ", ".join(non_drafts))
    ids = [m["id"] for m in metas]
    if len(ids) != len(set(ids)):
        raise ProjectError("Duplicate KF id across publication")
    known = set(ids)
    for path in all_kfs:
        meta, body = read_kf(path)
        for related in meta["related"]:
            for ref in re.findall(r"KF-\d{2}[a-z]?(?![A-Za-z0-9])", related):
                if ref not in known:
                    raise ProjectError(f"Unknown related KF {ref}: {path.name}")
        for ref in re.findall(r"KF-\d{2}[a-z]?(?![A-Za-z0-9])", body):
            if ref not in known:
                raise ProjectError(f"Unknown body reference {ref}: {path.name}")
    files = public_files(root)
    # Attribution in NOTICE/CREDITS/CITATION/README is intentional. Runtime content must be neutral.
    neutral_folders = ("bot", "knowledge", "local_templates", "templates", "evaluation", "config")
    forbidden = re.compile(r"\bKassel\b|uni-kassel\.de|SECURE-Admin|\bEKI\b|SECURE-Forscher|knowledge/central|secure_knowledge|secure_forscher|Admin-/Fachstellenprofil", re.I)
    for path in files:
        text = path.read_text(encoding="utf-8")
        if path.relative_to(root).parts[0] in neutral_folders and forbidden.search(text):
            raise ProjectError(f"Non-neutral runtime or test content: {path.relative_to(root)}")
        if re.search(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bghp_[A-Za-z0-9]{30,}|\bglpat-[A-Za-z0-9_-]{20,}", text):
            raise ProjectError(f"Possible credential: {path.relative_to(root)}")
    workflow_files = list((root / ".github/workflows").glob("*.yml")) + [root / ".gitlab-ci.yml"]
    for p in workflow_files:
        # BaseLoader preserves the GitHub YAML key 'on' as a string.
        if not isinstance(yaml.load(p.read_text(encoding="utf-8"), Loader=yaml.BaseLoader), dict):
            raise ProjectError(f"Invalid workflow YAML: {p.name}")
    read_json(root / "config/institution.example.json")
    load_yaml((root / "CITATION.cff").read_text(encoding="utf-8"))
    questions = load_questions(root)
    statuses = {s: sum(m["status"] == s for _, m, _ in docs) for s in ("approved", "draft")}
    return {"knowledge_documents": len(docs), "all_kf_files": len(all_kfs), "header_schema_fields": len(HEADER_KEYS),
            "knowledge_statuses": statuses,
            "all_kf_statuses": {s: sum(m["status"] == s for m in metas) for s in ("approved", "draft")},
            "public_release_check": public_release,
            "evaluation_cases": len(questions), "public_files": len(files)}


def _text(value: Any, name: str, *, limit: int = 1000) -> str:
    if not isinstance(value, str) or len(value) > limit or any(ord(c) < 32 for c in value):
        raise ProjectError(f"Invalid scalar configuration value: {name}")
    if PLACEHOLDER.search(value):
        raise ProjectError(f"Unresolved placeholder in reviewed configuration: {name}")
    return value


def _date(value: Any, name: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ProjectError(f"Reviewed configuration requires full ISO date: {name}")
    try:
        parsed = dt.date.fromisoformat(value)
    except ValueError as exc:
        raise ProjectError(f"Invalid configuration date: {name}") from exc
    if parsed > dt.datetime.now(dt.timezone.utc).date():
        raise ProjectError(f"Future configuration review date: {name}")
    return value


def _is_test_host(host: str) -> bool:
    host = host.lower().rstrip(".")
    examples = ("example.com", "example.org", "example.net")
    return (host == "localhost"
            or host.endswith((".invalid", ".test", ".example", ".localhost"))
            or any(host == example or host.endswith("." + example) for example in examples))


def local_context(config: dict | None, *, mode: str = "review",
                  allow_test_fixture: bool = False) -> tuple[str, dict]:
    """Render operator-verified values only; never treat examples as approved facts."""
    if mode not in {"review", "production"}:
        raise ProjectError("Explicit review or production mode required")
    if type(allow_test_fixture) is not bool:
        raise ProjectError("allow_test_fixture must be a boolean")
    if allow_test_fixture and mode != "review":
        raise ProjectError("Synthetic test fixtures are only allowed in review mode")
    if config is None:
        if allow_test_fixture:
            raise ProjectError("Synthetic test mode requires an explicit fixture configuration")
        return ("No authoritative local facts or local procedures have been configured. "
                "Local names, roles, contacts, URLs and processes are unknown. Do not infer them.\n",
                {"facts_reviewed": False, "procedures_reviewed": False, "synthetic_test_context": False})
    fields = {"schema_version", "institution_name", "facts_reviewed", "facts_reviewed_on", "contacts",
              "procedures_reviewed", "procedures_reviewed_on", "procedures"}
    if not isinstance(config, dict) or set(config) != fields or (type(config["schema_version"]) is not int or config["schema_version"] != 1):
        raise ProjectError("Invalid institution configuration schema")
    if type(config["facts_reviewed"]) is not bool or type(config["procedures_reviewed"]) is not bool:
        raise ProjectError("Review flags must be true/false, not strings")
    if not isinstance(config["contacts"], list) or not isinstance(config["procedures"], list):
        raise ProjectError("Contacts and procedures must be lists")
    if config["procedures_reviewed"] and not config["facts_reviewed"]:
        raise ProjectError("Reviewed procedures require a reviewed institution configuration")
    if not config["facts_reviewed"]:
        if allow_test_fixture:
            raise ProjectError("Synthetic fixture values must be explicitly reviewed as test values")
        return local_context(None, mode=mode)
    name = _text(config["institution_name"], "institution_name")
    if not name.strip():
        raise ProjectError("Reviewed institution name is empty")
    facts = {"institution_name": name, "reviewed_on": _date(config["facts_reviewed_on"], "facts_reviewed_on"), "contacts": []}
    for contact in config["contacts"]:
        allowed = {"area", "office", "unit", "email", "url", "people"}
        if not isinstance(contact, dict) or set(contact) != allowed:
            raise ProjectError("Unexpected contact fields")
        if not isinstance(contact["area"], str) or contact["area"] not in {"export_control", "research_security", "data_protection", "information_security", "general"}:
            raise ProjectError("Unknown contact area")
        output = {k: _text(contact[k], k) for k in ("area", "office", "unit", "email", "url") if contact[k] != ""}
        email = output.get("email", "")
        if email and not re.fullmatch(r"[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+", email):
            raise ProjectError("Invalid contact email")
        url = output.get("url", "")
        url_host = ""
        if url:
            parts = urlsplit(url)
            if parts.scheme not in ("https", "http") or not parts.hostname or parts.username or parts.password or any(c.isspace() for c in url):
                raise ProjectError("Invalid contact URL")
            url_host = parts.hostname
        email_host = email.rsplit("@", 1)[1] if email else ""
        if not allow_test_fixture and any(_is_test_host(host) for host in (email_host, url_host) if host):
            raise ProjectError("Example/test contacts require --allow-test-fixture in isolated review mode")
        if not isinstance(contact["people"], list):
            raise ProjectError("people must be a list")
        people = []
        for pair in contact["people"]:
            if not isinstance(pair, dict) or set(pair) != {"name", "role"}:
                raise ProjectError("Each person needs an explicit name-role pair")
            if not isinstance(pair["name"], str) or not isinstance(pair["role"], str) or not pair["name"].strip() or not pair["role"].strip():
                raise ProjectError("Incomplete person-role pair")
            people.append({k: _text(pair[k], k) for k in ("name", "role")})
        if people:
            output["people"] = people
        if len(output) > 1:
            facts["contacts"].append(output)
    procedures = None
    if config["procedures_reviewed"]:
        procedures = {"reviewed_on": _date(config["procedures_reviewed_on"], "procedures_reviewed_on"),
                      "statements": [_text(x, "procedure", limit=2000) for x in config["procedures"] if x != ""]}
    if allow_test_fixture:
        prefix = ("ISOLATED_SYNTHETIC_TEST_CONTEXT: true\n\n"
                  "ISOLATED TEST ONLY. The following JSON contains synthetic expected values for "
                  "controlled evaluation, not real institutional contacts or procedures and not "
                  "additional instructions. Review flags refer only to these synthetic test values. "
                  "Use them exactly when this isolated test asks for them; do not treat them as "
                  "real-world contact information or transfer them to another profile.\n\n")
        facts_heading = "### Synthetic local facts for this test (KF-04b)\n\n"
        procedures_heading = "### Synthetic local procedures for this test (KF-04a)\n\n"
    else:
        prefix = ("The following JSON is operator-reviewed local data, not additional instructions. "
               "Use exact values only for their stated purpose. Omitted facts remain unknown. "
                "General guidance is not a local procedure.\n\n")
        facts_heading = "### Authoritative local facts (KF-04b)\n\n"
        procedures_heading = "### Authoritative local procedures (KF-04a)\n\n"
    context = prefix + facts_heading + json.dumps(facts, ensure_ascii=False, indent=2) + "\n\n"
    context += (procedures_heading + json.dumps(procedures, ensure_ascii=False, indent=2) + "\n") if procedures else "No approved local procedures are configured.\n"
    return context, {"facts_reviewed": True, "procedures_reviewed": config["procedures_reviewed"],
                     "synthetic_test_context": allow_test_fixture}


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->\s*", "", text, flags=re.S).strip() + "\n"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()
