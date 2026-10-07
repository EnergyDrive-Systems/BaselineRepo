# Your First Project

Follow this guide once with a disposable project such as **baseline-smoke-test**.
The result is an independent GitHub repository, a working container/virtual environment,
and an agent ready to discuss your project. It is not a deployed application.

The main walkthrough uses Windows and VS Code; container commands use Linux syntax.
On macOS/Linux the GitHub/editor steps are the same, but use a suitable local clone
folder. Linux hosts must provide workspace access to the container's UID 10001.

## 0. Prepare The Template And Your Computer

**Template owner:** publish the intended changes through a reviewed PR and merge them
before this test. A GitHub template copy includes published files, not local/uncommitted
edits. At https://github.com/EnergyDrive-Systems/BaselineRepo verify the default branch
contains `.devcontainer/devcontainer.json`, `compose.yaml`, `uv.lock`, `AGENTS.md`,
`CLAUDE.md`, and this guide. Enable **Settings > General > Template repository** if needed.
The organization URL was verified reachable; the template setting itself was not inspected.

**Project user:** install Git, VS Code, and Docker Desktop using your organization's
approved process. On Windows use Linux containers and complete any required WSL 2 setup.
Start Docker Desktop; check its organizational licensing. Have internet access for
images/packages and a GitHub account permitted to create repositories in EnergyDrive-Systems.

In VS Code Extensions, install **Dev Containers** by Microsoft
(`ms-vscode-remote.remote-containers`). Python on the host is not required.
Claude/Copilot additionally need their own approved account/subscription; none is supplied.

In a **host PowerShell terminal**, check:

```powershell
git --version
docker version
docker compose version
```

**Pass:** Git resolves, Docker reports both client and server, and Compose reports v2.
If Docker's server is unavailable, fix/start Docker before continuing. Administrator-only
installation or OS changes belong to the user/IT team, not the coding agent.

## 1. Create Your Project On GitHub

1. Open https://github.com/EnergyDrive-Systems/BaselineRepo.
2. Choose **Use this template > Create a new repository**. Do not choose Fork or
   independently initialize an empty repository for this walkthrough.
3. Select **EnergyDrive-Systems** as the owner, not your personal account. Enter
   **baseline-smoke-test** as the name (or another available project name).
4. Choose **Private** unless an owner has approved public publication. Leave inclusion
   of all branches off; start from the template's default branch.
5. Create the repository and check the address is
   `https://github.com/EnergyDrive-Systems/baseline-smoke-test`.

**Pass:** your project has its own GitHub address and includes the template files.
If Use this template is absent, ask the template owner to enable it. If the organization
is unavailable as an owner, resolve membership/creation permission; do not silently
publish personally. Repository secrets, review ownership, and protection/environment
settings must be configured for the new project; do not assume they copied with files.

## 2. Clone The New Project And Open VS Code

On **your new project's page**, choose **Code > HTTPS** and copy its URL. Clone that
repository, not BaselineRepo. In a host PowerShell terminal:

```powershell
New-Item -ItemType Directory -Force C:\repos | Out-Null
Set-Location C:\repos
git clone https://github.com/EnergyDrive-Systems/baseline-smoke-test.git
Set-Location baseline-smoke-test
git remote -v
git status --short --branch
code .
```

Replace baseline-smoke-test with the name you selected. Do not reuse an existing folder
with that name. Authenticate using GitHub's approved browser/credential flow; do not
paste passwords or tokens into commands, documentation, or agent chats.

**Pass:** origin fetch/push both name your new organization project, and the worktree
is initially clean. If `code` is not found, open VS Code and use **File > Open Folder**
to open the cloned folder; no re-clone is needed.

## 3. Reopen In The Development Container

1. Review the repository setup, then trust the workspace if appropriate.
2. Accept **Reopen in Container**. If no prompt appears, press **Ctrl+Shift+P**, search
   for **Dev Containers: Reopen in Container**, and select it.
3. Wait for the initial image build, dependency sync, and editor connection. This can
   take several minutes on a new machine. Read build/setup errors rather than retrying blindly.
4. Open **Terminal > New Terminal** in the reopened window.

**Pass:** VS Code's remote indicator identifies a Dev Container, and the terminal is
inside Linux at `/workspace`, not a host PowerShell prompt at `C:\repos\...`.
The startup hooks automatically run `uv sync --locked`; Python/Pylance/Ruff are configured
as container extensions. Accept their installation if your editor prompts for it.

Opening a folder alone does not silently attach or launch an app. No database, gateway,
Terraform operation, application server, or production connection starts here.

## 4. Verify The Environment And Baseline Checks

Run these in the **container terminal**:

```sh
pwd
id -u
uv --version
uv run --locked python -c "import sys; print(sys.version); print(sys.prefix); print(sys.executable)"
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pyright
uv run --locked pytest
```

**Pass:** pwd is `/workspace`; UID is `10001`; Python is 3.13.x with prefix
`/workspace/.venv`. The executable may end in `python` or `python3`; both are valid
when using that virtual environment. Ruff and Pyright pass, and the unchanged template
currently has 12 passing tests. Pyright may mention missing `src` before application
code exists; it must still report zero errors. Future template versions may add tests.

Use **Python: Select Interpreter** in the Command Palette if VS Code selected another
interpreter; choose `/workspace/.venv/bin/python`. The named-volume venv is not a host
Windows environment and may not appear in host Explorer.

For the dependency audit, also run:

```sh
sh scripts/audit_dependencies.sh
```

**Pass:** no unresolved audit findings. Do not disable checks or update the lockfile
just to hide a failure; record it and ask the template owner to investigate.

