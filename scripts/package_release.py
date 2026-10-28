# SPDX-License-Identifier: Apache-2.0
"""Create a deterministic source ZIP from explicit public paths, never from dist/.local."""
import argparse
import sys
import zipfile
from pathlib import Path
from project import ROOT, ProjectError, public_files, validate_repository


def package_release(root: Path, target: Path) -> int:
    validate_repository(root, public_release=True)
    if target.exists() or target.is_symlink():
        raise ProjectError("Release file already exists; choose a new filename")
    target = target.absolute()
    if target.resolve().is_relative_to(root.resolve()) and not target.resolve().is_relative_to(root.resolve() / "dist"):
        raise ProjectError("Inside the repository, ZIP output must be below dist/")
    paths = public_files(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(target, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in paths:
            info = zipfile.ZipInfo("ki-companion-exportkontrolle/" + path.relative_to(root).as_posix(), (2026, 10, 26, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    with zipfile.ZipFile(target) as archive:
        if archive.testzip() is not None:
            raise ProjectError("ZIP integrity check failed")
    return len(paths)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "dist/ki-companion-exportkontrolle-source.zip")
    args = parser.parse_args()
    try:
        count = package_release(ROOT, args.out)
        print(f"Source archive created: {args.out}; {count} public files")
    except (ProjectError, OSError, ValueError) as exc:
        print(f"PACKAGING FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
