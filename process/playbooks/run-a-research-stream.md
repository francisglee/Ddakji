---
type: playbook
job: Run a research stream
modes: [turn-based, collab]
skills: [research]
workflows: []
---
## When
A territory needs sustained, multi-note research rather than one
answer — a period, a population, a sector — and you want to know what
is covered, what is thin, and what is still outsider framing. One-off
questions use [capture-research](capture-research.md) instead.

## Steps
| Step | Actor | Action | Artifact |
|---|---|---|---|
| 1 | you | copy [templates/research-stream.md](../../templates/research-stream.md) → `research/streams/<slug>.md`; write the questions; register it in `research/README.md` Streams | stream |
| 2 | AI | propose the period × lens (or wave × lens) cells that matter and why; you strike or add | coverage intent |
| 3 | you | pick a cell; invoke `/research <question>` naming the stream | invocation |
| 4 | AI | per [skills/research](../../skills/research/SKILL.md): note tagged `streams:`, `periods:`, `lenses:`, with Method and full References | note |
| 5 | you | **read the sources the note cites** before accepting; check for stereotype, over-generalization, outsider framing; challenge single-lens claims | reviewed note |
| 6 | AI | update the stream's Gaps; file open questions to `research/backlog/` | gaps, entries |
| 7 | you | repeat 3–6 per cell; findings that should bind go to `world/backlog/` (canon enters only via DR) | backlog entries |
| 8 | you | on a cadence (near-future material moves fast): `/research review <slug>` per [capture-research](capture-research.md) step 4; mark the stream `dormant` or `closed` when its questions are answered | curated notes |

## Mode variants
Turn-based is the default: you queue cells, the AI files notes, you
review in batches. In collab, steps 2–6 happen live in one session.
Step 5 is never skipped in either mode — a stream whose notes are not
read by the author fails the effort test (DR-0016, principles §7):
research is half the point, not overhead.