Terraform is optional for the first smoke test. Its documented commands run from a
**host terminal** through the separate Compose service; Docker is not mounted into
the development container. See [the root README](../README.md) for those commands.

## 5. Start Claude Code Or Another Agent

For the simplest Claude workflow, remain in the **container-connected VS Code window**.
Open Extensions, search **Claude Code** by Anthropic (`anthropic.claude-code`), and install
it in the Dev Container when that option is offered. Open its panel from the Command
Palette and sign in through the approved interactive flow. Complete sign-in directly
in the UI, never by giving credentials to an agent. Use a permission mode that lets
you review edits/commands for this first test; do not enable permission bypass.

The template does not install Claude automatically. The extension bundles its own
runtime for the panel but does not make a standalone `claude` executable available
on the terminal PATH. If your team wants CLI usage, arrange an approved, versioned
container installation using the [official container guide](https://code.claude.com/docs/en/devcontainer);
do not assume a host CLI installation exists inside the container.

For Copilot/Codex, install and sign in to the approved client in the same workspace.
Confirm its terminal/execution tools use the container and uv, not host Python.
Accounts, availability, permissions, and native skill discovery vary by client.

Send this first **read-only** prompt:

```text
Read CLAUDE.md if applicable, AGENTS.md, README.md, docs/standards.md,
docs/HANDOVER.md, and .agents/skills/README.md. Do not edit, commit, push,
deploy, or connect to external databases/equipment.
Summarize the rules for containers/venv, Material 3 UI, two-part review,
bug-fix evidence, documentation, and production restrictions.
Run pwd and uv run --locked python -c "import sys; print(sys.prefix)"
and report where execution actually occurs. List any unavailable tools.
```

**Pass:** the agent reports `/workspace` and `/workspace/.venv`, reads the shared policy,
and makes no edits. Claude's root entry point imports `AGENTS.md`; Copilot/Codex have
their own entry points. Do not mistake a confident summary for proof of tool location.
If native skill invocation is unavailable, ask it to read the named SKILL.md files
directly; no bulk plugin installation is necessary for this test.

## 6. Check Reopening And Record Your Test

Use **Dev Containers: Reopen Folder Locally**, close that project window, then open the
same folder and reopen in the container again. Repeat the Python prefix check and pytest.
Dependencies resync from the lockfile and the named-volume environment persists.
Do not run `docker compose down -v` as routine troubleshooting: it deletes volumes.

Record OS, VS Code/Docker versions, cloned URL and commit (`git rev-parse HEAD`), the
step that failed, exact error, and which commands passed. Redact credentials/private data
before sharing output. Use this acceptance checklist:

- [ ] New repository owner/address is EnergyDrive-Systems/my-project.
- [ ] Required template files are present and clone origin is correct.
- [ ] Container opens as developer at /workspace and .venv is selected.
- [ ] Lint, formatting, types, tests, and dependency audit pass.
- [ ] Agent reads shared guidance and proves its container execution location.
- [ ] Closing/reopening restores the working environment.

A successful local smoke test does not prove remote CI, client discovery in every agent,
real database/gateway behavior, or production release readiness.

## 7. Begin Real Project Work Through A PR

From the container terminal, create a project setup branch:

```sh
git switch -c setup/project-bootstrap
```

Ask the agent to read the grill-with-docs, grilling, and domain-modeling skill files,
then interview you about the actual project's purpose, users, active technologies,
acceptance criteria, and constraints. Confirm shared understanding before implementation.
Fill [PRD](PRD.md), replace inherited template-history handover entries with your project's
current state, and update [handover](HANDOVER.md). Preserve shared policy rather than
rewriting it as application-specific instructions. UI work defaults to Material 3.

Replace example CODEOWNERS, configure project protections/owners with the responsible
human, and add `docs/changes/project-bootstrap.md`. Add application directories only when
real code/resources exist. Renaming the Python project requires intentional lockfile
regeneration (`uv lock`) followed by locked sync and verification; it is not needed for
the smoke test. Never edit `uv.lock` manually.

Review the changes, commit on the setup branch, and publish that branch through VS Code
Source Control or your approved Git workflow. Open a PR to main; do not publish directly
to main. If Git asks for an author identity or authentication, configure your own approved
identity/credential flow, not the template author's. Remote CI and documentation checks
must pass before review/merge. Test results belong in the PR's change record.

There is no app to run until it is implemented. Specify its startup command, port,
runtime container, and integration fixtures in the project PRD/README. Do not enable
deployment simply because the environment smoke test passed; follow
[deployment guidance](deployment.md) and keep production adapters blocked until ready.

## Quick Troubleshooting

| Symptom | Check / Next Action |
| --- | --- |
| Wrong GitHub owner | Stop before cloning; create under the organization or arrange an approved transfer. |
| Clone reports not found | Confirm the project's exact URL and your account's access; private repositories may look absent. |
| Missing template files | Check the template default branch and publish/merge the intended version first. |
| No reopen command | Install Microsoft's Dev Containers extension and review workspace trust. |
| Docker connection/build error | Check Docker Desktop is running with Linux containers; inspect the Dev Containers log and network access. |
| Python prefix is not /workspace/.venv | Use the container terminal and uv; correct the editor interpreter. |
| Linux permission denied | Resolve workspace access for UID 10001 with IT/project owners; do not switch to root or weaken permissions blindly. |
| Lockfile mismatch | Confirm the correct published project version; review intended dependency changes and regenerate through uv if approved. |
| Claude is missing or not logged in | Install the extension in the container window and complete its own sign-in; terminal CLI is separate. |
| Git push unavailable inside container | Use the approved host Git/VS Code authentication workflow; never embed tokens in remote URLs. |

For this first test, stop at the first unexplained failure and share its step/result.