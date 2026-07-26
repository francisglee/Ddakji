---
type: decision-record
number: 1
scope: process
kind: new
status: accepted
amended-by: 0007 (retrofit)
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0001 — Authorship boundary: all prose is human-written, mechanically enforced

**Description:** Human-only prose paths with layered enforcement;
editorial fixes delivered as suggestions, applied by the author's hand.

## Context
The project uses AI for research, worldbuilding, and editorial feedback,
but the book's text must be authored by Francis Lee — as an ethical
commitment, for authorial voice, and to preserve copyrightability under
human-authorship doctrine and support publisher AI-disclosure. Advisory
instructions alone depend on model compliance; the boundary needed to be
mechanical.

## Alternatives considered
- **Advisory-only rules in AGENTS.md** — rejected: follows in practice,
  guarantees nothing; the risk moment is a casual "tighten this up."
- **Per-edit approval prompts for mechanical fixes (Option B)** —
  rejected: removes the hard deny, admits AI keystrokes into the
  manuscript, weakens the provenance ledger.
- **Working-directory confinement** — rejected: cwd is a soft boundary;
  tools read/write by absolute path.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0001-1 | Human-only paths | `works/*/drafts/**`, `world/artifacts/texts/**`, `blog/drafts/**` — no agent writes by any means incl. shell | — |
| 0001-2 | Option A editorial delivery | Fixes as suggested diffs in `editorial/`; author applies by hand | — |
| 0001-3 | Layered enforcement | Deny adapters (hard) · read-only bits (kernel) · pre-commit `DRAFTS=1` signature + prose purity (detection) · git (recovery) | — |
| 0001-4 | New-tool gate | No tool runs here until its adapter or read-only container exists | — |

### Details

**0001-2.** Every character in prose paths is physically typed by the
author — the ethical position and the human-authorship evidence are the
same fact. Draft files are created by the author from
`templates/draft.md`, never scaffolded by agents.

## Consequences
Prose commits form a clean human-authorship ledger. Scene metadata had
to move out of prose files so agents could maintain it → the scene
spec/prose split (DR-0003).

## Affected Files
| File | Changes Made | Decision ID | Commit ID |
|---|---|---|---|
| [.claude/settings.json](../.claude/settings.json) | deny rules for the three prose paths | 0001-1 | a079fc1 |
| [.githooks/pre-commit](../.githooks/pre-commit) | DRAFTS=1 signature + prose-commit purity | 0001-3 | a079fc1 |
| [AGENTS.md](../AGENTS.md) | Access Policy, enforcement ladder, new-tool gate | 0001-1, 3, 4 | a079fc1 |
| [tools/lock](../tools/lock), [tools/unlock](../tools/unlock) | kernel-level read-only bits | 0001-3 | 793fb35 |
| [templates/draft.md](../templates/draft.md) | author-copied prose template | 0001-2 | cb9de32 |
