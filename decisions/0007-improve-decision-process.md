---
type: decision-record
number: 7
scope: process
kind: improvement
status: accepted
amended-by: 0009 (0007-2)
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0007 — Improve decision-record process

**Description:** Decision receipts — itemized decisions with
affected-files and commit traceability, human approval lifecycle,
richer metadata, expanded scopes, readable titles, and the rename
SDR → decision record.

## Context
The decision log's purpose is receipts: evidence that the book was
written in accordance with the project's ethos. The founding format
(0001–0006) recorded decisions and rationale but not their footprint —
tracing which files or commits a decision touched required git
archaeology. Decisions inside a record weren't individually
addressable, human approval was implicit, scope vocabulary lacked homes
for research-practice, blog, and technical decisions, titles weren't
optimized for scanning, and the name "Story Decision Record" misnamed
the majority of early records, which are process decisions.

## Alternatives considered
- **Affected Files written at draft time (planned changes)** —
  rejected: implementation drifts from plans; the receipt would lie.
  The table records *actual* changes, completed when the change lands.
- **`status: draft` for in-review records in decisions/** — rejected:
  muddies what presence in the log means. Drafts live in the working
  tree; committed = approved.
- **One record per decision item** — rejected here: these items are
  facets of a single format change and would reverse together (see
  0007-1 guardrail).
- **Renaming the Decisions section "Implementation"** — rejected: fits
  process records but breaks story records, where a decision is
  accepted now and implemented over weeks of prose; "Decisions" is
  accurate at every lifecycle stage for every scope. The spec-doc
  instinct lives in the itemization style and the Affected Files table.
- **Stored `in-progress`/`closed` status values** — rejected: both are
  derivable (citing commits + Commit ID cells); storing derivable state
  drifts and multiplies edits to accepted records. `status:` records
  validity only; phase is computed.
- **No Commit ID column (rely on `git log --grep DR-NNNN`)** —
  rejected: in-doc linkable receipts are worth one close-out edit per
  record, and story records gain direct links to the `prose:` commits
  that realized them.
- **Positional titles ("SDR Process Update 1")** — rejected: the number
  already sequences; functional names carry meaning.
- **Declarative-only titles (strict ADR convention)** — set aside: a
  functional headline plus a mandatory Description line serves scanning
  better for this log's audience.
- **Pure-table Decisions section** — rejected: table cells can't carry
  reasoning; table-plus-optional-Details instead (0007-9).
- **Separate templates/logs for story vs process decisions** —
  rejected: two templates drift; two logs break single-sequence
  citation (0004). Metadata (`scope:`, `kind:`) is the distinction;
  rigor flexes in content depth, not structure (0007-10).
- **Keeping `machinery:` as commit category alongside an
  `infrastructure` scope** — rejected: two names for one concept.
- **Full supersession of 0004 to rename one term** — rejected: 0004
  otherwise stands; partial amendment needs a lighter mechanism.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0007-1 | Itemized decisions | Each record numbers decisions `NNNN-K`, individually addressable | — |
| 0007-2 | Affected Files section | Closing table: `File \| Changes Made \| Decision ID \| Commit ID`, files actually touched, with links | — |
| 0007-3 | Bidirectional trace | Implementing commits cite `DR-NNNN`; `git log --grep` complements the Affected Files table | — |
| 0007-4 | Approval lifecycle | Draft in working tree → author review/iteration → commit only on explicit approval | — |
| 0007-5 | Metadata & legal edits | `date-created`/`last-updated`; three legal edits to accepted records | — |
| 0007-6 | Expanded scopes | Add `research`, `blog`, `infrastructure`; process = how we work, infrastructure = what we run | — |
| 0007-7 | Vocabulary alignment | Commit category `machinery:` → `infrastructure:` (amends 0004) | — |
| 0007-8 | Readable titles | Functional headline + Description line + `kind:` field; filename slugs title | — |
| 0007-9 | Decisions-as-table | This 4-column table + Details prose only where it adds substance | — |
| 0007-10 | Rename SDR → decision record | One template `decision-record.md`, skill `/decision`, citations `DR-NNNN`; story and non-story records share structure | — |
| 0007-11 | decisions/ README | Conventions-only reader's guide; index stays generated-later | — |
| 0007-12 | Commit close-out | After implementation lands, Commit ID cells are filled (short hash, linked); a record isn't closed until they are | — |

### Details

**0007-1.** Guardrail: items in one record must be facets that would
reverse *together*; an independently reversible facet is its own record
(granularity rule unchanged — DR-0008 exists because of this).

**0007-4.** The record lifecycle is enumerable, so it lives as data
(Layering Rule): `process/workflows/decision-lifecycle.toml`. Its
states are two kinds, and the file marks which: **stored** (frontmatter
`status:` — the decision's *validity*: accepted | amended | superseded)
and **derived** (computed, never written — the implementation's
*phase*: `in-progress` = accepted ∧ citing commits exist ∧ Commit IDs
pending; `closed` = accepted ∧ no pending Commit IDs). Don't store
what you can derive: stored copies of derivable facts drift. `draft`
exists only in the working tree; `decisions/` contains no drafts.

**0007-5.** Legal edits, each updating `last-updated`:
`status: superseded-by NNNN` (full), `amended-by: NNNN (NNNN-K)`
(partial, addressable to a decision item), and the one-time retrofit
licensed in Consequences. The 0007-12 close-out is part of the landing
window, not a separate edit class.

**0007-9.** Backlog ID links the backlog entry a decision resolves
(see DR-0008); `—` marks decisions arising from live discussion —
retroactive backlog entries are ceremony, not receipts. Details
subsections appear only where a row can't carry the substance.

**0007-10.** "SDR" misnames non-story records; `scope:` and `kind:`
already carry the taxonomy (metadata over parallel structures). Story
records remain first-class: identical structure, depth flexing with
stakes — the story's evolution is documented as carefully as the
system's.

**0007-12.** Mechanic (a commit cannot contain its own hash):
implementation lands citing `DR-NNNN` → a small close-out edit fills
Commit ID cells and `last-updated`. For story records this links the
decision directly to the `prose:` commits that realized it — the
decision ledger meets the authorship ledger.

## Consequences
- `templates/sdr.md` → `templates/decision-record.md`; `skills/sdr/` →
  `skills/decision/`; AGENTS.md, principles, roles, workflows TOML,
  READMEs, and backlogs sweep "SDR" → "decision record / DR".
- One-time retrofit of 0001–0006: renamed date fields, `last-updated`,
  `kind:`, `amended-by: 0007`, Description lines, Decisions tables, and
  Affected Files tables (with commit IDs — the scaffold commits are
  known). Existing filenames kept; naming convention applies from 0007
  forward. This is the only mass edit of accepted records the log will
  ever contain, and this record is its license.
- Historical commit messages using `machinery:` or lacking DR citations
  remain as-is; conventions apply from this commit forward.

## Affected Files
| File | Changes Made | Decision ID | Author | Commit ID |
|---|---|---|---|---|
| [templates/decision-record.md](../templates/decision-record.md) | renamed from decision.md; Decisions table format, Affected Files section, new metadata, expanded scopes, Description line, legal-edits + close-out comments | 0007-1, 2, 5, 6, 8, 9, 12 | claude-fable-5 | a5a10a7 |
| [skills/decision/SKILL.md](../skills/decision/SKILL.md) | renamed from decision; approval lifecycle, itemization guardrail, amendment procedure, table-at-landing, DR-NNNN citation, close-out step, title conventions | 0007-1 – 4, 8 – 10, 12 | claude-fable-5 | a5a10a7 |
| [AGENTS.md](../AGENTS.md) | DR discipline update, scope list, DR-NNNN citation convention, `machinery:` → `infrastructure:`, DR→DR sweep, schema-reference clarification (`type:` is template-backed — enumerable from templates/ — or structural singleton) | 0007-3, 5 – 7, 10 | claude-fable-5 | a5a10a7 |
| [process/principles.md](../process/principles.md), [process/roles/](../process/roles/), [process/workflows/](../process/workflows/), READMEs, backlogs | DR→DR terminology sweep | 0007-10 | claude-fable-5 | a5a10a7 |
| [decisions/README.md](README.md) | new: conventions-only reader's guide | 0007-11 | claude-fable-5 | a5a10a7 |
| [process/workflows/decision-lifecycle.toml](../process/workflows/decision-lifecycle.toml) | new: record lifecycle as data — stored validity states vs derived phase states (in-progress, closed) | 0007-4, 0007-12 | claude-fable-5 | a5a10a7 |
| [0001](0001-authorship-boundary.md) [0002](0002-vendor-neutral-architecture.md) [0003](0003-fact-view-split.md) [0004](0004-versioning-and-release.md) [0005](0005-editorial-system.md) [0006](0006-baek-il-structure.md) | retrofit: date fields, `kind`, `amended-by: 0007`, Description, Decisions + Affected Files tables | 0007-5, 8, 9 | claude-fable-5 | a5a10a7 |
