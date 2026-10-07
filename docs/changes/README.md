# PR Change Records

Every PR adds/updates its own `docs/changes/<descriptive-name>.md` plus an affected
project document. Use lowercase hyphenated filenames; do not reuse another PR's record.
CI enforces paths; human reviewers enforce relevance and meaningful content.

Include change/reason, requirements/security/control effects, updated docs, actual
checks/results, unverified real-runtime behavior, deployment/rollback impact, and any
approved exception. Maintenance and docs-only PRs still need a record. PR numbers are
not required because the branch may precede the PR.