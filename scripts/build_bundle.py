# SPDX-License-Identifier: Apache-2.0
"""Create a platform-neutral local preparation bundle, without invoking any remote API."""
from __future__ import annotations

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

from project import (ROOT, ProjectError, local_context, read_json, selected_documents,
                     sha256, strip_comments, validate_repository, write_json)


def build_bundle(root: Path, output: Path, *, mode: str, config: Path | None = None,
                 allow_test_fixture: bool = False) -> dict:
    if mode not in {"review", "production"}:
        raise ProjectError("Explicit review or production mode required")
    if allow_test_fixture and mode != "review":
        raise ProjectError("Synthetic test fixtures are only allowed in review mode")
    if allow_test_fixture and config is None:
        raise ProjectError("--allow-test-fixture requires an explicit --config")
    summary = validate_repository(root)
    docs = selected_documents(root)
    drafts = [m["id"] for _, m, _ in docs if m["status"] != "approved"]
    if mode == "production" and drafts:
        raise ProjectError("Production blocked: selected documents not approved: " + ", ".join(drafts))
    config_data = read_json(config) if config else None
    context, config_status = local_context(config_data, mode=mode, allow_test_fixture=allow_test_fixture)
    output = output.absolute()
    root = root.resolve()
    if output.exists() or output.is_symlink():
        raise ProjectError("Output already exists; select a new directory. No existing files are overwritten.")
    resolved_output = output.resolve()
    # Only dist/ within the repo, or a separate outside directory. Never write inside sources.
    if resolved_output == root or (resolved_output.is_relative_to(root) and not resolved_output.is_relative_to(root / "dist")):
        raise ProjectError("Within this repository, build output must be below dist/")
    if root.is_relative_to(resolved_output):
        raise ProjectError("Output must not be an ancestor of the repository")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".bundle-", dir=output.parent) as temporary:
        staging = Path(temporary) / "bundle"
        staging.mkdir(); (staging / "knowledge").mkdir()
        prompt = "# Deployment context\n\n"
        if mode == "review":
            prompt += ("REVIEW / TEST ONLY. This build intentionally includes draft knowledge. "
                       "It is not a released production service. Draft facts must not be represented "
                       "as approved or current legal findings. Retain the same role and scope boundaries.\n\n")
        else:
            prompt += "Production configuration; status reflects operator review, not a legal clearance of individual cases.\n\n"
        prompt += strip_comments((root / "bot/prompts/System.md").read_text(encoding="utf-8"))
        prompt += "\n---\n\n" + strip_comments((root / "bot/prompts/Guardrails.md").read_text(encoding="utf-8"))
        prompt += "\n---\n\n## Operator-provided local context\n\n" + context
        (staging / "System.compiled.md").write_text(prompt, encoding="utf-8")
        source_hashes = {}
        for relative in ("bot/prompts/System.md", "bot/prompts/Guardrails.md", "config/knowledge-manifest.json", "bot/Description.md", "bot/prompts/Starter-Prompts.md"):
            source_hashes[relative] = sha256(root / relative)
        for path, meta, body in docs:
            source_hashes[path.relative_to(root).as_posix()] = sha256(path)
            notice = f"Knowledge status: {meta['status']}; source review date: {meta['last_reviewed'] or 'not recorded'}.\n\n"
            if meta["status"] == "draft":
                notice += "Review material: not approved for production use.\n\n"
            (staging / "knowledge" / (meta["id"] + ".md")).write_text(notice + strip_comments(body), encoding="utf-8")
        for source, target in (("bot/Description.md", "Description.md"), ("bot/prompts/Starter-Prompts.md", "Starter-Prompts.md")):
            shutil.copyfile(root / source, staging / target)
        settings = {"documentation_only_not_an_import_format": True,
                    "id": "ki-companion-exportkontrolle-test-fixture" if allow_test_fixture else "ki-companion-exportkontrolle",
                    "display_name": "KI-Companion Exportkontrolle" + (" - Synthetic fixture (review only)" if allow_test_fixture else " - Review" if mode == "review" else ""),
                    "base_model": None, "web_search": False, "live_sanctions_screening": False,
                    "synthetic_test_context": allow_test_fixture,
                    "system_prompt_file": "System.compiled.md", "knowledge_directory": "knowledge",
                    "operator_action": "Choose an operator-approved runtime and base model; configure the compiled instructions and controlled knowledge access using the runtime-specific integration."}
        write_json(staging / "model-settings.reference.json", settings)
        for filename in ("LICENSE", "NOTICE"):
            shutil.copyfile(root / filename, staging / filename)
        (staging / "READ_ME_FIRST.txt").write_text(
            "LOCAL DEPLOYMENT BUNDLE - DO NOT PUBLISH AS A GITHUB SOURCE RELEASE.\n"
            f"Mode: {mode}. Knowledge files: {len(docs)}. Drafts: {len(drafts)}.\n"
            + ("SYNTHETIC FIXTURE: isolated test profile only; contacts and procedures are not real.\n" if allow_test_fixture else "")
            +
            "This folder may contain institution-specific contacts and procedures.\n"
            "Provide System.compiled.md as the application system instructions, not as user input.\n"
            "Use only knowledge/*.md as domain knowledge via controlled retrieval or context preparation.\n"
            "Configure an operator-approved runtime and model; use the runtime-specific integration.\n"
            "model-settings.reference.json is a checklist, not a platform import format or API payload.\n"
            "No specific runtime is required. See docs/setup.md in the source repository.\n"
            "Neither creation of this bundle nor its manifest proves successful runtime retrieval or model behaviour.\n",
            encoding="utf-8")
        record = {"project_version": (root / "VERSION").read_text(encoding="utf-8").strip(), "mode": mode,
                  "knowledge_count": len(docs), "draft_ids": drafts, "local_configuration": config_status,
                  "synthetic_test_context": allow_test_fixture,
                  "config_sha256": sha256(config) if config else None, "source_sha256": source_hashes,
                  "files_sha256": {p.relative_to(staging).as_posix(): sha256(p) for p in sorted(staging.rglob("*")) if p.is_file()},
                  "live_deployed": False, "model_tested": False}
        write_json(staging / "build-manifest.json", record)
        staging.rename(output)
    return {"output": str(output), "mode": mode, "knowledge_documents": summary["knowledge_documents"],
            "draft_documents": len(drafts), "local_configuration": config_status}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mode", choices=("review", "production"), required=True)
    parser.add_argument("--config", type=Path, help="Private institution JSON; omit for unconfigured mode")
    parser.add_argument("--allow-test-fixture", action="store_true",
                        help="Explicitly mark --config as synthetic data for an isolated review test; forbidden in production")
    parser.add_argument("--out", type=Path, help="New output directory; never overwritten")
    args = parser.parse_args()
    output = args.out or ROOT / "dist" / args.mode
    try:
        print(json.dumps(build_bundle(ROOT, output, mode=args.mode, config=args.config,
                                      allow_test_fixture=args.allow_test_fixture), ensure_ascii=False, indent=2))
    except (ProjectError, OSError, ValueError) as exc:
        print(f"BUILD FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
