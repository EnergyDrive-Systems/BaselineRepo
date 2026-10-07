## Change

What changed, why, and which requirements/profiles are affected?

## Two-Part Review

Comparison base/head commits and originating issue or PRD:

- [ ] Standards compliance checked against the relevant rules and profiles.
- [ ] Requirements coverage checked against acceptance criteria and evidence.

Record separate conclusions. List standards findings, missing/partial requirements,
incorrect behavior, and unintended scope changes, or state none found. Missing
requirements mean coverage is unverified, not passed.

## Documentation

- [ ] Updated an affected project document.
- [ ] Added/updated this PR's `docs/changes/<descriptive-name>.md`.
- [ ] Updated PRD/handover/architecture/README where applicable.

Link changed docs and explain unaffected sections.

## Evidence

Actual commands/results and what remains unverified. Distinguish CPython/container
checks from real Ignition, database, infrastructure, and operational acceptance.

For UI changes (otherwise state Not applicable):

- [ ] Applied Material Design 3 and `docs/profiles/ui.md`, or linked an approved exception.
- [ ] Recorded responsive screenshots and actual interaction/state checks.
- [ ] Checked keyboard/focus, labels, contrast, touch targets, and scaling/accessibility.
- [ ] Documented platform limitations and preserved SCADA alarm/control conventions.

## Bug-Fix Evidence

For bug fixes, complete the following; otherwise state Not applicable.

- Expected versus actual behavior and reproducible command/runtime steps:
- Root cause supported by observed evidence:
- Before-fix failure and after-fix result for the regression check:
- Original scenario recheck, runtime limits, or reason automated coverage is impractical:

- [ ] Temporary instrumentation and throwaway fixtures removed.

## Risk And Release

Data/control effects, security/cost impact, migrations, deployment/rollback. Identify
release and operational approvers for affected operations.

- [ ] No secrets or sensitive state/exports added.
- [ ] Checks run in approved container/venv.
- [ ] No agent-executed production mutation or credential change.