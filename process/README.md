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

## Contents

- `principles.md` — operating principles; source of the AI-disclosure statement
- `roles/` — professional ethic per agent dimension
- `workflows/` — scene status, idea lifecycle, publish pipeline (TOML)
- `automation.md` — map of what runs when, guarding what
- `reading/` — annotated external materials on craft and AI authorship
- `backlog.md` — open process questions (fed by retros)
- `retros/` — per-milestone retrospectives, scaffolded by `/release`
