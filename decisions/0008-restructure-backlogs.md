---
type: decision-record
number: 8
scope: process
kind: improvement
status: accepted
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0008 — Restructure backlogs as per-item folders

**Description:** Each domain backlog becomes a folder of one-file-per-
item entries with stable IDs, enabling conflict-free parallel intake
and decision↔backlog traceability; summaries are generated, never
hand-maintained.

## Context
Backlogs are the project's issue tracker: intake for feedback, ideas,
questions, and bugs, feeding the idea lifecycle (backlog → DR → outline
→ scene → changelog). As single files, they invite merge conflicts
under parallel agent workflows, give items no individual metadata or
stable identity, and offer decision records nothing precise to cite as
an origin.

## Alternatives considered
- **Single backlog.md with inline item IDs** — rejected: still a merge
  bottleneck for concurrent intake; no per-item metadata or lifecycle.
- **Hand-maintained summary backlog.md concatenating entries** —
  rejected: hand-maintained derived views drift; summaries must be
  generated (automation axiom 2).
- **One global backlog** — rejected: domain backlogs keep intake close
  to the work; a global view is a generated concern.
- **Global ID space** — rejected: domain-prefixed references
  (`baek-il#0001`) are self-locating and let domains number
  independently.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0008-1 | Backlog folders | Each domain's `backlog.md` becomes `backlog/` with one file per item | — |
| 0008-2 | Entry schema & IDs | Filename `NNNN-slug.md` is the ID; referenced as `<domain>#NNNN`; typed frontmatter | — |
| 0008-3 | Generated summaries | Any backlog index/summary is tool-generated; until the generator exists, `ls` + frontmatter is the summary | — |
| 0008-4 | Decision↔backlog linkage | DR Decisions tables cite Backlog IDs; resolved entries point back via `resolved-by: DR-NNNN` | — |
| 0008-5 | Generalize idea lifecycle | One lifecycle branching after `decided`: story → outlined → written → shipped; non-story → implemented → closed | — |

### Details

**0008-1.** Domains: `works/baek-il/backlog/`, `works/ddakji/backlog/`,
`world/backlog/`, `research/backlog/`, `blog/backlog/`,
`process/backlog/`. Existing items migrate to entries; the old single
files are removed. `research/backlog/` is new (no single file to
migrate): intake for research questions and tasks — interviews to
conduct, claims to verify, sources to find — while *canon* questions
remain `world/` intake. One backlog per scope that can originate
decisions (DR-0007-6).

**0008-2.** Entry frontmatter: `kind` (idea | question | plot-bug |
continuity-bug | feedback | task — named `kind` because `type:` is
reserved for template typing), `status` (open | decided | done |
dropped), `priority` (now | next | later), `created`, `resolved-by`
(DR-NNNN, when status is decided). Template:
`templates/backlog-item.md`. Intake stays cheap: copy template, one
line of substance, done — ranking and grouping happen later, not at
capture.

**0008-4.** The two-way link is the traceability loop: feedback →
entry → ranked → cited by a DR's Backlog ID column → entry closed with
`resolved-by`. Entries resolved without a decision (plain tasks) close
as `done` with no DR reference.

**0008-5.** The current lifecycle tail (outlined → written → shipped)
is story-shaped and meaningless for process/infrastructure ideas. One
file with a branch after `decided` beats two files sharing a
`backlog → decided` prefix (shared prefixes drift). Entry statuses
align: `open` ↔ backlog, `decided` ↔ decided, `done` ↔ the no-DR task
path, `dropped` terminal. The record's own states live separately in
`decision-lifecycle.toml` (DR-0007) — the idea and the record
documenting it are different objects with different lifecycles.

## Consequences
- `templates/backlog-item.md` added; `templates/` docs referencing
  "backlog.md" update.
- Five backlog.md files migrate to folders; existing items become
  numbered entries (receipts preserved: item text carried over
  verbatim where possible).
- AGENTS.md idea-lifecycle wording and `process/workflows/idea-lifecycle.toml`
  notes update to reference entries and IDs.
- Backlog index generator added to the process backlog as an open item
  (build when volume warrants; generated-only per 0008-3).

## Affected Files
| File | Changes Made | Decision ID | Commit ID |
|---|---|---|---|
| [templates/backlog-item.md](../templates/backlog-item.md) | new template | 0008-2 | *pending* |
| [works/baek-il/backlog/](../works/baek-il/backlog/), [works/ddakji/backlog/](../works/ddakji/backlog/), [world/backlog/](../world/backlog/), [blog/backlog/](../blog/backlog/), [process/backlog/](../process/backlog/) | migrate single files → per-item entries | 0008-1, 0008-2 | *pending* |
| [research/backlog/](../research/backlog/) | new domain backlog (no migration); research/README.md notes the world-vs-research intake split | 0008-1, 0008-2 | *pending* |
| [AGENTS.md](../AGENTS.md) | lifecycle wording: entries, IDs, resolved-by linkage | 0008-3, 0008-4 | *pending* |
| [process/workflows/idea-lifecycle.toml](../process/workflows/idea-lifecycle.toml) | entry/ID wording; branch after `decided` for non-story ideas | 0008-3 – 0008-5 | *pending* |
