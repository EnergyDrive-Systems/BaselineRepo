---
name: code-review
description: "Use when reviewing a PR, branch, or diff for standards compliance, requirements coverage, regressions, missing tests, or unintended scope changes."
---

# Two-Part Code Review

## Prerequisites

Paths are repository-relative. Read `AGENTS.md`, `docs/standards.md`,
`docs/HANDOVER.md`, and the applicable `docs/profiles/` files. Identify the originating
issue, PRD, or approved acceptance criteria. Review is read-only unless fixes are requested.

For UI changes, automatically read `docs/profiles/ui.md`. Material Design 3 is the
default; check platform adaptations, accessibility, responsive/state coverage, and
actual interaction evidence rather than judging visual appearance alone.

## Workflow

1. Resolve the comparison base and head to commits and record both. Use the merge-base
   diff for a PR; use the intended baseline for an explicit commit review. Ask only if
   no reliable comparison is available. An empty diff is not evidence of correctness.
2. **Standards:** check touched code against applicable rules, test quality, runtime
   boundaries, documentation, and deployment obligations. Separate documented violations
   from design suggestions. Do not repeat every finding already explained by tooling.
3. **Requirements:** map acceptance criteria to behavior and evidence. Identify missing
   or partial requirements, incorrect implementation, regressions, and unintended scope.
   If the spec is unavailable, mark this axis unverified rather than passed.
4. Trace suspected defects through nearby callers/tests. Cite file/line, evidence,
   consequence, and a concrete remedy. Label uncertain findings and missing runtime checks.
5. Report Standards and Requirements separately, with severity-ordered findings within
   each. Preserve both conclusions; passing one must not mask failure of the other.

## Completion Evidence

Return comparison commits, requirement sources, findings for each axis, checks actually
performed, and unresolved risks. Say explicitly if no findings were identified and note
test gaps. Never imply agent review replaces required human review or release approval.