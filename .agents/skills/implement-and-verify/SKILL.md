---
name: implement-and-verify
description: "Use when implementing agreed requirements or fixes through small changes, focused container and venv validation, and accompanying documentation updates."
---

# Implement And Verify

## Prerequisites

Paths are repository-relative. Read `AGENTS.md`, `README.md`, `docs/standards.md`,
`docs/structure.md`, `docs/HANDOVER.md`, and active profiles. Confirm agreed requirements
and acceptance criteria. For unresolved design, use `grill-with-docs`, loading `grilling`
and `domain-modeling` separately, with a read-file fallback when Skill tools are absent.

## Workflow

1. Inspect the nearest owning implementation and test boundary. Preserve contributor
   changes and choose a small, falsifiable implementation hypothesis and acceptance check.
   Create only directories with real content; do not introduce speculative abstractions.
2. Add a failing acceptance/regression check where practical. Implement one useful
   slice and immediately run its cheapest discriminating validation before widening scope.
   Repair within that slice or revise the hypothesis according to the result.
3. Use the documented container commands and uv-managed `.venv` for standalone Python.
   Apply the explicit Designer/Ignition/Terraform runtime exceptions. Run relevant lint,
   types, tests, and dependency/configuration checks; do not weaken failing gates.
4. Validate contracts and failure paths on the actual target runtime where necessary.
   Distinguish fixtures/static checks from real database, gateway, and integration evidence.
5. Update affected PRD/architecture/README sections, handover, and this PR's change record.
   Use `code-review` for separate standards and requirements conclusions before delivery.
   Read another skill's file directly when invocation tools are unavailable.

## Completion Evidence

Report requirements covered, files changed, actual commands/results, unperformed checks,
and deployment/rollback implications. Do not declare completion with unresolved required
gates. Follow existing production restrictions; implementation never authorizes release.