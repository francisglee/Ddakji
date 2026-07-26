---
type: decision-record
number: 2
scope: process
kind: new
status: accepted
amended-by: 0007 (retrofit)
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0002 — Vendor-neutral architecture: neutral core, thin per-tool adapters

**Description:** All business logic in vendor-neutral locations;
AGENTS.md canonical; per-tool enforcement adapters committed with the
repo.

## Context
The project must not be coupled to one AI vendor. Business logic
(rules, procedures, templates) should work with any capable agent tool;
Claude Code is simply the first adapter.

## Alternatives considered
- **CLAUDE.md as canonical** — rejected: Claude-specific dialect.
- **Skills under `.claude/skills/` as canonical** — rejected: vendor
  path; root `skills/` with a symlink adapter instead.
- **Gitignoring `.claude/`** — rejected: the adapter must travel with
  the repo or fresh clones run unprotected.
- **A vendor-neutral enforcement file** — rejected: doesn't exist; each
  tool has its own config dialect. Neutral *declaration* + per-tool
  *implementation* instead.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0002-1 | AGENTS.md canonical | Constitution is vendor-neutral; CLAUDE.md is a one-line `@AGENTS.md` import | — |
| 0002-2 | Skills at root | `skills/` canonical (open SKILL.md format, tool-neutral bodies); `.claude/skills` symlink for discovery | — |
| 0002-3 | Policy declared neutrally | Access Policy in AGENTS.md; adapter registry lists per-tool implementations | — |
| 0002-4 | Adapters committed | Enforcement is the repo's default state, not a setup step | — |

## Consequences
Adopting a new tool = write its adapter (or use the read-only
container), add it to the registry. Enforcement strength varies by tool
capability; the detection layer (pre-commit hook) is the
vendor-agnostic floor. `tools/check-policy` drift lint deferred until a
second adapter exists.

## Affected Files
| File | Changes Made | Decision ID | Commit ID |
|---|---|---|---|
| [AGENTS.md](../AGENTS.md) | canonical constitution, Access Policy + registry | 0002-1, 0002-3 | a079fc1 |
| [CLAUDE.md](../CLAUDE.md) | one-line importer + Claude-only notes | 0002-1 | a079fc1 |
| [.claude/settings.json](../.claude/settings.json) | first committed adapter | 0002-3, 0002-4 | a079fc1 |
| [skills/](../skills/) + `.claude/skills` symlink | root-canonical skills, discovery adapter | 0002-2 | 793fb35 |
