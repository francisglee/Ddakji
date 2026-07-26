---
type: playbook
job: Explore a territory into canon
modes: [turn-based, collab]
skills: [explore, decision]
workflows: [canon-lifecycle]
---
## When
A thematic or worldbuilding territory needs thinking before the
universe commits to a position.

## Steps
| Step | Actor | Action | Artifact |
|---|---|---|---|
| 1 | you | copy [templates/exploration.md](../../templates/exploration.md) → `research/explorations/<slug>.md`; fill topic, `explores:` | exploration doc |
| 2 | you | seed Dimensions with first thoughts (turn-based) or state the territory (collab) | edits |
| 3 | AI | on `/explore <slug>`: per [skills/explore](../../skills/explore/SKILL.md) — dimensions, multi-sided theses | edits |
| 4 | you | react in Notes; iterate 2↔3 until the territory feels mapped | edits |
| 5 | you | **distill**: copy the entity template (e.g. [theme.md](../../templates/theme.md)) → `world/…`, choose champions, cite `explorations:` | proposed entity |
| 6 | AI | backfill the exploration's `informs:`; on request `/decision` drafts the canonization DR — Alternatives must engage unchampioned theses (DR-0010) | DR draft |
| 7 | you | review, iterate, approve → lands and closes out | canon |

## Mode variants
Turn-based: steps 2–4 happen across sessions via file edits +
invocations. Collab: 2–4 compress into live dialogue; distillation
(step 5) is yours in every mode — the AI never initiates it.
