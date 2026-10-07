# Standalone Python Profile

Baseline: CPython 3.13; approve exact patch/image digests per project. Ignition is
excluded from this profile's language and tool configuration.

- Use `uv sync --locked` and `uv run --locked` in the development container. Keep
  the mandatory `.venv` in its named volume, never in Git or shared with Windows.
- VS Code uses `.devcontainer/devcontainer.json` to attach to the Compose `dev`
  service and sync locked dependencies at creation/start. Its interpreter is
  `/workspace/.venv/bin/python`; reopening is explicit, not a silent folder-open task.
- Declare dependencies in `pyproject.toml`; commit `uv.lock`. Add official BigQuery
  client, psycopg, or approved SQL Server drivers only for selected profiles.
- Ruff enforces formatting/import/correctness/security rules; Pyright is strict.
  Type public contracts and changed code. Explain any suppression narrowly.
- The documentation checker suppresses subprocess lint rules only for its Git call:
  both revisions are validated full hashes, execution uses an argument list without
  a shell, and Git runs in an unprivileged container. Tests allow assertions and
  explicit subprocess calls for isolated Git fixtures and the fail-closed adapter.
- Audit a hash-pinned export of all lockfile groups with `scripts/audit_dependencies.sh`;
  do not assume pip-audit understands uv's lockfile format directly.
- pytest covers behavior and failures. Integration fixtures use isolated systems,
  never production writes. Cover denied/repeated/partial-failure write scenarios.
- Separate logic from database/HTTP/Ignition adapters. Validate inputs; use UTC and
  decimal arithmetic for exact quantities. Bound timeouts/retries and preserve idempotency.
- Use redacted structured logs with correlation identifiers. Fail explicitly, avoid
  swallowed broad exceptions, and do not log false success.
- Before release add a non-root runtime image, signal handling, real health checks,
  resource limits, secret injection, and rollback procedure. The dev image is not deployable.