# Organization Development Baseline

![EnergyDrive logo](assets/brand/energydrive-logo.png)

Starter template for Python services, Ignition Perspective, BigQuery, Cloud SQL
for PostgreSQL, and optional SQL Server. Use combined or separate projects without
copying different versions of the rules. No application or infrastructure is deployed.

All new and changed UIs follow Material Design 3 principles by default, including
Ignition Perspective. Agents automatically load `docs/profiles/ui.md` for UI work;
review checks responsive behavior, accessibility, and actual task-flow evidence.

## Start Here

1. Create a GitHub repository from this template and complete `docs/PRD.md`.
2. Read `docs/standards.md` and `docs/structure.md`; select profiles in the PRD.
3. Add real CODEOWNERS and configure branch protection and protected environments
   using `docs/deployment.md`.
4. Add project code in `src/`, Ignition resources in `ignition/`, SQL in `sql/`, and
   infrastructure in `infra/terraform/`, only as needed.
5. Complete `docs/HANDOVER.md` activation items before the first release.

## Development

Prerequisites: running Docker with Compose v2, Git, and VS Code with the Dev Containers
extension (`ms-vscode-remote.remote-containers`). The workspace recommends that extension;
install it when prompted if missing. Install Designer separately. Check Docker Desktop
licensing for organizational use. The image uses CPython 3.13 and uv; `uv.lock` fixes
actual dependency versions. No global Python installs.

### VS Code (Preferred)

1. Clone/copy the repository and open its folder in VS Code. Review and trust its
   configuration before allowing startup commands.
2. Accept **Reopen in Container**, or run **Dev Containers: Reopen in Container** from
   the Command Palette if no prompt appears.
3. Wait for the initial image build and setup. VS Code attaches to the `dev` service;
   startup hooks create/sync `.venv` with `uv sync --locked`. Python/Pylance/Ruff are
   configured as container extensions, with `/workspace/.venv/bin/python` as the default
   interpreter and pytest enabled. Previously saved interpreter choices may need to be
   corrected using **Python: Select Interpreter**.

Dependency sync runs at creation and each container start, including after reopening.
Changes to the lockfile while attached require `uv sync --locked` again. In a container
terminal use `uv run --locked pytest` or the other uv commands below without Compose.
Use **Dev Containers: Rebuild Container** after changing the image/container configuration.
Closing the container window stops its Compose services; named-volume data persists.

Opening a folder alone does not silently attach or run commands: Docker, the extension,
workspace trust, and the user's reopen choice are required. No application, database,
Ignition gateway, Terraform operation, or production connection starts automatically.
Unlike the reference project's tasks, this generic template has no application to launch.

The container keeps UID 10001 to preserve named-volume ownership. Linux hosts must
provide workspace write access to that UID; verify host permissions before first use.
Windows Docker Desktop is the locally verified environment.

### Command Line Alternative

```sh
docker compose build dev
docker compose run --rm dev uv sync --locked
docker compose run --rm dev uv run --locked ruff check .
docker compose run --rm dev uv run --locked ruff format --check .
docker compose run --rm dev uv run --locked pyright
docker compose run --rm dev uv run --locked pytest
docker compose run --rm dev sh scripts/audit_dependencies.sh
docker compose run --rm terraform fmt -check -recursive
docker compose run --rm terraform init -backend=false
docker compose run --rm terraform validate
```

Compose keeps the Linux `.venv` in a named volume; never share it with a Windows venv.
Use the container interpreter for editor type checking. Formatting fixes use
`ruff format .` in the same container. Optional hooks use
`uv run --locked pre-commit run --all-files` inside `dev`; CI remains authoritative.

## Map

| Path | Responsibility |
| --- | --- |
| `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` | Shared agent rules and client entry points |
| `.agents/skills/` | Reviewed interview, implementation, review, runtime, and readiness workflows |
| `docs/standards.md`, `docs/structure.md` | Engineering rules and repository layout |
| `docs/profiles/` | Material 3 UI, Python, Ignition, database, and Terraform rules |
| `docs/PRD.md`, `docs/HANDOVER.md`, `GLOSSARY.md` | Requirements, current state, terminology |
| `docs/deployment.md`, `docs/changes/` | Release controls and per-PR records |
| `.github/workflows/` | Quality gates and fail-closed deployment scaffold |
| `.devcontainer/`, `.vscode/extensions.json` | VS Code container lifecycle and host extension recommendation |
| `assets/brand/` | Original EnergyDrive logo and practical reuse notes |
| `scripts/`, `tests/` | Template checks and their tests |
| `Dockerfile`, `compose.yaml`, `pyproject.toml`, `uv.lock` | Isolated development tooling |
| `infra/terraform/` | Infrastructure version baseline; no provisioned resources |

See `docs/structure.md` for lazily created application directories. Terraform is
included, but no cloud project, database, firewall, or identity is created.

## Releases

Ignition baseline: **8.3.10**, verified against vendor stable downloads on 2026-10-07.
Upgrades are reviewed PRs, never floating `latest` updates. The included Dockerfile
is a development tool image, **not a production service**. Add an application-specific
runtime target and health check before enabling container release.

The manual deployment workflow models artifact promotion but environment adapters
deliberately fail until real deployment is implemented. Configure GitHub protections
before running it. Every PR updates an affected document and a descriptive change
record. Docs ship with changes; no automatic post-merge documentation commit is needed.