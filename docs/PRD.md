# Project Requirements

## Identity And Profiles

Complete before implementation: name, product/technical owners, independent reviewer,
release approver, operational approver, and support contact. Select active profiles:
Python / Perspective / BigQuery / PostgreSQL / SQL Server / Terraform. Inactive
profiles remain reference material, not unused dependencies.

## Runtime And Data Contracts

Record approved image digests, Python patch, Ignition gateway/modules/Designer,
Terraform/providers, deployment targets, and environment boundaries. Specify schemas,
units, timestamps, freshness, retention, expected volumes, identities, query budgets,
and privacy/access constraints. No secrets.

## Write Classification

For each operation record destination, authorization, validation, idempotency, audit,
and effect. Identify equipment-affecting data writes and operational approval/interlocks
separately from ordinary business-data writes.

## Scope

| Requirement | Acceptance Evidence | Status |
| --- | --- | --- |
| Define project-specific requirements | Approved contracts and acceptance tests | Next |

Use Done, Blocked, Next, Later. Define performance, availability, recovery objectives,
failure cases, and explicit exclusions. Link diagrams and ADRs only when they exist.

## Delivery

Specify artifacts, deployment adapters, approval roles, integration/gateway acceptance,
backup/restore evidence, rollback limits, and costs. Update in the same PR as behavior
or requirements changes. Record consequential decisions in ADRs with dates/owners.