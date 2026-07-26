---
type: decision-record
number: 13
scope: process
kind: new
status: accepted
date-created: 2026-07-26
last-updated: 2026-07-26
---
# 0013 — Add human playbooks & interaction modes

**Description:** Operator's manuals — one playbook per human
job-to-be-done as a swimlane table owning the human lane and handoff
points; a three-mode interaction vocabulary (solo / turn-based /
collab); the invocation rule for when AI responds.

## Context
All procedural documentation is written for the AI as executor
(skills) or as state data (workflows). Nothing documents workflows from
the human's chair: which template to copy where, which docs to edit,
and at what point the AI responds. The author works in two distinct
styles — document-mediated turns and live collab sessions — and prose
drafting is a third, human-only style the system must describe
honestly.

## Alternatives considered
- **Two modes (turn-based, collab)** — rejected: prose drafting is
  solo *by constitution* (DR-0001); a playbook pretending AI is always
  in the loop would misdescribe the most important workflow.
- **Human guidance inside SKILL.md files** — rejected: audience mixing;
  skills are the AI lane. Two audiences, two docs, zero shared
  sentences.
- **Playbooks 1:1 with skills** — rejected: human jobs span skills
  ("ship a version" = /release + /publish + retro); playbooks organize
  by job-to-be-done, skills by procedure.
- **Modes documented per-playbook only** — rejected: modes are a
  cross-cutting concept; defined once in `process/README.md`, declared
  per-playbook.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0013-1 | Playbook entity | `process/playbooks/<job>.md`, template `playbook.md`: trigger, `modes:` declared, swimlane table (Step \| Actor \| Action \| Artifact), mode variants where handoffs differ | — |
| 0013-2 | Interaction modes | `solo` (human only; AI absent or on-request) · `turn-based` (document-mediated: human edits, invokes with a pointer; AI responds in docs) · `collab` (live session: intent given, AI drives, approval gates). Defined once in `process/README.md` | — |
| 0013-3 | Three-lane rule | Workflow TOML = states · skill = AI lane · playbook = human lane + handoffs. Playbooks cite skills/workflows/rules, never restate — a restated step is the drift smell | — |
| 0013-4 | Invocation rule | AI acts only when invoked; an invocation carries a pointer (turn-based) or an intent (collab). This is the general answer to "when does AI respond" | — |
| 0013-5 | Initial roster | Seven playbooks by job: draft-a-scene (solo), get-scene-feedback, explore-to-canon, capture-research, conduct-interview, record-a-decision, ship-a-version | — |

## Consequences
- `templates/playbook.md` and `process/playbooks/` (seven files) added;
  `playbook` joins the AGENTS.md schema key-types list.
- `process/README.md` gains an Interaction modes section beside the
  layer model, and the contents list gains playbooks.
- **Definition-of-done for workflows**: a workflow ships when all three
  lanes exist — states (TOML), AI lane (skill), human lane (playbook).
  Enforced where it can be: playbooks join the layer enumeration in
  `skills/decision/SKILL.md` (the Layering Rule change-set step), so DR
  drafting itself checks the lane is present. Writing the human lane is
  also the workflow's usability test — a playbook that's hard to write
  is a workflow that's badly designed, caught at draft time.

## Affected Files
| File | Changes Made | Decision ID | Author | Commit ID |
|---|---|---|---|---|
| [templates/playbook.md](../templates/playbook.md) | new template | 0013-1 | claude-fable-5 | *pending* |
| [process/playbooks/](../process/playbooks/) | seven playbooks per roster | 0013-1, 0013-5 | claude-fable-5 | *pending* |
| [process/README.md](../process/README.md) | Interaction modes section; contents line | 0013-2 | claude-fable-5 | *pending* |
| [AGENTS.md](../AGENTS.md) | `playbook` in schema key-types list | 0013-1 | claude-fable-5 | *pending* |
| [skills/decision/SKILL.md](../skills/decision/SKILL.md) | playbooks join the layer enumeration in the change-set step | 0013-1 | claude-fable-5 | *pending* |
