---
type: playbook
job: Record a decision
modes: [collab, turn-based]
skills: [decision]
workflows: [decision-lifecycle]
---
## When
A discussion has produced an independently reversible decision — or a
backlog entry is ripe for deciding.

## Steps
| Step | Actor | Action | Artifact |
|---|---|---|---|
| 1 | you | raise the decision (live discussion, or point at `<domain>#NNNN`) | intent |
| 2 | AI | on `/decision`: per [skills/decision](../../skills/decision/SKILL.md) — draft in the working tree; `decisions/` holds no drafts | DR draft |
| 3 | you | review; iterate — drafts are cheap, records are immutable | edits |
| 4 | you | **approve explicitly** — commit = acceptance, nothing lands before your word | approval |
| 5 | AI | implement the change set (all affected layers), commit citing `DR-NNNN` | landing |
| 6 | AI | close out: fill Commit ID cells | closed record |
| 7 | you | spot-check the Affected Files table against the diff | verification |

## Mode variants
Turn-based: leave draft feedback as file edits or margin notes; the AI
picks them up on next invocation. The approval gate (step 4) is
identical in every mode.
