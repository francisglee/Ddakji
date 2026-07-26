---
type: readme
---
# process/ — the meta-project

How and why this project works. Book content never lives here.

## The layer model

Each statement lives in exactly one layer (the Layering Rule, AGENTS.md):

| Layer | Holds | Where |
|---|---|---|
| Why | values, ethics, role conduct — at depth | `principles.md`, `roles/` |
| What | binding rules, terse | `AGENTS.md` (repo root) |
| How | procedures & code | `skills/`, `tools/` |
| When | point-in-time decisions + rationale | `decisions/` (repo root) |
| State machines | enumerable workflows as data | `workflows/*.toml` |

Prose layers cite by reference and never restate. Diagrams
(`assets/generated/`) and lint are generated views of the workflow data.
Cross-layer changes flow through one DR (`scope: process`).

## Roles vs skills — conduct vs procedure

| Question | → `roles/<role>.md` | → `skills/<name>/SKILL.md` |
|---|---|---|
| What kind of statement? | ethic, axiom, standard — *who you are while working* | steps, inputs/outputs, guards — *how a task runs* |
| Holds regardless of task? | yes — binds across every activity of that role | no — scoped to one procedure |
| Violating it means… | mis*conduct* (doing wrong) | mal*practice* (doing the task wrong) |
| Changes when… | values evolve (rare, DR-worthy) | workflow evolves (often) |
| Referenced by | many skills, AGENTS.md, ambient reasoning | invoked explicitly, one task at a time |

The subtle case — an ethically-flavored *step* (e.g. "/interview:
consent block first"): the step lives in the skill (it's sequenced);
the principle it implements lives in the role. Skills cite roles, never
restate them: the skill says *when* the principle bites, the role says
*why* it always does. The same sentence appearing in both places is the
smell that the principle belongs up, the timing down.

## Interaction modes

How the human and AI share a workflow (DR-0013). Each playbook declares
which modes it supports:

| Mode | Shape | AI acts |
|---|---|---|
| `solo` | human-only work — prose is solo by constitution | not at all, or only on later request |
| `turn-based` | document-mediated: you edit files, then invoke with a pointer | only when invoked; responds by writing docs |
| `collab` | live session: intent stated, AI drives | continuously, inside approval gates |

Invocation rule: **AI acts only when invoked; an invocation carries a
pointer (turn-based) or an intent (collab).** Playbooks
(`playbooks/`) are the operator's manuals — human lane + handoffs only;
skills are the AI lane; workflows are the states. A workflow is done
when all three lanes exist.

## Contents

- `principles.md` — operating principles; source of the AI-disclosure statement
- `roles/` — professional ethic per agent dimension
- `workflows/` — scene status, idea/decision/canon lifecycles, publish pipeline (TOML)
- `automation.md` — map of what runs when, guarding what
- `playbooks/` — operator's manuals, one per human job-to-be-done
- `reading/` — annotated external materials on craft and AI authorship
- `backlog/` — open process questions, one entry per file (fed by retros)
- `retros/` — per-milestone retrospectives, scaffolded by `/release`
