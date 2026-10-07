---
name: release-readiness
description: "Use when assessing a release candidate, deployment readiness, compatibility, migration sequencing, acceptance evidence, rollback, or handover completeness."
---

# Release Readiness Assessment

## Prerequisites

Paths are repository-relative. Read `AGENTS.md`, `docs/standards.md`,
`docs/deployment.md`, `docs/HANDOVER.md`, the project PRD, and active profiles.
This skill assesses evidence; it does not deploy, apply Terraform, migrate production,
issue equipment commands, or grant approvals. Use sanitized artifacts and reports.

## Workflow

1. Identify the exact source commit and immutable artifact checksum/image digest.
   Confirm the artifact tested is the artifact proposed for promotion, with recorded
   runtime versions, dependency locks, provenance, and relevant security results.
2. Check both review axes and required CI results. Verify real environment adapters
   and smoke checks exist; a successful no-op or development tooling image is not a release.
3. Assess compatibility across service/database/gateway versions, persistent data,
   imports, and job sequencing. For migrations, check parity/rehearsal and explicit
   cutover criteria; an HTTP health check alone does not validate data correctness.
4. Check target-runtime acceptance, operational effects, failure detection, backup/
   restore evidence, and rollback/roll-forward limits. Identify irreversible effects.
   Mark missing evidence as a blocker or risk, not an assumption.
5. Confirm the existing review/approval requirements are satisfied by recorded human
   decisions and configured pipeline gates. Update documentation and handover with
   current state, verified evidence, gaps, and next actions without duplicating the PRD.

## Completion Evidence

Return Ready for human decision, Not ready, or Unverified, with commit/artifact identity,
blocking gaps, residual risks, evidence references, and responsible next actions.
Readiness is not release authorization. Do not execute production workflows while
collecting evidence or request production credentials from the user.