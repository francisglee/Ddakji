---
type: playbook
job: Conduct an interview
modes: [solo, turn-based]
skills: [interview]
workflows: []
---
## When
Someone's lived experience should inform the story (coverage targets:
[research/README](../../research/README.md)).

## Steps
| Step | Actor | Action | Artifact |
|---|---|---|---|
| 1 | AI | on `/interview prep <topic>`: question areas + consent items to raise | prep notes |
| 2 | you | **conduct the interview** (solo, real world); secure consent explicitly | recording / notes |
| 3 | you | park raw material (large recordings outside the repo, linked) | raw material |
| 4 | AI | on `/interview process`: per [skills/interview](../../skills/interview/SKILL.md) — doc with consent block first | interview doc |
| 5 | you | **verify the consent block yourself** — you are its guarantor, not the AI | consent |
| 6 | AI | follow-ups → `research/backlog/`; cross-link `informs:` | entries |

## Mode variants
The interview itself is always solo-human. Prep and processing are
turn-based; collab works for prep when planning question areas
together.
