# Baseline Template

2026-10-07: Generalized IoT-specific guidance into an organizational starter. Added
repo structure, container/venv rules, Python/database/Ignition/Terraform profiles,
per-PR documentation enforcement, and fail-closed deployment scaffolding.

Updated README, PRD, handover, standards, glossary, and deployment guidance. Production
changes require independent review/release approval and operational approval for control
effects. No application, resources, or credentials deployed.

Validation in the non-root container `.venv`: 12 tests passed, including real Git
diff fixtures and deployment refusal. Ruff lint/format, strict Pyright, locked
dependency audit, Compose validation/build, Terraform fmt/init/validate, and actionlint
passed. The source secret scan found no leaks. The patched development image passed
the fixable high/critical vulnerability gate. uv is 0.9.30 and CPython is 3.13.11.

Real Ignition/database/cloud/apply/deployment behavior remains unverified. GitHub CI
has not run remotely, branch/environment protections are not configured, and local
secret scanning covered files rather than history because this folder has no `.git`.
Deployment activation and adapters fail closed; no production workflow was executed.

Configure repository protections and project adapters before release. Source-template
changes can be reverted through a PR; infrastructure/data/control need separate recovery.