#!/bin/sh
set -eu

uv export --locked --all-groups --format requirements-txt --output-file /tmp/baseline-audit.txt > /dev/null
uv run --locked pip-audit --require-hashes --disable-pip -r /tmp/baseline-audit.txt