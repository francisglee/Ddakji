---
type: decision-record
number: 14
scope: process
kind: improvement
status: accepted
date-created: 2026-07-26
last-updated: 2026-07-26
---
# 0014 — Ground principles in external authorities

**Description:** `process/principles.md` gains a References section
citing the consensus guidance that informs it; external authority
enters the why-layer only via `process/reading/` notes → DR; seeded
with the Authors Guild AI Best Practices for Authors.

## Context
The operating principles were reasoned from first principles in
conversation. The author wants them grounded in — and checkable
against — published consensus on AI-assisted authorship (starting with
the Authors Guild's guidance), with more guides addable over time. The
intake mechanism already exists: `process/reading/` notes record
external materials and what they changed here.

## Alternatives considered
- **Folding into DR-0013** — rejected: independently reversible from
  playbooks (the 0007-1 guardrail; same test that split 0008).
- **Inline citations scattered through principles** — rejected: a
  References section is the single registry; principle sections cite
  into it.
- **Adopting external guides as binding** — rejected: authorities
  *inform* principles, they do not *govern* them. The commitments are
  the author's; references establish provenance and enable a "checked
  against consensus" claim, not outsourced ethics. Divergences from a
  cited authority are noted deliberately, not hidden.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0014-1 | References section | `principles.md` ends with References: each entry an authority (linked) + one line on what it informs here; principle sections cite entries | — |
| 0014-2 | Intake path | External guidance enters the why-layer only via a `process/reading/` note (summary, what it argues, what it changed here) → DR for any principle change. No principle edits from a skim | — |
| 0014-3 | Seed | Authors Guild, "AI Best Practices for Authors" (authorsguild.org/resource/ai-best-practices-for-authors/): reading note filed; References entry added; principles checked against it, divergences (if any) noted | — |

## Consequences
- Implementation includes actually reading the guide (fetched at
  landing) — the reading note must be honest, not a placeholder.
- If the check against the guide suggests principle *changes*, those
  are proposed separately for author review (0014-2's own rule), not
  slipped into this change set.
- Future guides repeat the loop: reading note → References entry → DR
  if principles move.

## Affected Files
| File | Changes Made | Decision ID | Author | Commit ID |
|---|---|---|---|---|
| [process/principles.md](../process/principles.md) | References section; section citations | 0014-1, 0014-3 | claude-fable-5 | *pending* |
| [process/reading/authors-guild-ai-best-practices.md](../process/reading/authors-guild-ai-best-practices.md) | new reading note (guide fetched and read; alignment check included) | 0014-2, 0014-3 | claude-fable-5 | *pending* |
| [process/backlog/0010-authors-guild-principle-proposals.md](../process/backlog/0010-authors-guild-principle-proposals.md) | four proposed principle changes filed for author decision (per 0014-2) | 0014-2 | claude-fable-5 | *pending* |
