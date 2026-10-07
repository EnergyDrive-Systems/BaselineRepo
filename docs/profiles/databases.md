# Database Profiles

Record connection owners, classification, schemas/datasets, permissions, retention,
and recovery. Keep organization-specific names and credentials out of the template.

## Shared

- Parameterize values; allowlist identifiers. Never concatenate user input into SQL.
  Store dialect-specific queries separately.
- Separate read-only, runtime R/W, migration, and IaC identities. Agents never obtain
  production write identities. Tests must refuse production targets.
- Version migrations and test representative non-production data. Document locking,
  backfills, compatibility, and rollback/roll-forward. Applied migrations are immutable;
  destructive changes need owner approval.
- Bound results, timeouts, and retries. Use contract tests, idempotent writes, audit
  trails, and observability. Database updates consumed as equipment commands are control writes.
- Use approved TLS/short-lived authentication. Production mutations, IAM/network, and
  password changes require owner approval and restricted workflows.

## Data Contracts

Define units, precision, timestamp meaning (event, ingestion, or interval start/end),
and interval boundary semantics. Use UTC instants for event identity and explicit IANA
timezones for local-calendar rules. Test daylight-saving gaps/repeated times and reject
ambiguous local inputs unless an offset or occurrence is supplied. Do not guess a zone.

Distinguish missing, invalid, stale, and genuine zero values. Specify completeness and
duplicate rules; quarantine invalid batches/windows with diagnostics rather than
silently overwriting valid data or inventing defaults. Define reconciliation and retry
behavior. Effective-dated records need explicit overlap/gap rules and boundary tests;
do not force one interval convention onto unrelated business domains.

## SQL Source And Generation

Keep one authoritative current definition per managed SQL object under the selected
dialect's `objects/` directory. Generated deployment bundles are outputs, not a second
editable source. Mark generated files, record input hashes/order, and provide a
deterministic generator plus a CI freshness check before relying on those bundles.

Current object definitions and immutable migration history have different purposes.
Changes update the current definition and add a migration when needed; do not rewrite
applied migrations or substitute hash-based object deployment for migration history.
Document dependency order and validate generated SQL on the target database engine.

## Migration Acceptance

Define source/target mappings and unsupported constructs explicitly. Preserve traceability
to sanitized source artifacts; unsupported translations fail closed with recorded gaps,
not executable approximations. Test semantic equivalence, not merely syntax conversion.

Before cutover, rehearse on representative non-production data and compare keys, row
coverage, aggregates, null handling, precision, timestamps, and business results. Include
historical/inactive data where in scope. Document compatibility sequencing for readers,
writers, and jobs, any maintenance pause, exact acceptance criteria, and rollback limits.
Resume processing only when agreed checks pass. Compatibility removal is a separate
reviewed step after consumers migrate; retention periods remain project-specific.

## BigQuery

Use the official API/client or approved connector. Require dry runs where available,
maximum bytes billed, appropriate partition filters, explicit columns, and scan-cost
estimates for scheduled queries. Dry runs do not estimate all ingestion/storage costs.
Avoid unrestricted polling scans. Scope datasets/job privileges narrowly.

Choose batch load, Storage Write API, or DML deliberately. Record volume, latency,
deduplication, retry/reconciliation, quotas, dataset location, encryption, retention,
and deletion requirements. Do not treat BigQuery as PostgreSQL OLTP.

## Cloud PostgreSQL

Use certificate-validated TLS and approved private connectivity/proxy. Bound pools;
use explicit transactions/isolation. Test deadlocks, constraints, and idempotent retries.
Record indexes/query plans, migration locks, backup/PITR, and restoration tests.
Ignition direct Named Query R/W connections need scoped identities and server authorization.

## SQL Server (Optional)

Use approved supported JDBC/ODBC drivers with TLS certificate validation; never disable
verification to fix connectivity. Test parameter syntax, transactions/isolation,
identity handling, datetime precision, locking, retries, and migrations on SQL Server,
not merely PostgreSQL or SQLite.