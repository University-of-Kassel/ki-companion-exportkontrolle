# SPDX-License-Identifier: Apache-2.0
"""Export a test plan, not a test result. Does not call a model or a judge."""
import argparse
from pathlib import Path
from project import ROOT, ProjectError, load_questions, write_json


def plan(root: Path = ROOT) -> dict:
    questions = load_questions(root)
    indexed = {q["id"]: q for q in questions}
    cases = []
    for q in questions:
        chain, cursor = [], q
        while cursor.get("follows"):
            cursor = indexed[cursor["follows"]]
            chain.append(cursor["id"])
        cases.append(dict(q, predecessor_chain=list(reversed(chain)), result="not_run"))
    return {"schema_version": 1, "execution_status": "not_run", "cases": cases,
            "instructions": "For each chain, use actual preceding bot replies. Respect fixture and unconfigured isolation. Record UI/runtime versions, source hashes and retrieval evidence. No model or judge has been called by this script."}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", type=Path, default=ROOT / "dist/evaluation-plan.json")
    args = p.parse_args()
    if args.out.exists():
        raise SystemExit("Output exists; choose a new filename")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    write_json(args.out, plan())
    print(f"Test plan exported to {args.out}; all cases remain not_run")
