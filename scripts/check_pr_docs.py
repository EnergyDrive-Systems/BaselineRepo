import argparse
import re
import subprocess
from collections.abc import Sequence
from pathlib import PurePosixPath

CHANGE_RECORD = re.compile(r"docs/changes/[a-z0-9][a-z0-9-]*\.md")
PROJECT_DOCUMENTS = {"README.md", "GLOSSARY.md"}


def documentation_errors(changed_paths: Sequence[str]) -> list[str]:
    paths = {PurePosixPath(path).as_posix() for path in changed_paths}
    records = {
        path for path in paths if CHANGE_RECORD.fullmatch(path) and path != "docs/changes/README.md"
    }
    documents = {
        path
        for path in paths
        if path in PROJECT_DOCUMENTS
        or (path.startswith("docs/") and path.endswith(".md") and path not in records)
    }
    errors: list[str] = []
    if not records:
        errors.append("Add or update a PR-specific docs/changes/<descriptive-name>.md record.")
    if not documents:
        errors.append("Update an affected document under docs/, README.md, or GLOSSARY.md.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Require documentation updates in every PR.")
    parser.add_argument("base", help="Trusted base commit from the PR event")
    parser.add_argument("head", help="PR head commit from the PR event")
    arguments = parser.parse_args()
    base = str(arguments.base)
    head = str(arguments.head)
    for revision in (base, head):
        if re.fullmatch(r"[0-9a-fA-F]{40,64}", revision) is None:
            parser.error("Revisions must be full Git commit hashes.")
    result = subprocess.run(
        ["git", "diff", "--name-only", "--diff-filter=AMR", "-z", f"{base}...{head}"],
        check=True,
        capture_output=True,
        text=True,
    )
    errors = documentation_errors(result.stdout.strip("\0").split("\0"))
    for error in errors:
        print(error)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
