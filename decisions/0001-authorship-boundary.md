---
type: sdr
number: 1
scope: process
status: accepted
date: 2026-07-25
---
# 0001 — Authorship boundary: all prose is human-written, mechanically enforced

## Context
The project uses AI for research, worldbuilding, and editorial feedback,
but the book's text must be authored by Francis Lee — as an ethical
commitment, for authorial voice, and (recognized later in the discussion)
to preserve copyrightability under human-authorship doctrine and to
support publisher AI-disclosure. Advisory instructions alone
(AGENTS.md-style) depend on model compliance; the boundary needed to be
mechanical.

## Alternatives considered
- **Advisory-only rules in AGENTS.md** — rejected: follows in practice,
  guarantees nothing; the risk moment is a casual "tighten this up."
- **Per-edit approval prompts for mechanical fixes (Option B)** —
  rejected: removes the hard deny, admits AI keystrokes into the
  manuscript, weakens the provenance ledger.
- **Working-directory confinement** — rejected: cwd is a soft boundary;
  tools read/write by absolute path.

## Decision
Human-only paths: `works/*/drafts/**`, `world/artifacts/texts/**`,
`blog/drafts/**`. No agent writes there by any means, including shell.
Editorial fixes are delivered as suggested diffs in `editorial/`; the
author applies them by hand (Option A). Enforcement is layered:
per-tool deny adapters (hard), read-only file bits via `tools/lock`
(cheap, kernel-level), pre-commit hook with `DRAFTS=1` author signature
and prose-commit purity (detection), git history (recovery). New tools
require an adapter or read-only container before running here.

## Consequences
Prose commits form a clean human-authorship ledger. Scene metadata had
to move out of prose files so agents could maintain it → led to the
scene spec/prose split (0003). Draft files are created by the author
from `templates/draft.md`, never scaffolded by agents.
