# VS Code Dev Container Startup

2026-10-07: Added `.devcontainer/devcontainer.json` using the existing Compose `dev`
service, image, non-root user, and named volumes. The editor lifecycle overrides the
one-shot default command, syncs locked dependencies at creation/start, and configures
the Python interpreter, pytest, and Python/Pylance/Ruff extensions inside the container.
Added a host Dev Containers extension recommendation.

Updated README, structure, Python profile, and handover with prerequisites, explicit
reopen/trust behavior, volume persistence, rebuild steps, and host permission limitations.
No reference-project apps, hard-coded targets, auth bypasses, global pip installs,
production connections, or automatic folder-open tasks were imported.

Validation: JSON/lifecycle/interpreter/reference assertions and Compose validation passed.
Actual startup with temporary Dev Containers CLI 0.80.2 succeeded on Windows; both
`uv sync --locked` hooks completed and the non-root container stayed running. Runtime
checks confirmed `.venv` as Python's prefix, equivalence of the configured interpreter
and uv's `python3` alias, UID 10001, and installed pytest. Editor diagnostics reported
no errors. The validation container was stopped afterward without deleting its volumes.
GUI attachment and extension installation have not been exercised; other host platforms
remain unverified.

Deployment/rollback: development tooling only; no application or infrastructure deployed.
Remove the added editor configuration through a PR to return to CLI-only operation;
do not delete named volumes containing development data as part of rollback.