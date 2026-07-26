---
type: decision-record
number: 11
scope: process
kind: improvement
status: accepted
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0011 — Split research skills, add creation dates

**Description:** One research skill becomes three (`/research`,
`/interview`, `/explore`) under one shared researcher ethic; research
templates gain `date-created`; notes gain `last-reviewed` + curation
loop, subject bins, and a paper-style body; `informs:` accepts backlog
IDs alongside world slugs.

## Context
`research/` now holds three document types with distinct epistemics
(DR-0010): notes (verifiable claims), interviews (testimony under
consent), explorations (positions to be argued). A single `/research`
skill written for notes doesn't describe how to process an interview or
sustain an exploration, and the research templates carry no creation
date, leaving research staleness (which matters for near-future
extrapolation) to git archaeology.

## Alternatives considered
- **One branching skill** — rejected: three procedures with different
  inputs, outputs, and guards; a branching procedure is conditional
  complexity, the same reason exploration got its own template instead
  of a polymorphic research-note (0010).
- **Per-type roles (researcher-notes, researcher-interviews, …)** —
  rejected: roles are ethics, and the evidentiary/consent/labeling
  ethic is shared across all three types. Procedures differ; principles
  don't. One role, three skills.
- **`last-updated` on research templates** — rejected: it tracks
  *editing*, which is mechanical and derivable
  (`git log -1 --format=%as -- <file>`); hand-maintained it goes stale
  immediately. DRs carry it only because their edits are exceptional
  gated events. The curation need is a different date — *reviewing* —
  which is semantic and IS stored (0011-4): a note can be edited
  without re-verification and reviewed without editing, so git can
  never substitute for `last-reviewed`.
- **`last-reviewed` on interviews or explorations** — rejected:
  testimony is fixed at its interview `date:` (a moving present doesn't
  change what was said); explorations are positions, not
  reality-tracked claims.
- **Subject bins as subfolders of notes/** — rejected: taxonomy in
  metadata; notes routinely straddle bins (a chaebol piece is economy,
  industries, and politics at once) — multi-valued `subjects:` handles
  that, directories can't.
- **README sections as content inventories** — rejected: what-exists is
  derivable (`ls`) and drifts; README sections list *intent* — bin
  vocabulary, interview coverage targets, exploration territories
  anchored to stable backlog IDs.
- **Mandatory table of contents** — rejected: headers are the ToC
  (derivable; renderers generate it); optional for long notes so short
  notes carry no ceremony.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0011-1 | Three research skills | `/research` (sourced note → notes/), `/interview` (process testimony under consent → interviews/), `/explore` (start/continue a multi-sided exploration → explorations/) | — |
| 0011-2 | One researcher role | `process/roles/researcher.md` governs all three; explorations additionally engage the dramaturg ethic (thinking partner, conclusions are the author's) | — |
| 0011-3 | `date-created` on research templates | Set once at creation on research-note, interview, exploration; never edited thereafter | — |
| 0011-4 | `last-reviewed` on notes | Research-note gains `last-reviewed:` — stamped only on deliberate re-verification against current reality; the note's epistemic horizon | — |
| 0011-5 | Curation loop | `/research` gains a re-review procedure (re-verify, adjust `status:`, stamp `last-reviewed`); staleness report filed as a tooling backlog item (flag `verified` notes past a review horizon) | — |
| 0011-6 | Subject bins | Notes gain multi-valued `subjects:` from a controlled vocabulary registered in `research/README.md` (culture, history, demographics, government-politics, economy, industries, climate, religion, social-issues, language, technology-science) | — |
| 0011-7 | Paper-style note body | Research-note body: optional Contents (long notes), sections by relevant dimensions, References section (full citations; frontmatter `sources:` stays the machine-checkable list) | — |
| 0011-8 | `informs:` accepts backlog IDs | `informs:` entries are world slugs and/or `<domain>#NNNN` backlog IDs — a doc can feed canon or feed work; both reference forms self-locate | — |

### Details

**0011-1.** `/interview`'s distinct guards: consent block completed
before anything else; transcript handling per size rules; follow-ups
filed to `research/backlog/`. `/explore`'s distinct guards: argue
multiple sides seriously; never conclude for the author; distillation
is proposed only when the author initiates it (canon-lifecycle gate).

**0011-4.** Three dates, three treatments: `date-created` — semantic,
set once, stored. Last *edited* — mechanical, derivable from git,
never stored. `last-reviewed` — semantic and non-derivable (editing ≠
re-verifying; reviewing needn't produce a commit), stored, stamped only
by the deliberate act it names. Especially load-bearing for
present/near-future material whose truth moves under the story.

## Consequences
- `skills/research/SKILL.md` rescoped to notes; `skills/interview/` and
  `skills/explore/` added; AGENTS.md workflow index and
  `process/automation.md` skill table updated.
- `templates/research-note.md`, `templates/interview.md`,
  `templates/exploration.md` gain `date-created:` (interview keeps its
  separate `date:` — the interview date and the doc-creation date are
  different facts).
- `research/README.md` cleaned up and gains a Roles section
  (orientation change, done alongside).
- `process#0008` filed: staleness report — stats extension flagging
  `verified` notes whose `last-reviewed` exceeds a review horizon; the
  generated re-verification queue.

## Affected Files
| File | Changes Made | Decision ID | Author | Commit ID |
|---|---|---|---|---|
| [skills/research/SKILL.md](../skills/research/SKILL.md) | rescoped to notes explicitly | 0011-1 | claude-fable-5 | *pending* |
| [skills/interview/SKILL.md](../skills/interview/SKILL.md) | new — testimony processing under consent | 0011-1 | claude-fable-5 | *pending* |
| [skills/explore/SKILL.md](../skills/explore/SKILL.md) | new — multi-sided exploration partner | 0011-1 | claude-fable-5 | *pending* |
| [AGENTS.md](../AGENTS.md), [process/automation.md](../process/automation.md) | workflow index + skill table gain both | 0011-1 | claude-fable-5 | *pending* |
| [templates/research-note.md](../templates/research-note.md), [templates/interview.md](../templates/interview.md), [templates/exploration.md](../templates/exploration.md) | `date-created:` added; research-note also gains `last-reviewed:`, `subjects:`, paper-style body; `informs:` comments allow backlog IDs on all three | 0011-3, 4, 6 – 8 | claude-fable-5 | *pending* |
| [process/backlog/0008-staleness-report.md](../process/backlog/0008-staleness-report.md) | new entry — generated re-verification queue | 0011-5 | claude-fable-5 | *pending* |
| [research/README.md](../research/README.md) | reworked: tables-first, linked, bin registry, coverage targets, territories, roles | 0011-2, 0011-6 | claude-fable-5 | *pending* |
