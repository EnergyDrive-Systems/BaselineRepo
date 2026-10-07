---
name: diagnosing-bugs
description: "Use when debugging failures, incorrect results, intermittent faults, or performance regressions and collecting reproducible bug-fix evidence."
---

# Evidence-Based Bug Diagnosis

## Prerequisites

Paths are repository-relative. Read `AGENTS.md`, `docs/standards.md`,
`docs/HANDOVER.md`, and applicable profiles. Identify expected versus actual behavior
and the runtime in which it occurs. Use non-production fixtures; follow existing rules.

## Workflow

1. Establish and run the cheapest check that can catch the exact symptom: a focused
   test, CLI fixture, request, or repeatable gateway procedure. Record the failure.
   Minimize inputs without changing the failure; do not mistake a nearby error for it.
2. State a falsifiable local hypothesis and the observation that would disprove it.
   Inspect the nearest deciding code and use targeted instrumentation only as needed.
   Change one relevant variable at a time and rerun the discriminating check.
3. For intermittent faults, record trial count and reproduction rate. For performance
   faults, capture comparable inputs, runtime/load, and before/after measurements.
   Do not add uncontrolled sleeps or log sensitive payloads to manufacture evidence.
4. Add regression coverage at the real behavior boundary and show it fails before
   applying the fix. Make the smallest root-cause change, then run the same check
   immediately and recheck the user's original scenario.
5. Remove temporary instrumentation and throwaway fixtures. Update affected docs,
   handover, and the PR change record with the supported root cause and test results.

## Completion Evidence

Provide reproduction steps, root-cause evidence, before/after results, original-scenario
verification, and remaining uncertainty. If automation is impractical, document why
and provide repeatable runtime evidence for reviewer acceptance. A production-only
repro is a blocker for human investigation, not permission to instrument production.
CPython checks never prove a fault dependent on Ignition's embedded runtime is fixed.