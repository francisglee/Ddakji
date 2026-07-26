---
type: playbook
job: Capture research
modes: [turn-based, collab]
skills: [research]
workflows: []
---
## When
A question needs verifiable grounding — history, present reality,
near-future trajectories.

## Steps
| Step | Actor | Action | Artifact |
|---|---|---|---|
| 1 | you | state the question (collab) or file a `research/backlog/` entry (turn-based) | intent / entry |
| 2 | AI | on `/research <question>`: per [skills/research](../../skills/research/SKILL.md) — sourced note → `research/notes/` | note |
| 3 | you | review; adjust `subjects:`, challenge claims, accept | note |
| 4 | you | later, when reality may have moved: invoke `/research review <slug>` | invocation |
| 5 | AI | re-verify, adjust `status:`, stamp `last-reviewed` | curated note |

## Mode variants
Solo capture is legal too: draft a note yourself from the template; AI
verification is then a later turn-based pass.
