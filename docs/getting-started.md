# Your First Project

This guide is for someone starting a project, not maintaining the template. You can
follow the main steps by clicking buttons and menus; no terminal commands need to be
typed. Ask your project lead or IT contact to help with installation or permissions.

The result is your own project repository, a ready development environment, and an
agent helping you plan your application. The template itself is not a running app.

Prefer the visual walkthrough? Open the separate
[17-slide infographic](presentations/first-project.html) or
[standalone PDF](presentations/first-project.pdf). It follows the same GUI-first path,
with expected results, a beginner-friendly agent prompt, and troubleshooting.

The examples use Windows. On a Mac, use Command instead of Ctrl for editor shortcuts
and select a suitable local folder. Linux users should ask their technical helper to
check folder permissions before starting. Technical commands are in the optional
helper appendix at the end, not in the main walkthrough.

## A Few Words You Will See

| Word | Plain-English Meaning |
| --- | --- |
| Repository / repo | The project's files and saved history on GitHub. |
| Template | A prepared starting set of files for a new project. |
| Clone | Download a working copy linked to your GitHub project. |
| Container | An isolated workspace with the project's development tools. |
| Virtual environment / .venv | The project's own Python environment, set up for you. |
| Branch | A separate workspace for changes before they are reviewed. |
| Commit | A named save point in the project's history. |
| Pull request / PR | A request for someone to review your branch before merging it. |

## 1. Get Your Computer Ready

Ask IT or your project lead to make sure these are installed: **Git**, **VS Code**, and
**Docker Desktop**. Git runs behind VS Code's buttons; you do not need to learn Git
commands for this guide. Installation, Windows WSL 2 setup, organizational licensing,
and administrator-only changes belong to you/IT, not the coding agent.

1. Open **Docker Desktop** from the Start menu and wait until it says the engine is
   running. On Windows the setup must use Linux containers; ask IT if unsure.
2. Open **VS Code**, then click **Extensions** (the four-squares icon on the left).
3. Search **Dev Containers**, select the extension published by **Microsoft**, and click
   **Install**. Its identifier is `ms-vscode-remote.remote-containers`.
4. Sign in to GitHub through VS Code's **Accounts** menu when needed. Use your approved
   organization account. Keep a browser signed in to GitHub too.

**You should see:** Docker is running and Dev Containers is installed in VS Code.
You do not need to install Python on your computer. Internet is needed for the first
setup. Claude/Copilot/Codex require their own approved account/subscription; the template
does not provide those accounts.

## 2. Create Your Project On GitHub

1. Open https://github.com/EnergyDrive-Systems/BaselineRepo.
2. Choose **Use this template > Create a new repository**. Do not choose Fork or
   independently initialize an empty repository for this walkthrough.
3. Select **EnergyDrive-Systems** as the owner, not your personal account. Enter
   your project name, for example **my-first-project**.
4. Choose **Private** unless an owner has approved public publication. Leave inclusion
   of all branches off; start from the template's default branch.
5. Create the repository and check the address is
   `https://github.com/EnergyDrive-Systems/my-first-project`.

**You should see:** your project name beside **EnergyDrive-Systems** on GitHub, with
files such as README.md and a `.devcontainer` folder. If your lead already created the
project, use the link they provided and continue to Step 3; do not create a duplicate.
If Use this template is absent, ask the template owner to enable it. If the organization
is unavailable as an owner, resolve membership/creation permission; do not silently
publish personally. Your project lead configures ownership, protections, and deployment
settings separately; you do not need to set those up just to open the project.

## 3. Download And Open The Project In VS Code

1. On **your new project's GitHub page**, click **Code**, choose **HTTPS**, and click the
   copy icon beside the address. Copy your project, not BaselineRepo.
2. In VS Code, choose **View > Command Palette** (or Ctrl+Shift+P). This is a menu-search
   box, not a terminal. Search **Git: Clone** and select it.
