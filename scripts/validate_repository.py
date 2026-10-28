# SPDX-License-Identifier: Apache-2.0
"""Validate only public sources; no network, model calls, or deployment."""
import argparse
import json
import sys
from project import ProjectError, validate_repository

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--public-release", action="store_true",
        help="Also require draft status for all published KF files; omit for a locally approved working copy",
    )
    args = parser.parse_args()
    try:
        print(json.dumps(validate_repository(public_release=args.public_release), ensure_ascii=False, indent=2))
    except (ProjectError, OSError, ValueError) as exc:
        print(f"VALIDATION FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
