---
type: playbook
job: Capture freely
modes: [solo, turn-based]
skills: [mine]
workflows: [idea-lifecycle]
---
## When
Something's in your head — an idea, a doubt, a fragment, a connection —
and deciding where it belongs would cost more than writing it down.

## Steps
| Step | Actor | Action | Artifact |
|---|---|---|---|
| 1 | you | copy [templates/journal-entry.md](../../templates/journal-entry.md) → `journal/entries/YYYY-MM-DD-slug.md`; write freely | entry |
| 2 | you | `DRAFTS=1 git commit` (`prose:`) — the idea-provenance ledger | ledger entry |
| 3 | you | whenever ready (batching is fine): invoke `/mine` | invocation |
| 4 | AI | per [skills/mine](../../skills/mine/SKILL.md): route ideas to backlogs/seeds, report → `journal/mined/` | report + entries |
| 5 | you | read the report; decide the "Needs your call" items | decisions |

## Mode variants
Solo is complete at step 2 — mining is optional and can lag capture by
days. In collab, this playbook dissolves: speaking to the AI *is* the
capture, and routing happens live.