3. Paste the copied address and press Enter. If asked, sign in using the browser flow.
4. Choose a parent folder such as `C:\repos` using the folder picker. You can create
   that folder through File Explorer first. VS Code creates a project folder inside it.
5. When cloning finishes, click **Open** or **Open in New Window** when prompted.

**You should see:** the project folder and README in VS Code's **Explorer** (the files
icon). Source Control should initially have no changed files. Check the project name
matches the GitHub page you copied; ask your helper if you are unsure about the connection.

Do not clone into an existing folder with the same name. Use the approved sign-in flow;
never put passwords/tokens in the project address, files, or agent messages.

## 4. Open The Prepared Development Environment

1. Review the repository setup, then trust the workspace if appropriate.
2. Accept **Reopen in Container**. If no prompt appears, press **Ctrl+Shift+P**, search
   for **Dev Containers: Reopen in Container**, and select it.
3. Wait for the initial image build, dependency sync, and editor connection. This can
   take several minutes on a new machine. Read build/setup errors rather than retrying blindly.
4. Keep this reopened window for project work. There is no need to open or type into
   a terminal to complete the main guide.

**You should see:** the bottom-left remote indicator identifies a **Dev Container**.
Python, Pylance, and Ruff install inside it; accept installation prompts if shown.
The project's Python environment and locked dependencies are prepared automatically.
If the window is still local or setup shows an error, stop and ask for help before editing.

Opening a folder alone does not silently attach or launch an app. No database, gateway,
Terraform operation, application server, or production connection starts here.

## 5. Check That Setup Worked Using Menus

1. In the container-connected window, choose **Terminal > Run Task**. You are selecting
   a named action, not typing a command. If the menu differs, open the Command Palette
   and choose **Tasks: Run Task**.
2. Select **Baseline: Run All Quality Checks**.
3. A results panel opens and each check runs. Leave it to finish; you do not need to
   type into this panel. The dependency audit needs internet access.
4. Confirm the checks finish successfully. The six results end in **PASS** messages:
   environment, lint, format, types, tests, and audit.
   The final message is **All six quality checks passed. Your development setup is ready.**

**You should see:** **Environment ready**, Python 3.13.x, and `/workspace/.venv` in the
environment result. Types have zero errors, tests pass (the starter currently has 12),
and the audit has no unresolved findings. A missing `src` message before application
code exists is normal if the type check still reports zero errors.

The check tasks do not fix files or deploy anything. They require the approved container;
a location/user mismatch fails rather than silently running checks on the host.

To rerun just one check, return to **Run Task** and select it, for example
**Baseline: Run Tests**. For a test-results view, click **Testing** (the beaker icon).
If hidden, use **View > Open View**, search Testing, and open it. Click its Run All Tests
button. If tests do not appear, run **Python: Configure Tests** from the Command Palette,
choose pytest and the tests folder, or ask your helper. The menu task still works.

If the Python interpreter is wrong, open the Command Palette, choose **Python: Select
Interpreter**, then select `/workspace/.venv/bin/python` (use Enter interpreter path
if needed). You do not need to find a Windows `.venv` folder in File Explorer.

If any check fails, note which one and show the results to your helper. Do not disable
checks or change dependency versions to hide the failure. Terraform/cloud setup is not
part of this beginner flow; your technical lead handles it when required.

## 6. Open Claude Code Or Your Approved Agent

For the simplest Claude workflow, remain in the **container-connected VS Code window**.
Open Extensions, search **Claude Code** by Anthropic (`anthropic.claude-code`), and install
it in the Dev Container when that option is offered. Open its panel from the Command
Palette and sign in through the approved interactive flow. Complete sign-in directly
in the UI, never by giving credentials to an agent. Use a permission mode that lets
you review edits/actions while learning; do not enable permission bypass.

The template does not install Claude automatically. The extension bundles its own
runtime for the panel but does not make a standalone `claude` executable available
on the terminal PATH. The panel is sufficient for this guide. A terminal-based Claude
installation is optional work for your technical lead, not a beginner prerequisite.

