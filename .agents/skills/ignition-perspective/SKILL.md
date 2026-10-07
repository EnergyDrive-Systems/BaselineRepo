---
name: ignition-perspective
description: "Use when designing or changing Ignition Perspective views, bindings, project scripts, Named Queries, tags, alarms, exports, or gateway acceptance tests."
---

# Ignition Perspective Workflow

## Prerequisites

Paths are repository-relative. Read `AGENTS.md`, `docs/standards.md`,
`docs/profiles/ignition.md`, `docs/structure.md`, and `docs/HANDOVER.md`.
Record actual gateway/module/Designer versions and confirm a safe dev/test gateway.

For view or interaction changes, automatically read `docs/profiles/ui.md` and apply
Material Design 3 through native components, shared style classes, reusable views,
and supported theme tokens. Preserve alarm/safety conventions and test accessibility;
do not claim native components automatically provide full M3 conformance.

## Workflow

1. Start at the affected resource and expected behavior. Prefer native bindings,
   Named Queries, tags/UDTs, alarms, and pipelines. Keep event scripts thin and place
   reusable logic in project libraries instead of duplicating it across views.
2. Respect embedded-runtime syntax and APIs; do not apply standalone CPython packages,
   typing/formatting rules, or `.venv` assumptions to gateway scripts. Avoid blocking
   network/database work in UI execution paths and document cache invalidation.
3. Track reviewable resources in Git. Preserve required metadata and distinguish project,
   tags/UDTs, and gateway configuration. Reconcile Designer edits before PR review;
   record dependencies, import order, provider mapping, and post-import enabled states.
4. Round-trip import/export in a clean matching non-production gateway. Test affected
   queries/bindings, freshness/quality, restart persistence, and desktop/mobile behavior.
   For alarms test source versus device failures, delays/deadbands, flapping, acknowledgement,
   escalation cancellation, journaling, recovery, and any risk-assessed suppression.
5. Update requirements, architecture, handover, and the PR record with actual runtime
   evidence and rollback limits. Observe existing rules for equipment-affecting behavior.

## Completion Evidence

List changed resources, target versions, packaging/import details, runtime tests/results,
unverified paths, and recovery implications. CPython/static validation is supplementary;
never report real gateway acceptance from it. Do not connect test resources to production
equipment or execute production imports as part of this workflow.