# Guideline Refinements

2026-10-07: Incorporated reusable, non-access-related lessons from the reviewed archives
into existing standards and profiles. Added two-part PR review and bug-fix evidence to
both standards and the PR template. Refined data/time contracts, authoritative SQL
definitions versus migration history, deterministic generated bundles, migration parity
and cutover, alarm behavior, architecture versioning, and deployment-field ownership.

Updated handover to separate current state, verified evidence, gaps, and next actions.
No new top-level guidance documents, bulk skill imports, project-specific identifiers,
access-policy changes, workflow changes, or application changes were introduced.

Validation: 27 documentation structure/required-content checks passed. The existing
Security section compared unchanged, normalizing only line endings. Editor diagnostics
are checked separately. No runtime tests or remote deployment checks are claimed for
this documentation-only change.

Deployment/rollback: guidance only; no resource mutations. Revert wording through a
reviewed PR if needed. Existing container/venv rules and production restrictions remain.