# GUI-First Beginner Onboarding

2026-10-07: Reworked the project-user guide and 17-slide infographic for inexperienced
readers, not the template owner conducting a copy test. Added plain-English terms,
GitHub button and VS Code dialog routes, expected screens, GUI branching/staging/commits/
PRs, returning to work, and beginner troubleshooting. Template maintenance and technical
commands are in a separate optional owner/helper appendix. Re-exported the PDF.

Added seven explicit VS Code tasks using scripts/run_dev_check.sh: a combined action
plus environment/lint/format/types/tests/audit. They retain existing uv/venv tools,
do not fix files or deploy, and reject the wrong container/workspace/user. The combined
task runs sequentially in one results panel and stops on failure. No folder-open tasks,
frameworks, dependencies, deployment settings, or access-policy changes were introduced.

Updated root README, presentation notes, structure, and handover. Preserved unrelated
contributor formatting and prior presentation work. The guide's two plain-language
chat prompts match the slide wording with formatting indentation normalized.

Validation: the real combined runner completed all six checks, including 12 tests and
the locked dependency audit, with the expected final readiness message. Wrong-location
execution was rejected and shell lint passed. Task JSON/content consistency checks and
diagnostics passed. Browser checks covered all 17 slides at 1440/390/320px (51 layouts)
without content/footer or horizontal overflow, and logos loaded. A screenshot was inspected.

Real browser PDF export and container-side parsing verified 17 numbered 16:9 pages,
GUI routes and both prompts, and absence of obsolete copy-test/terminal instructions.
Fixed cover-page spacing without removing content. All 40 local links and seven task
references passed; final editor diagnostics reported no errors. Actual GUI task selection/
test discovery, a fresh GitHub project, agent sign-in, other-host rendering, and full
accessibility conformance remain unverified.

Deployment/recovery: no deployment or production mutation. Review/revert through a PR;
keep the guide/deck/PDF and task labels synchronized. Do not delete development volumes
as a recovery shortcut or bypass review/security policies for novice convenience.