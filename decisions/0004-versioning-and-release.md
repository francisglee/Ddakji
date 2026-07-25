---
type: sdr
number: 4
scope: process
status: accepted
date: 2026-07-25
---
# 0004 — Versioning & release: semver per work, stable slugs, generated archives

## Context
The author wanted software-style versioning and browsable draft history
("draft two") without hand-maintained version copies that drift from
git.

## Alternatives considered
- **Per-scene version numbers / version-suffixed filenames** — rejected:
  duplicates git, churns every reference key, creates "which is
  current?" ambiguity.
- **Hand-maintained snapshot copies** — rejected: drift.
- **Two decision logs (process vs story)** — rejected: two numbering
  sequences make SDR references ambiguous; `scope:` frontmatter is the
  separation (taxonomy in metadata).

## Decision
- Semver attaches to **works**, not scenes: MAJOR structural break ·
  MINOR new/rewritten scenes · PATCH line fixes. Tags `<work>/vX.Y.Z`.
  `1.0.0` = submission-ready.
- Working drafts keep stable slug names; `/release` snapshots drafts
  into `works/<work>/archive/vX.Y.Z/` (generated, browsable) alongside
  changelog entry, tag, and retro scaffold.
- Scene *maturity* is a status field (`scene-status.toml`); scene
  *history* is git; scene *rationale* is SDRs.
- One decision log, one sequence, `scope:` field.
- Commit taxonomy: every message starts `governance:` `process:`
  `machinery:` `world:` `works:` or `prose:`; `prose:` commits are pure
  and DRAFTS=1-signed (hook-enforced) — the human-authorship ledger.

## Consequences
`main` always releasable; branches only for experiments and risky
tooling/enforcement changes. CHANGELOG per work records *what* shipped;
SDRs record *why*; retros record *how it went*.
