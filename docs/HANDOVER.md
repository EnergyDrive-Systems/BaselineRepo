# Handover

## Current State

2026-10-07: Organizational starter for containerized Python and Ignition Perspective,
database profiles, Terraform, and GitHub CI/CD. Git owns source; agents have no production
execution authority. No application, real cloud resources, production identities, or
working deployment adapters are included. No GitHub protections have been configured.

This working folder was not a Git repository when inspected. Nothing pushed/deployed.

2026-10-07: Refined standards with separate standards/requirements review and bug-fix
evidence, plus data contracts, SQL source/generation, migration acceptance, alarm behavior,
and infrastructure/release ownership. Existing access policies remain unchanged.

2026-10-07: Added seven repository-owned skills for review, diagnosis, implementation,
release readiness, Ignition Perspective, database changes, and Terraform changes.
The skill index and root agent routing reference them; existing access policies remain.

2026-10-07: Added Compose-backed VS Code Dev Container configuration and a host extension
recommendation. Creation/start syncs the container `.venv` automatically; interpreter
and pytest settings target it. The user still selects Reopen in Container. No app or
external service auto-start tasks were copied from the reference project.

2026-10-07: Located the original EnergyDrive PNG in the RappCloud report assets and
added it under `assets/brand/` for project reuse. README displays it; usage notes record
provenance and resolution limits. No report code or unrelated project files were imported.

2026-10-07: Added the mandatory Material Design 3 UI profile and default agent routing.
Implementation, review, and Perspective skills plus the PR template require UI evidence.
Perspective adapts the principles through native resources; existing safety/access rules
and unrelated contributor changes remain unchanged.

2026-10-07: Added a branded five-slide infographic under `docs/presentations/`, with
offline browser navigation and a standalone 16:9 PDF. It includes Material 3 and the
original small EnergyDrive logo, and distinguishes scaffolding from project activation.

2026-10-07: Added a first-project walkthrough from GitHub template creation through
clone/container/venv checks, agent startup, reopening, and project setup PR. The intended
organization repository was verified reachable; the local origin still uses its old
personal-owner URL. Latest local documentation changes must be published before a fresh
GitHub copy can include them. No remote settings, commits, pushes, or new projects were
created by the agent.

## Next Actions

- [ ] Complete PRD and assign reviewer, release and operational approvers.
- [ ] Add real CODEOWNERS, required checks, and default-branch protection.
- [ ] Protect test/production environments and prevent self-approval.
- [ ] Verify runtime/image versions, profiles, and licenses.
- [ ] Add application/SQL/Ignition resources, matching tests, runtime container targets.
- [ ] Implement real deployment/smoke adapters and immutable digest promotion.
- [ ] Configure Terraform backend/locking/providers and restricted plan/apply.
- [ ] Configure OIDC/secret stores without production credentials in agent tools.
- [ ] Demonstrate integration, gateway acceptance, backup/restore, and rollback.
- [ ] Verify skills discovery in each enabled client and review updates.
- [ ] Confirm first-open/reopen behavior and interpreter/extension selection in VS Code
	on each supported host OS; Windows lifecycle startup was verified with the CLI.
	- [ ] Follow docs/getting-started.md against a new organization template copy; record
		first-open, agent, reopening, CI, and any permission/authentication failures.

## Unresolved Gaps

Template checks do not prove real gateway, database, infrastructure apply, or deployment
behavior. Remote GitHub checks, project-specific runtime acceptance, and real deployment
adapters remain outstanding. This refinement is guidance, not new CI enforcement of
review quality, SQL freshness, or migration parity; projects must implement those checks
where applicable.

## Verified Evidence

Local verification passed: 12 policy/adapter tests, lint/format, strict typing,
dependency audit, source secret scan, fixable high/critical image gate, Compose build,
workflow lint, and credential-free Terraform validation. See the baseline change record
for exclusions. The base image is digest-pinned; distribution security updates are
applied at build time, so record the resulting image digest rather than assuming
separate rebuilds produce identical bytes.

These results are from initial template verification, not a rerun for the documentation
refinement. Record new evidence in the corresponding change record. Keep handovers focused
on current state, verified evidence, unresolved gaps, and next actions; requirements
remain in PRD. Update this file in maintenance PRs and whenever state/gaps change.

Skill addition: all seven new workflows passed YAML metadata, structure, reference,
and index/routing validation in the container `.venv` (94 assertions). This does not
prove client discovery or real workflow execution; the onboarding check remains open.

Dev Container: JSON/Compose checks and actual lifecycle startup passed using Dev Containers
CLI 0.80.2 on Windows. Both locked-sync hooks completed and the container stayed running
as `developer`. VS Code GUI attachment/extension installation and other host OS behavior
remain unverified; no active editor window was reopened by the agent.

Runtime checks also confirmed the configured `.venv` interpreter, UID 10001, and installed
pytest. The CLI-created validation container was stopped; existing named volumes were
retained. Reopen in Container starts the environment again.

Brand asset: visual identity, original/copy SHA256 equality, 210 x 60 image decoding,
opaque alpha, and README image references were verified. A higher-resolution/vector
brand master is not supplied by the reviewed archive.

Material 3: 31 policy/routing checks, edited-skill YAML/reference validation in the
container `.venv`, and editor diagnostics passed. Existing Security policy was verified
unchanged against Git. Actual UI usability/accessibility requires per-project runtime
evidence; these checks validate instructions, not rendered interface conformance.

Presentation: JavaScript syntax, all five slide layouts at 1440/390/320 pixels, logo
loading, keyboard navigation/boundaries, and mobile control hit areas passed. Desktop
screenshots were inspected. A real browser generated the PDF; a container-side parser
verified five 16:9 pages with expected headings/footers. Integrated-browser print-media
emulation was unreliable, so export evidence comes from the real browser instead.

Onboarding guide: organization Git URL reachability, required-step/configuration checks,
nine document links, container path/UID/venv, lint/format/types, 12 tests, dependency audit,
and editor diagnostics passed. A human end-to-end test of a new GitHub template copy,
VS Code GUI, agent sign-in, and reopen behavior remains outstanding. Publish the guide
through a reviewed PR before expecting it in a new GitHub copy.