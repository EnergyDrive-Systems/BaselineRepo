# Material 3 UI Standard

2026-10-07: Established Material Design 3 principles as the default for all new and
changed UIs. Added one shared UI profile and wired it into root agent guidance,
implementation/review/Perspective skills, the Ignition profile, PR evidence, README,
and handover. No additional skill or frontend framework was installed.

The profile covers shared semantic tokens, component states, adaptive layouts,
EnergyDrive branding, accessibility, task-flow verification, and SCADA human factors.
It distinguishes Material 3 principles from library/platform capabilities and requires
actual runtime evidence without claiming that a visual theme guarantees good UX.

Validation: 31 required-content/routing checks passed, the brand reference exists, and
the Security section matches the committed baseline (normalizing line endings). A YAML
parser in the container `.venv` validated the three edited skills' metadata and references.
Editor diagnostics reported no errors. No UI application, gateway, visual/accessibility
runtime suite, or CI conformance gate is implemented or certified by this change.

Deployment/rollback: guidance only; no deployment or production mutation. Exceptions
follow existing owner-review rules. Revert policy wording through a reviewed PR if needed;
do not use this addition to redesign unrelated screens or erase contributor changes.