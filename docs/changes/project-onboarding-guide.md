# First-Project User Guide

2026-10-07: Added docs/getting-started.md with numbered steps and pass checkpoints for
prerequisites, organization-owned GitHub template creation, cloning the new repository,
Dev Container/venv startup, quality checks, Claude Code or alternative agents, reopening,
and a first project-setup PR. Linked it from README and updated handover.

The guide distinguishes host versus container commands and published files versus local
changes. It does not claim Claude CLI, agent subscriptions, GitHub protections, a running
app, or production deployment are included. Skill read-file fallback and troubleshooting
allow users to report the first failure without relaxing standards or exposing secrets.

Validation: organization Git URL is reachable. Guide/configuration and required-step
checks passed; nine local document links resolve. Container checks confirmed /workspace,
UID 10001, Python 3.13.11, and /workspace/.venv. Lint/format, strict typing, all 12 tests,
and the locked dependency audit passed. Editor diagnostics reported no errors.

The user will test actual GitHub template creation, GUI reopening, agent sign-in,
reopening persistence, and project permissions; those actions have not been performed
for a new GitHub project by the agent. Template-repository status and remote CI are not
claimed verified. No new clone or organization repository was created during validation.

Deployment/rollback: documentation only. No commit, push, repository creation, settings
change, production connection, or deployment is executed. Revert the guide through a
reviewed PR if needed; preserve other contributors' presentation/documentation work.