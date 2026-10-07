# Ignition Perspective Profile

Initial target: **Ignition 8.3.10**, vendor stable release verified on 2026-10-07.
Record gateway, Perspective, Designer, and third-party module versions in PRD;
Designer Launcher versions do not identify the gateway runtime. Review upgrades.

UI work must also follow `docs/profiles/ui.md`: Material Design 3 is the default for
Perspective views and interactions. Adapt it through native components, shared style
classes, reusable views, and supported theme tokens. Verify platform limitations on the
gateway/browser; visual styling does not replace alarm semantics or operational safeguards.

- Dev/test gateways are containerized, with persistent volumes, approved licensing,
  runtime secrets, local-only access, and no production device connections. Pin the
  vendor image digest; never use floating `latest`.
- Designer is a desktop exception. Gateway scripts use embedded Jython/Python
  2.7-compatible syntax/runtime, not the CPython `.venv`, modern Python packages,
  or the standalone Ruff/Pyright profile.
- Prefer bindings, Named Queries, tags, UDTs, alarms, pipelines, and security levels
  over custom implementations. Keep event scripts thin; reuse project libraries.
  Avoid blocking database/network operations in UI execution paths.
- Version resources under `ignition/`. Reconcile/export Designer changes before PR;
  import into a clean matching gateway and round-trip export to detect missing resources.
  Preserve required Ignition resource metadata.
- Separate projects, tags/UDTs, and gateway configuration deliverables. Document import
  order, dependencies, providers, alarms, and post-import enabled states. Tag import
  must not silently disable scheduled query execution.
- Use managed JDBC connections and parameterized Named Queries for approved direct
  PostgreSQL/SQL Server R/W. Enforce authorization server-side, not by hiding controls.
- Prefer Python services for complex BigQuery logic/ingestion. Direct access requires
  an approved connector, auth, cost controls, and validated write semantics; JDBC alone
  does not make BigQuery a transactional database.
- Separate monitoring/control. Validate authority, freshness, ranges, confirmation,
  interlocks, and audit trails. Application checks do not replace safety-rated systems.
- Document cache lifetime and invalidation/versioning when global state survives saves.
  Test stale data, restart, session isolation, and failure behavior.

## Alarm Behavior

Distinguish upstream source-health failures from individual device-health failures;
missing/stale data must not automatically mean a healthy device or a device outage.
Document quality/freshness thresholds, active/clear delays, deadbands, priority, and
recovery behavior. Test flapping, source loss/recovery, restart, and post-import states.

Specify escalation timing, acknowledgement versus clear behavior, cancellation of
pending notifications, and recovery-message deduplication. Define journal retention,
notification-failure visibility, and operational ownership per project. Assess derived
alarm suppression for risk; retain a visible source-health alarm and never suppress
safety-relevant conditions merely to reduce notification volume.

Gateway acceptance covers Perspective desktop/mobile, security, Named Queries, tag
quality, alarms, write denial/approval, restarts, and persistence. Record real runtime
evidence; CPython tests alone are not sufficient.

Production containers require tested backup/restore, persistence, licensing recovery,
availability, network boundaries, and site approval. Source rollback may not reverse
equipment actions or database mutations. Add project-specific Compose gateway settings
only after secret, licensing, and network requirements are defined.

Source: https://inductiveautomation.com/downloads/ignition

Verified vendor container reference (not started by this template):
`inductiveautomation/ignition:8.3.10@sha256:174fb4d8c640a6439baec35540bdf15169f850f6f849a1ae80dcb91bbe66b119`.
Verify the vendor's secret/licensing and persistence configuration when adding the
project's gateway service. Never commit an initial administrator password.