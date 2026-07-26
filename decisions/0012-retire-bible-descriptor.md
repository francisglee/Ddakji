---
type: decision-record
number: 12
scope: process
kind: improvement
status: accepted
date-created: 2026-07-26
last-updated: 2026-07-26
---
# 0012 — Retire the "bible" descriptor

**Description:** `world/` is described as "the story universe" in
descriptive contexts and "canon" in authority contexts; "bible" is
retired from living documents.

## Context
"Bible" (from TV writing's series bible) appeared in eleven places
across living docs. The author wants impartial terminology —
particularly apt given the story itself engages religion. Committed
decision records containing the word are immutable and keep it
(precedent: 0007-7's treatment of historical commit messages).

## Alternatives considered
- **Keeping "bible"** — rejected: fails the impartiality criterion;
  industry jargon opaque to outside readers of a repo whose receipts
  are meant to be read.
- **"Ddakji worldbuilding"** — considered: accurate but names an
  activity, not the thing; doesn't compose in rule prose.
- **Replacing "canon" as well** — rejected, consciously: "canon" also
  has religious etymology, but it is thoroughly secularized in
  storytelling usage, load-bearing across status fields
  (`proposed | canon`), the canon lifecycle, and eleven prior records —
  replacement would churn the entire system for marginal gain. Bible
  retired, canon retained: ratified deliberately against the
  impartiality criterion.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0012-1 | Standard descriptors | Descriptive contexts: **"the story universe"**. Authority contexts: **"canon"** (AGENTS rule 4 becomes *Canon authority*; "canon outranks the scene"). "Bible" swept from living docs; immutable records keep it | — |

## Consequences
- Sweep: AGENTS.md (researcher role line, rule 4 name and text), root
  README (two table rows), `templates/coverage.md`,
  `process/roles/dramaturg.md`, `process/roles/researcher.md`,
  `world/README.md` (title and body).
- DR-0010's single occurrence stays (immutable record).
- `process/README.md` gains the roles-vs-skills conduct/procedure table
  (orientation addition riding this change set).

## Affected Files
| File | Changes Made | Decision ID | Author | Commit ID |
|---|---|---|---|---|
| [AGENTS.md](../AGENTS.md) | rule 4 → *Canon authority*; bible → story universe / canon; fixes cross-line "an DR" artifact from the 0007 sweep | 0012-1 | claude-fable-5 | *pending* |
| [README.md](../README.md) | table rows: story universe | 0012-1 | claude-fable-5 | *pending* |
| [world/README.md](../world/README.md) | title + body: story universe / canon | 0012-1 | claude-fable-5 | *pending* |
| [process/roles/dramaturg.md](../process/roles/dramaturg.md), [process/roles/researcher.md](../process/roles/researcher.md) | canon outranks / feeding the story universe | 0012-1 | claude-fable-5 | *pending* |
| [templates/coverage.md](../templates/coverage.md) | contradictions vs canon | 0012-1 | claude-fable-5 | *pending* |
| [process/README.md](../process/README.md) | roles-vs-skills table (rider) | 0012-1 | claude-fable-5 | *pending* |
