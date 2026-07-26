# Contributing — how this book is made

The contribution model per domain (DR-0009). This is a map: every cell
links to the governing rule; nothing is restated here. Changes to this
model flow through a decision record.

| Domain | Written by | AI contribution | Governed by |
|---|---|---|---|
| `works/*/drafts/`, `world/artifacts/texts/`, `blog/drafts/` | **francis only** (mechanically enforced) | none — suggestions via `editorial/`, applied by hand | [DR-0001](decisions/0001-authorship-boundary.md), [Access Policy](AGENTS.md) |
| `works/*/scenes/`, outlines, briefs, roadmaps | collaborative | planning, continuity annotation | [DR-0003](decisions/0003-fact-view-split.md) |
| `world/` (canon) | collaborative | research synthesis; canon enters only via DR | [AGENTS.md rule 4](AGENTS.md), [DR-0003](decisions/0003-fact-view-split.md) |
| `research/` | collaborative | AI-led sweeps; human interviews under consent | [AGENTS.md rule 10](AGENTS.md), [roles/researcher](process/roles/researcher.md) |
| `editorial/` | AI (dramaturg) | reader-experience feedback only; never prose | [DR-0005](decisions/0005-editorial-system.md), [roles/dramaturg](process/roles/dramaturg.md) |
| `decisions/` | drafted by either | **approved only by francis** | [DR-0007](decisions/0007-improve-decision-process.md) |
| `process/`, `tools/`, `skills/`, `notebooks/`, `web/` | collaborative | heavy | [Layering Rule](AGENTS.md), [roles/automation](process/roles/automation.md) |
| `works/*/publish/`, `archive/`, `assets/generated/` | generated only | — | [Access Policy](AGENTS.md) |

## Attribution receipts

Who did each piece of work is recorded where the work is recorded:
**Author** cells in decision records' Affected Files tables, **source:**
fields on backlog entries, and the pure `prose:` commit ledger
(`git log --grep '^prose:'`) for every word of prose. The definition of
a role in force for any row is derivable:
`git show <commit>:process/roles/<role>.md`. Effort summaries are
generated from these receipts, never hand-written (process#0006).

## Contributors

Attribution cells use these registry keys (detail lives here, once):

- `francis` — Francis Lee <francis.g.lee@gmail.com>. Author. All prose.
- `claude-fable-5` — Anthropic Claude Fable 5 (model ID
  `claude-fable-5`), via Claude Code CLI · active 2026-07-25 – present ·
  roles per [process/roles/](process/roles/).

AI entries record: exact model ID string, provider, harness, dates
active, roles pointer — enough to re-run a comparable setup and
establish provenance, not to replay output (DR-0009, 0009-7). A model
change is a new key, never a re-attribution of old cells.

This is a private, single-author project; external contributions are
not accepted. For the reasoning behind this model, see
[process/principles.md](process/principles.md).
