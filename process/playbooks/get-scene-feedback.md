---
type: playbook
job: Get feedback on a scene
modes: [turn-based, collab]
skills: [coverage]
workflows: [scene-status]
---
## When
A scene is `drafted` (developmental/line) or `revised` (copy/proof) and
you want a pass.

## Steps
| Step | Actor | Action | Artifact |
|---|---|---|---|
| 1 | you | confirm the pass is permitted for the status ([scene-status.toml](../workflows/scene-status.toml) feedback table) | — |
| 2 | you | invoke `/coverage <slug> [pass]` | invocation |
| 3 | AI | per [skills/coverage](../../skills/coverage/SKILL.md): report → `editorial/` | coverage report |
| 4 | you | read the report; apply mechanical fixes by hand (`unlock` → edit → `DRAFTS=1` `prose:` commit → `lock`) | prose |
| 5 | you | address developmental/line observations in revision; iterate 2–4 as needed | prose |
| 6 | you | advance `status:` when the pass is addressed | status |

## Mode variants
Turn-based: invoke with the slug, read the report later. Collab:
discuss findings live; the report still lands in `editorial/` (the
record survives the session).