For Copilot/Codex, install and sign in to the approved client in the same workspace.
Ask the agent to confirm its execution tools use the container, not host Python.
Accounts, availability, permissions, and native skill discovery vary by client.

Send this first **read-only** prompt:

```text
I am new to this project. Read the repository's shared agent instructions,
README, standards, handover, and skill index. Do not change any files,
commit, push, deploy, or connect to external databases or equipment.
Explain the main rules in plain language, including Material 3 UI design,
review, bug-fix evidence, documentation, and production restrictions.
Use the project's environment check inside the development container.
Show the actual result and tell me whether setup is ready. If a tool is
unavailable, say so rather than guessing. Wait for me before making changes.
```

**You should see:** the agent reports `/workspace` and `/workspace/.venv`, reads the policy,
and makes no edits. Claude's root entry point imports `AGENTS.md`; Copilot/Codex have
their own entry points. Do not mistake a confident summary for proof of tool location.
If native skill invocation is unavailable, ask it to read the named SKILL.md files
directly; no bulk plugin installation is necessary for this test.

## 7. Describe What You Want To Build

Tell the agent your goal, who will use the project, and what success looks like. For example:

```text
I want to build [describe the goal] for [the users]. Use the requirements
interview and domain-modeling workflows. Ask me the necessary questions
and recommend sensible choices. Do not implement anything until we agree.
Help me document the requirements and current project state afterward.
```

Open **Explorer > docs > PRD.md** to see the requirements document, and HANDOVER.md
for current state and next steps. Ask the agent to replace inherited template-history
entries with your project's state, without rewriting shared policy. Confirm its summary
before allowing implementation. New/changed UIs use Material Design 3 by default.

Your project lead selects technologies, configures reviewers/protections, and handles
infrastructure/access decisions. You are not expected to administer those settings.

## 8. Save Changes For Review Using The GUI

Before the agent edits project files:

1. Click the branch name (usually **main**) in VS Code's bottom-left status bar.
2. Choose **Create new branch** and name it **setup/project-bootstrap**. Alternatively,
   search **Git: Create Branch** in the Command Palette.
3. Confirm the status bar now shows that branch, not main. Ask the agent to update PRD,
   handover, and `docs/changes/project-bootstrap.md`, then review its changes.
4. Open **Source Control** (the branch icon). Click each changed file to see its diff.
   Stage only intended files using the **+** buttons. Do not stage secrets or generated data.
5. Enter a short commit message, such as **Set up project requirements**, then click
   **Commit**. If asked for Git identity/sign-in, get help configuring your own account.
6. Click **Publish Branch** when available. Do not choose Publish to GitHub to create
   another repository: this project already has its GitHub destination.
7. Return to your project's page on GitHub. Use **Compare & pull request**, or
   **Pull requests > New pull request**. Set base to main and compare to your setup branch.
8. Complete the PR description with evidence, create the PR, and request the designated
   reviewer. Wait for required checks and independent approval before merge.

**You should see:** a PR in the correct organization project, with your setup branch
compared to main. Do not commit/publish directly on main, bypass checks, or merge your
own changes without the required review. Ask your lead if Publish Branch is unavailable
or the sign-in/identity dialogs are confusing; do not put credentials in chat.

There is no application to run until one is built. Your project README should eventually
describe its own start button/task, local address, and fixtures. Development setup alone
does not permit production deployment; [deployment guidance](deployment.md) still applies.

## 9. Come Back To The Project Later

1. Save files and close the project window. Do not delete containers/volumes to close it.
2. Next time, start Docker Desktop and use **VS Code > File > Open Recent** to select
   the project. If needed, choose **Reopen in Container** again.
3. Check the Dev Container indicator and rerun **Baseline: Run All Quality Checks**.

**You should see:** the same files and project environment, with passing checks again.
Dependencies resync automatically. Ask for help before any reset/delete-volume operation.

## If Something Goes Wrong

