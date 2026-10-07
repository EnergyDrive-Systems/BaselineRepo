# Terraform Profile

Use Terraform for managed infrastructure changes in the pinned tooling container.
The included root constrains the version and provisions nothing.

Define configuration ownership per resource/field: Terraform owns infrastructure,
while the release pipeline owns application artifact promotion. Where both touch the
same service, document the boundary and intentional lifecycle exclusions, then test
that a plan after release does not revert the deployed artifact. Do not use broad
`ignore_changes` rules to conceal drift; all remaining fields stay subject to review.

- Separate environment roots, state, and identities. CLI workspaces alone are not a
  sufficient production boundary.
- Before real resources, configure approved encrypted remote state, access control,
  versioning, audit, and backend-supported locking. Backend bootstrap needs its own
  approved process. Do not manage production from untracked local state.
- Pin provider constraints and module versions; commit `.terraform.lock.hcl` per root.
  No speculative providers/resources. Match tooling versions/digests for plan/apply.
- PR CI runs formatting and credential-free validation. Real plans run only in trusted
  restricted workflows with short-lived identities. Plans/state may contain secrets;
  store encrypted with limited access/retention, never in Git or ordinary PR artifacts.
  Marking a value sensitive does not remove it from state.
- Approve the exact saved plan and source commit; apply that plan, not an unreviewed
  replacement. Protect environments/locks, serialize changes, and inspect drift.
- Document costs, region, ownership labels, IAM/network scope, database deletion
  protection, recovery, replacement risks, and reversibility. No automatic destroy,
  broad permissions, or password resets.
- Add provider-aware security/policy checks for actual resources before enabling IaC
  deployment. Never give the dev Compose service production credentials.

Real plan/apply adapters are intentionally absent pending reviewed project configuration.