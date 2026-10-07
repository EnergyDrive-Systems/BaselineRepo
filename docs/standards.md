# Engineering Standards

## Required Baseline

- Git owns reviewable Python, Ignition resources, SQL, and IaC. Emergency gateway edits
  must be reconciled into a reviewed PR before the next release.
- Develop in containers. Standalone Python uses a `.venv`; Designer is a desktop
  exception, Ignition uses its embedded runtime, and Terraform uses its tooling container.
- Select active profiles and record versions, data flows, owners, environments, and
  write effects in the PRD. Avoid unused frameworks and database dependencies.
- Use small modules, explicit typed Python contracts, parameterized SQL, validated
  inputs, redacted structured logs, timeouts, and bounded retries.
- Test behavior and failures. Cover authorization, data contracts, idempotency, and
  control-write boundaries according to risk; coverage percentage is not proof.
- Commit dependency/provider locks; pin reviewed image digests and action/skill
  versions. Intentionally update them and scan dependencies, images, and secrets.
- Service containers run non-root, handle termination, provide meaningful health
  checks, and keep mutable data outside images. Tooling containers are not services.

## Change Control

Every PR requires independent human review, required green checks, an updated affected
document, and its own change record. Update PRD for requirements/behavior, handover for
state/gaps, diagrams for data flows, and README for setup/layout. Even maintenance PRs
update handover plus a record. After merge, docs must describe delivered behavior.

Production release approval is separate from code review. Control writes require
operational approval too. Small-team exceptions need a dated owner, justification,
expiry, compensating controls, and risk acceptance in `docs/adr/`; agents cannot grant
exceptions. Create ADRs only for consequential choices with real trade-offs.

## Two-Part Review

Review the same change against two separate criteria; passing one does not imply
passing the other. Record the base/head commits and the originating issue or PRD.

- **Standards compliance:** check the relevant engineering/profile rules, test quality,
  maintainability, and deployment/documentation obligations. Distinguish documented
  violations from subjective design suggestions; tooling success is only part of review.
- **Requirements coverage:** map acceptance criteria to implementation and evidence.
  Record missing/partial requirements, incorrect behavior, and unintended scope changes.
  If requirements are unavailable, report coverage as unverified, not passed.

Keep findings and conclusions separate. Resolve blocking findings before merge; any
intentional scope change must update the agreed requirements in the same PR.

## Bug-Fix Evidence

For bug fixes, record expected versus actual behavior and a reproducible command or
runtime procedure that catches the reported symptom. Minimize the failing case, state
the supported root cause, and add a regression test at the boundary where it occurs.
Demonstrate failure before the fix and success afterward, then recheck the original
scenario; absence of an exception is not proof of correct behavior.

Pin inputs, time, and fixtures where practical. For intermittent faults, report the
reproduction rate and remaining uncertainty. For performance fixes, record comparable
before/after measurements. If automated regression coverage is impractical, document
why and provide repeatable runtime evidence for reviewer acceptance. Remove temporary
instrumentation and throwaway fixtures before completion. Ignition evidence must use
its actual runtime where the symptom depends on gateway behavior.

## Security

Agents have no production credentials or execution authority. Use non-production
fixtures and explicitly authorized least-privilege reads. Application runtime R/W
identities are separately approved. Password rotation requires explicit owner approval
and a restricted execution workflow; never let agents change database passwords.

Keep secrets in approved secret stores and inject them at runtime. Prefer short-lived
identities/OIDC. Separate environments. Never commit `.env`, state, sensitive datasets,
backups, certificates, or plan files; do not send them to agents. Audit writes without
logging sensitive payloads. Untrusted PR jobs have no cloud/production credentials.

Do not use `pull_request_target` to execute contributor code. Protect workflow/policy
changes with real CODEOWNERS. Agent instructions guide; GitHub settings, CI, IAM, and
application authorization enforce. Do not silently disable checks or broaden permissions.

## Evidence

PRs record actual commands/results, unverified runtime behavior, and rollback impact.
CPython tests do not prove Jython or gateway behavior. Security exceptions must be
reviewed and time-limited. A deployment stub or checklist is never successful deployment.