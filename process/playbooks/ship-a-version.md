---
type: playbook
job: Ship a version
modes: [collab]
skills: [release, publish]
workflows: [publish-pipeline, scene-status]
---
## When
A roadmap milestone is reached (semver mapping: AGENTS rule 6) — and
optionally content goes public.

## Steps
| Step | Actor | Action | Artifact |
|---|---|---|---|
| 1 | you | judge the milestone reached; call the version | intent |
| 2 | AI | on `/release <work> <vX.Y.Z>`: per [skills/release](../../skills/release/SKILL.md) — changelog, tag, archive snapshot, retro scaffold | release |
| 3 | you | fill the retro (`process/retros/`); actions → `process/backlog/` | retro |
| 4 | you | (if publishing) invoke `/publish <target>` | invocation |
| 5 | AI | per [skills/publish](../../skills/publish/SKILL.md): walk every check in [publish-pipeline.toml](../workflows/publish-pipeline.toml); run exporter; **stop at the diff** | export + checks |
| 6 | you | review the publish diff — this is the irreversible-in-rights-terms moment | approval |
| 7 | AI | commit; published content is now canon (errata-only changes) | public content |

## Mode variants
Collab only — releasing and publishing are multi-step with approval
gates; don't run them half-attended.