Stop at the first unexplained error. Tell your helper the step, what you clicked, what
you expected, and what appeared instead. A screenshot is useful; remove credentials
and private data before sharing it. Find VS Code's version in **Help > About** and Docker's
version in Docker Desktop's About menu if requested. Do not post sign-in codes or tokens.


| Symptom | Check / Next Action |
| --- | --- |
| Wrong owner / cannot create project | Ask your lead to create it under EnergyDrive-Systems or arrange transfer. Do not use a personal repo as a workaround. |
| Clone says repository not found | Check the address copied from your new project and browser sign-in; ask your lead about access. |
| No Use this template / missing files | Ask the template owner to publish the current version and enable template use. |
| VS Code says Git is missing | Ask IT to install Git, then restart VS Code. |
| No Reopen in Container / no tasks | Check Microsoft's Dev Containers extension and that the current template was copied. |
| Docker or container setup fails | Open Docker Desktop and wait for the engine; use the Dev Containers log link and share the first error with IT. |
| Check task fails / Python looks wrong | Confirm the Dev Container indicator; use Python: Select Interpreter or ask your helper. No commands need to be typed. |
| Tests are not shown in Testing | Use Baseline: Run Tests from Run Task; ask for test-discovery help if needed. |
| Claude missing / not signed in | Install Claude Code in the container window and complete its browser sign-in. |
| Commit / Publish Branch unavailable | Confirm the setup branch and Source Control state; ask your helper about identity/sign-in. Do not create a second personal repository. |
| Permission denied / lockfile error | Stop and ask your technical lead. Do not switch to root, edit lockfiles, or weaken checks. |

## Ready-To-Start Checklist

- [ ] The GitHub project belongs to EnergyDrive-Systems and has the expected name.
- [ ] VS Code shows the right folder and a Dev Container connection.
- [ ] All six menu-driven checks pass; Testing can show the starter tests.
- [ ] The agent reads shared instructions, shows real setup results, and waits for approval.
- [ ] Project requirements are agreed before implementation.
- [ ] Changes go through a branch and reviewed PR, not directly onto main.
- [ ] Reopening the project restores its environment and passing checks.

This confirms development setup, not every agent's native skill discovery, database/
gateway integration, remote CI, accessibility conformance, or production readiness.

## Template Owner / Technical Helper Appendix

Beginners can stop above. The owner ensures the published template has the current
guide, `.devcontainer/devcontainer.json`, `.vscode/tasks.json`, `compose.yaml`, `uv.lock`,
`AGENTS.md`, and `CLAUDE.md`. Enable **Settings > General > Template repository** if needed.
Merge intended template changes through a reviewed PR before asking users to copy it;
uncommitted local edits do not appear on GitHub. Configure real CODEOWNERS, protections,
environments, and approvals per project; none is established by copying files.

Linux workspace access must accommodate UID 10001. Installation and cloud/Terraform setup
are helper responsibilities. Do not mount the Docker socket or production credentials
to make beginner checks work. If project metadata/dependencies change intentionally,
regenerate locks through uv and rerun checks; never edit `uv.lock` manually.

Optional **host PowerShell** diagnostics:

```powershell
git --version
docker version
docker compose version
```

Optional **container terminal** diagnostics/checks (the tasks already run these tools):

```sh
pwd
id -u
uv --version
uv run --locked python -c "import sys; print(sys.version); print(sys.prefix); print(sys.executable)"
uv run --locked ruff check .
uv run --locked ruff format --check .
uv run --locked pyright
uv run --locked pytest
sh scripts/audit_dependencies.sh
```

Expect /workspace, UID 10001, and /workspace/.venv; python/python3 aliases are both valid
when resolving to that environment. For optional Terraform tooling, use the separate
Compose service from the host as documented in [the root README](../README.md).
The GUI installation flow for Claude is covered in its
[official VS Code guide](https://code.claude.com/docs/en/vs-code); optional versioned CLI
installation belongs in the approved container, not as a presumed host dependency.