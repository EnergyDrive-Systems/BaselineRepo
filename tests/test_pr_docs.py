import subprocess
import sys
from pathlib import Path

import pytest

from scripts.check_pr_docs import documentation_errors, main


@pytest.mark.parametrize(
    ("paths", "error_count"),
    [
        (["src/service.py"], 2),
        (["docs/changes/add-service.md"], 1),
        (["docs/standards.md"], 1),
        (["docs/changes/README.md"], 1),
        (["docs/changes/add-service.md", "docs/PRD.md"], 0),
        (["docs/changes/fix-ci.md", "README.md"], 0),
        (["docs/changes/glossary.md", "GLOSSARY.md"], 0),
        (["docs/changes/Bad Name.md", "docs/PRD.md"], 1),
    ],
)
def test_documentation_requirement(paths: list[str], error_count: int) -> None:
    assert len(documentation_errors(paths)) == error_count


def git_command(directory: Path, *arguments: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(directory), *arguments],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


@pytest.mark.parametrize("with_docs", [True, False])
def test_cli_checks_real_diff(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, with_docs: bool
) -> None:
    git_command(tmp_path, "init", "--initial-branch=main")
    git_command(tmp_path, "config", "user.name", "Policy Test")
    git_command(tmp_path, "config", "user.email", "policy-test@example.invalid")
    (tmp_path / "README.md").write_text("Initial docs\n", encoding="utf-8")
    git_command(tmp_path, "add", ".")
    git_command(tmp_path, "commit", "-m", "Initial fixture")
    base = git_command(tmp_path, "rev-parse", "HEAD")
    (tmp_path / "source.txt").write_text("Changed source\n", encoding="utf-8")
    if with_docs:
        (tmp_path / "README.md").write_text("Updated docs\n", encoding="utf-8")
        records = tmp_path / "docs" / "changes"
        records.mkdir(parents=True)
        (records / "fixture-change.md").write_text("Evidence\n", encoding="utf-8")
    git_command(tmp_path, "add", ".")
    git_command(tmp_path, "commit", "-m", "Change fixture")
    head = git_command(tmp_path, "rev-parse", "HEAD")
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(sys, "argv", ["check_pr_docs.py", base, head])
    assert main() == (0 if with_docs else 1)


def test_cli_refuses_revision_options(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(sys, "argv", ["check_pr_docs.py", "--bad-option", "a" * 40])
    with pytest.raises(SystemExit) as error:
        main()
    assert error.value.code == 2


def test_deployment_adapter_fails_closed(tmp_path: Path) -> None:
    artifact = tmp_path / "source.tar.gz"
    artifact.write_bytes(b"test artifact")
    adapter = Path(__file__).resolve().parents[1] / "scripts" / "deploy.sh"
    result = subprocess.run(
        ["sh", str(adapter), "test", str(artifact)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1
    assert "not configured" in result.stderr
