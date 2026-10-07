---
name: terraform-change-review
description: "Use when reviewing Terraform configuration or sanitized plans for resource replacement, drift, lifecycle exclusions, infrastructure ownership, costs, or recovery implications."
---

# Terraform Change Review

## Prerequisites

Paths are repository-relative. Read `AGENTS.md`, `docs/standards.md`,
`docs/profiles/terraform.md`, `docs/deployment.md`, and `docs/HANDOVER.md`.
Identify environment/root, comparison commits, tooling/provider locks, and intended scope.
Use sanitized reports only; never load raw state or secret-bearing plans into agent context.

## Workflow

1. Review configuration intent and dependency/lock changes. Run the documented pinned
   container's formatting and credential-free validation for affected roots where safe.
   Do not generate credentialed plans or apply/destroy/import/refresh live infrastructure.
2. Examine an existing sanitized plan for creates, changes, replacements, and deletes.
   Explain why each destructive or costly operation is necessary. Without a usable plan,
   distinguish configuration-only findings and mark runtime effects unverified.
3. Check environment/state boundaries, backend locking/versioning, deletion protection,
   ownership labels, cost assumptions, and module/provider compatibility against the profile.
   Flag hidden dependencies and changes affecting unrelated resources.
4. Trace ownership of service configuration versus release-promoted artifacts. Check
   narrowly justified lifecycle exclusions and post-release drift evidence; broad
   `ignore_changes` must not hide unintended divergence or revert pipeline releases.
5. Check approval evidence binds the exact source and reviewed plan identity. Document
   recovery/roll-forward implications, data persistence, and missing validation. Existing
   production rules remain authoritative; review does not grant execution authority.

## Completion Evidence

Return severity-ordered findings, root/environment, commit/plan identity if supplied,
replacement/drift/cost summary, checks run, and unresolved risks. Never certify an apply
from fmt/validate alone. Do not request credentials, print sensitive values, or execute
production actions to fill evidence gaps.