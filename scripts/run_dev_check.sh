#!/bin/sh
set -eu

if [ ! -f /.dockerenv ] || [ "$(pwd)" != /workspace ] || [ "$(id -u)" != 10001 ]; then
    printf '%s\n' 'Open this project with Dev Containers: Reopen in Container, then run the task again.' >&2
    exit 1
fi

check=${1:?Expected a development check name}
case "$check" in
    all)
        for quality_check in environment lint format types tests audit; do
            sh "$0" "$quality_check"
        done
        printf '\n%s\n' 'All six quality checks passed. Your development setup is ready.'
        exit 0
        ;;
    environment)
        uv run --locked python -c 'import sys; from pathlib import Path; expected = Path("/workspace/.venv"); sys.prefix == str(expected) or sys.exit("Select the container virtual environment before continuing."); print("Environment ready."); print("Python:", sys.version.split()[0]); print("Virtual environment:", sys.prefix); print("Project folder: /workspace")'
        ;;
    lint) uv run --locked ruff check . ;;
    format) uv run --locked ruff format --check . ;;
    types) uv run --locked pyright ;;
    tests) uv run --locked pytest ;;
    audit) sh scripts/audit_dependencies.sh ;;
    *) printf '%s\n' 'Unknown development check; refusing execution.' >&2; exit 1 ;;
esac

printf '\nPASS: %s check completed.\n' "$check"