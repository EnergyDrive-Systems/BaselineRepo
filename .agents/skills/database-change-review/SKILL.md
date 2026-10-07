---
name: database-change-review
description: "Use when reviewing BigQuery, PostgreSQL, or SQL Server queries, SQL objects, generated bundles, migrations, time/data contracts, parity, or query-cost changes."
---

# Database Change Review

## Prerequisites

Paths are repository-relative. Read `AGENTS.md`, `docs/standards.md`,
`docs/profiles/databases.md`, `docs/structure.md`, and `docs/HANDOVER.md`.
Identify dialect/engine version, affected contracts, comparison commits, and intended
effects. Review is read-only; validation uses non-production fixtures under existing rules.

## Workflow

1. Map changed queries/objects to consumers and acceptance criteria. Check parameterized
   values, identifier handling, result bounds, timeouts, and failure/retry/idempotency behavior.
   Use dialect-specific semantics; SQLite tests cannot certify PostgreSQL/SQL Server behavior.
2. Verify authoritative object definitions versus immutable migration history. Generated
   bundles need deterministic inputs/order/hashes and a freshness check. Do not approve
   hand-edited outputs or unsupported executable translation approximations.
3. Review units/precision, null versus zero, timestamp identity, timezone/DST and interval
   boundaries, duplicate/completeness rules, quarantine, and effective-dated overlap/gaps.
4. Assess schema/routine compatibility, historical-data coverage, backfills, locks,
   job sequencing, representative parity, rehearsal, cutover gates, and recovery limits.
   Check PostgreSQL transaction/isolation or SQL Server driver-specific behavior as relevant.
5. For BigQuery, inspect partitions/filters, scan estimates, bytes-billed limits, quotas,
   and the chosen batch/stream/DML semantics. Dry-run evidence must name its environment;
   do not execute production jobs merely to assess cost.

## Completion Evidence

Report findings by severity with object/consumer, evidence, consequence, and remedy.
Separate static conclusions, actual engine tests, and missing evidence. Record cost,
compatibility, and rollback impacts in the PR change record. No production SQL execution,
schema changes, password changes, or invented parity results are permitted.