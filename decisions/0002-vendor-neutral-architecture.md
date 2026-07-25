---
type: sdr
number: 2
scope: process
status: accepted
date: 2026-07-25
---
# 0002 — Vendor-neutral architecture: neutral core, thin per-tool adapters

## Context
The project must not be coupled to one AI vendor. Business logic
(rules, procedures, templates) should work with any capable agent tool;
Claude Code is simply the first adapter.

## Alternatives considered
- **CLAUDE.md as canonical** — rejected: Claude-specific dialect.
- **Skills under `.claude/skills/` as canonical** — rejected: vendor
  path; moved to root `skills/` with a symlink adapter.
- **Gitignoring `.claude/`** — rejected: the adapter must travel with
  the repo or fresh clones run unprotected; committing adapters is how
  enforcement is the default state.
- **A vendor-neutral enforcement file** — rejected: doesn't exist; each
  tool has its own config dialect. Neutral *declaration* + per-tool
  *implementation* instead.

## Decision
AGENTS.md is the canonical constitution (CLAUDE.md is a one-line
`@AGENTS.md` import). Procedures live in root `skills/` (open SKILL.md
format, tool-neutral bodies), discovered by Claude via the
`.claude/skills` symlink. The Access Policy is declared vendor-neutrally
in AGENTS.md; each tool implements it in a committed adapter, listed in
the policy's registry. Instructions avoid vendor dialect (no tool names,
no per-vendor features) outside adapter files.

## Consequences
Adopting a new tool = write its adapter (or use the read-only container),
add it to the registry. Enforcement strength varies by tool capability;
the detection layer (pre-commit hook) is the vendor-agnostic floor.
`tools/check-policy` drift lint deferred until a second adapter exists.
