---
type: decision-record
number: 4
scope: process
kind: new
status: accepted
amended-by: 0007 (0007-7, retrofit)
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0004 — Versioning & release: semver per work, stable slugs, generated archives

**Description:** Software-style versioning adapted to fiction — semver
on works, git as history, generated draft archives, one decision log,
categorized commits.

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
  sequences make record references ambiguous; `scope:` frontmatter is
  the separation (taxonomy in metadata).

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0004-1 | Semver per work | MAJOR structural break · MINOR new/rewritten scenes · PATCH line fixes; tags `<work>/vX.Y.Z`; 1.0.0 = submission-ready | — |
| 0004-2 | Stable slugs + generated archives | Working drafts keep stable names; `/release` snapshots to `archive/vX.Y.Z/` | — |
| 0004-3 | Three separations | Scene maturity = status field; history = git; rationale = decision records | — |
| 0004-4 | One decision log | Single sequence; `scope:` field separates domains | — |
| 0004-5 | Commit taxonomy | Categorized commit prefixes; `prose:` commits pure and DRAFTS=1-signed — the human-authorship ledger. *Category `machinery:` renamed `infrastructure:` by 0007-7.* | — |

## Consequences
`main` always releasable; branches only for experiments and risky
tooling/enforcement changes. CHANGELOG per work records *what* shipped;
decision records the *why*; retros the *how it went*.

## Affected Files
| File | Changes Made | Decision ID | Commit ID |
|---|---|---|---|
| [AGENTS.md](../AGENTS.md) | semver rule, conventions, commit taxonomy | 0004-1, 3 – 5 | a079fc1 |
| [skills/release/SKILL.md](../skills/release/SKILL.md) | changelog, tag, archive snapshot procedure | 0004-1, 0004-2 | 793fb35 |
| [works/baek-il/CHANGELOG.md](../works/baek-il/CHANGELOG.md), [ROADMAP.md](../works/baek-il/ROADMAP.md) (both works) | per-work version artifacts | 0004-1 | 6e0aecf |
