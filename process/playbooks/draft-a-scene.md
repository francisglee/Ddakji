---
type: playbook
job: Draft a scene
modes: [solo]
skills: []
workflows: [scene-status]
---
## When
An outline slot exists and you're ready to write prose. Prose is solo
by constitution (DR-0001) — no AI in this loop.

## Steps
| Step | Actor | Action | Artifact |
|---|---|---|---|
| 1 | you | ensure the scene doc exists: copy [templates/scene-doc.md](../../templates/scene-doc.md) → `works/<work>/scenes/<slug>.md`; fill purpose & turns | scene spec |
| 2 | you | `tools/unlock`; copy [templates/draft.md](../../templates/draft.md) → `works/<work>/drafts/<slug>.md` | draft file |
| 3 | you | write prose above `<!-- END SCENE -->`; authorial notes in Evolution below | prose |
| 4 | you | `DRAFTS=1 git commit` with a `prose:` message; `tools/lock` | prose ledger entry |
| 5 | you | set scene doc `status: drafted` (respect the WIP limit, AGENTS rule 7) | status |

## Mode variants
Spec planning (step 1) may be collab — purpose/turns are legitimate AI
territory. Steps 2–4 are solo, always.
