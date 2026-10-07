# Baseline Workflow Skills

2026-10-07: Added seven organization-maintained skills: code-review, diagnosing-bugs,
implement-and-verify, release-readiness, ignition-perspective, database-change-review,
and terraform-change-review. Retained the existing requirements/domain-modeling skills.

Updated the skill index, root agent routing, README map, and handover. Skills reference
existing standards/profiles and name triggers, prerequisites, workflows, and completion
evidence. No upstream bundle, client-specific hooks, dependencies, or execution tools
were installed. Existing access rules and production restrictions are unchanged.

Validation: a real YAML parser in the existing container `.venv` checked metadata,
name/directory matches, workflow sections, repository references, and index/routing
coverage for all seven skills; 94 assertions passed. Editor diagnostics are checked
separately. Actual discovery/invocation in all three clients and real runtime behavior
remain unverified; skills are guidance, not CI gates or deployment approval.

Deployment/rollback: none executed. Skill changes can be reverted through a reviewed
PR. No Python implementation, workflow code, infrastructure, or production data changed.