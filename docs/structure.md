# Repository Structure

Keep the root for navigation, shared policy, and tool configuration. Do not add empty
trees, `misc/`, duplicate standards, or application frameworks before they are needed.

| Path | Content |
| --- | --- |
| `src/<package>/` | Standalone Python logic and adapters; thin transport boundaries |
| `tests/` | Unit tests; add `integration/` when real integration tests exist |
| `ignition/projects/<project>/` | Sanitized, reviewable Designer/gateway project resources |
| `ignition/tags/` | Reviewed tags/UDTs without secrets |
| `sql/bigquery/`, `sql/postgres/`, `sql/mssql/` | Queries for selected dialects only |
| `sql/<dialect>/objects/` | Authoritative current definitions, one file per managed SQL object |
| `sql/<dialect>/migrations/` | Ordered immutable migrations when needed |
| `infra/terraform/modules/<name>/` | Components with demonstrated reuse |
| `infra/terraform/environments/<name>/` | Independent environment roots/state boundaries |
| `scripts/` | Repository automation, not business logic |
| `assets/brand/` | Reusable company artwork and provenance/usage notes, not project exports |
| `docs/` | Requirements, standards, handover, release guidance, diagrams, decisions |
| `docs/changes/` | One descriptive record per PR |
| `docs/presentations/` | Stakeholder decks, their editable sources, and generated PDF documentation |
| `.github/` | CI/CD, ownership, contributor entry points |
| `.devcontainer/` | Container attachment, lifecycle initialization, and container editor settings |
| `.vscode/` | Minimal shared editor recommendations; no project-specific auto-start tasks |
| `.agents/skills/` | Reviewed agent workflows |

One service uses the root Python configuration and Dockerfile development/runtime
targets. Introduce `services/<name>/` only for independently deployed workloads; each
then owns dependencies, tests, image, and lockfile. Avoid premature monorepo tooling.
Separate repositories share the standards but activate fewer profiles.

Use descriptive lowercase directory names and snake_case Python modules. Preserve
standard uppercase agent/PRD/handover/glossary filenames. No source version-number
directories. Releases use tags and immutable registry artifacts, not overwritten Git
binary files. Record checksums, source commit, and release notes.

Keep sensitive gateway backups/datasets outside Git. Never blanket-ignore Ignition
source. Document export/import round trips. New paths require a README map update.

When an architecture diagram is needed, keep one editable Mermaid source in
`docs/arch/architecture.mmd`. Update it in the same PR as changed boundaries/data flows.
Use Git history for versions; rendered previews may be CI artifacts. Do not add committed
per-PR snapshots or a workflow that rewrites contributor branches. Create the diagram
only when there is real architecture to describe.

Generated SQL bundles belong in release artifacts; if a project needs a committed
bundle, clearly mark it generated and require a freshness check. Keep source definitions
and migration history distinct as described in the database profile.