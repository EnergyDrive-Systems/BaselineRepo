# Skills

`grill-with-docs` is the existing upstream wrapper tracked in `skills-lock.json`,
from mattpocock/skills. All other skills here are organization-maintained workflows,
not claimed to be hash-locked upstream copies. They translate the baseline's standards
into procedures; no archive skill bundle was installed. Git commits pin reviewed local
versions once the repository is initialized and committed by an authorized contributor.

## Workflow Index

| Skill | Use For |
| --- | --- |
| `grill-with-docs` | Requirements/design interview with terminology capture |
| `grilling` | Question rounds, recommendations, and shared understanding |
| `domain-modeling` | Agreed glossary terms and consequential decisions |
| `code-review` | Separate standards and requirements reviews |
| `diagnosing-bugs` | Reproduction, root cause, regression, and cleanup evidence |
| `implement-and-verify` | Small agreed changes, focused validation, and documentation |
| `release-readiness` | Artifact/runtime evidence, recovery, and handover assessment |
| `ignition-perspective` | Perspective resource changes and real gateway acceptance |
| `database-change-review` | SQL/data contracts, migrations, parity, and query costs |
| `terraform-change-review` | Configuration/sanitized plan, drift, replacement, and ownership review |

Use only the skills relevant to the task and active profiles; do not load all ten for
every change. Each new skill names prerequisites, workflow, and completion evidence.
Paths in skill bodies are repository-relative. Read referenced standards as the source
of policy rather than treating a workflow summary as an independent exception.

## Invocation And Maintenance

Review licensing, code, tool permissions, and dependencies before updates. No automatic
upstream skill updates. Skill text cannot override access/approval policies.

Verify `.agents/skills/` discovery for installed Claude Code, Codex, and Copilot versions.
Register directories through client-supported configuration if needed; avoid divergent
copies. Root `AGENTS.md` gives a read-file fallback when no Skill tool is available.
Claude imports shared rules from `CLAUDE.md`, Codex uses `AGENTS.md`, and Copilot has
its `.github/` entry point. Verify discovery during onboarding.

Invoke a named skill when supported, or read `.agents/skills/<name>/SKILL.md` and follow
it directly. Load dependencies individually. Do not assume every client supports the
same tool names, background agents, or slash commands. Delegate only when the current
client and task instructions permit it. Skills guide behavior, not deterministic
permission enforcement, human approvals, or proof of runtime correctness.