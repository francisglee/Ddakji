---
type: decision-record
number: 9
scope: process
kind: improvement
status: accepted
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0009 — Contribution attribution & transparency

**Description:** Who-did-the-work becomes part of the receipts: Author
column on Affected Files, `source:` field on backlog entries, one
attribution vocabulary, a CONTRIBUTING.md stating the per-domain
contribution model, and effort summaries as generated-only reports.

## Context
The receipts say *what* changed and *when*, but not *who did the work*
— which matters in a project whose core claim is a precise division of
labor between human and AI. Commit trailers carry some of this, but
in-doc attribution makes it scannable, and there is no single
human-readable statement of the contribution model per domain for an
outside reader (publisher, collaborator) to consult.

## Alternatives considered
- **Author column on the Decisions table** — rejected: every decision
  is author-approved by definition (0007-4); "who decided" is constant
  and derivable. Attribution attaches to *work*, not decisions.
- **Different vocabularies for Author and Source** — rejected: same
  actors, two spellings would fracture any future attribution query.
- **Deriving attribution from git commit authorship** — rejected as
  sole source: commits batch multiple actors' contributions and
  trailers vary by tool; in-doc attribution is the declared record,
  git the corroboration.
- **A detailed per-domain contribution page** — rejected: the detail
  already lives in `process/roles/`, AGENTS.md, and domain READMEs; a
  second copy drifts. CONTRIBUTING.md is a one-screen map that links,
  never restates.
- **Hand-maintained contribution/effort summary** — rejected: efforts
  are fully derivable from Author/source/`prose:` ledger; storing
  derivables drifts. Summaries are generated only.
- **Explicit versioning of process/ entities (roles, workflows,
  automation)** — rejected: the definition in force at any moment is
  derivable from a row's Commit ID (`git show <commit>:<path>`), and
  meaningful revisions are already named by their DRs. Version numbers
  would add bump-ceremony, drift risk (an unbumped edit lies), and a
  second naming scheme for states DRs already name.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0009-1 | Author column | Affected Files becomes `File \| Changes Made \| Decision ID \| Author \| Commit ID` (amends 0007-2) | — |
| 0009-2 | Backlog source field | Entry frontmatter gains `source:` — who raised the item (amends 0008-2) | — |
| 0009-3 | Attribution vocabulary | Cells hold a short registry key + optional role: `francis` · `claude-fable-5 (dramaturg)` · bare key for unroled use | — |
| 0009-7 | Contributors registry | Detailed identities defined once, in CONTRIBUTING.md; cells reference keys. Humans: name + email. AI: detail per the reproducibility guideline (Details) | — |
| 0009-4 | Backfill | Records 0001–0009 and all current backlog entries get honest attribution; a bounded second mass edit, narrower than 0007's retrofit | — |
| 0009-5 | CONTRIBUTING.md | Root-level, hand-written contribution *model*: per-domain table of who does what, linking to governing rules; changes only via DR | — |
| 0009-6 | Generated effort summaries | Any contribution/effort *summary* is tool-generated from the attribution receipts; never hand-maintained | — |

### Details

**0009-3.** Roles are those defined in `process/roles/` (dramaturg,
researcher, automation); the parenthetical is optional because some
work (e.g. process design) is unroled. Prose paths need no attribution
field — they are `francis` by construction (DR-0001).

**0009-5.** CONTRIBUTING.md is the public-facing companion to
`process/principles.md`'s disclosure stance: the first document an
outside reader consults on how this book is made. One screen; map, not
manual.

**0009-7.** AI registry entries record enough to *re-run a comparable
setup and establish provenance — not to replay output* (generative
output is not bit-reproducible; seeds/sampling params would be
reproducibility theater). Per AI entry: exact model ID string (the API
identifier, not the marketing name) · provider · harness/interface
(behavior differs by harness) · dates active in the project · roles
pointer to `process/roles/`. Explicitly not collected: sampling
parameters, seeds, context snapshots. A model change is a new registry
entry with a new key, never an edit that re-attributes old cells.
Role and workflow definitions are NOT separately versioned: the
definition in force for any row is derivable —
`git show <commit>:process/roles/<role>.md` — since every row carries
both Author and Commit ID, and every meaningful process change is
already named by its DR. Explicit version numbers would be a parallel
naming scheme with bump-ceremony and drift risk (see Alternatives).

**0009-6.** Implemented as a backlog entry (build when there is enough
data to summarize); the generator walks Author columns, `source:`
fields, and the `prose:` commit ledger.

## Consequences
- `templates/decision-record.md` and `templates/backlog-item.md` gain
  the column/field; `skills/decision/SKILL.md` and AGENTS.md
  (Decision-record discipline) update the table spec.
- 0007 gains `amended-by: 0009 (0007-2)`; 0008 gains
  `amended-by: 0009 (0008-2)` — first live use of the amendment
  mechanism.
- CONTRIBUTING.md added at root; root README links it.
- `process#0006` filed for the effort-summary generator.
- Backfill touches 0001–0009 Affected Files tables and all current
  backlog entries; licensed by 0009-4.

## Affected Files
| File | Changes Made | Decision ID | Author | Commit ID |
|---|---|---|---|---|
| [templates/decision-record.md](../templates/decision-record.md), [templates/backlog-item.md](../templates/backlog-item.md) | Author column / `source:` field | 0009-1, 0009-2 | claude-fable-5 | 6c9c4f0 |
| [skills/decision/SKILL.md](../skills/decision/SKILL.md), [AGENTS.md](../AGENTS.md) | table spec + attribution vocabulary | 0009-1 – 3 | claude-fable-5 | 6c9c4f0 |
| [CONTRIBUTING.md](../CONTRIBUTING.md), [README.md](../README.md) | contribution model doc incl. Contributors registry; README link | 0009-5, 0009-7 | claude-fable-5 | 6c9c4f0 |
| [process/backlog/0006-effort-summary-generator.md](../process/backlog/0006-effort-summary-generator.md) | new entry for the generator | 0009-6 | claude-fable-5 | 6c9c4f0 |
| [0007](0007-improve-decision-process.md), [0008](0008-restructure-backlogs.md) | `amended-by` frontmatter; Author backfill | 0009-1, 0009-4 | claude-fable-5 | 6c9c4f0 |
| [0001](0001-authorship-boundary.md) – [0006](0006-baek-il-structure.md), all `*/backlog/` entries | Author / `source:` backfill | 0009-4 | claude-fable-5 | 6c9c4f0 |
