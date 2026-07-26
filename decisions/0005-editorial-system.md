---
type: decision-record
number: 5
scope: process
kind: new
status: accepted
amended-by: 0007 (retrofit)
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0005 — Editorial system: workshop ethic, status gates, four-level passes

**Description:** AI editorial feedback made scoped, safe for early
drafts, and structurally incapable of ghostwriting.

## Context
AI editorial help is wanted, but feedback had to be scoped, safe for
early drafts, and structurally incapable of drifting into ghostwriting.
Borrowed from: Milford/Clarion workshop norms, publishing's staged edit
levels, film's script coverage and picture lock.

## Alternatives considered
- **Free-form feedback on request** — rejected: unscoped, drifts into
  prescription, no protection for early drafts.
- **Feedback rules only in skills** — rejected: skills load on
  invocation; the ethic must bind ambiently (the casual-paste moment),
  so it lives in AGENTS.md with procedures in `skills/coverage`.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0005-1 | Workshop ethic | Feedback = reader experience + diagnosis; prescriptions only on explicit request; replacement prose never | — |
| 0005-2 | Four-level taxonomy | Every pass declares developmental \| line \| copy \| proof and stays in scope | — |
| 0005-3 | Status gates as data | sketch: none · drafted: dev/line · revised: copy/proof · locked: reopening DR · published: errata — in `scene-status.toml` | — |
| 0005-4 | Coverage reports | `templates/coverage.md`, filed in `editorial/`, anchored to the scene doc's purpose/turns | — |

## Consequences
Feedback is comparable across scenes, scoped by request, and cannot
touch prose (mechanical fixes per DR-0001 Option A). WIP limit (≤3
drafted) and serial buffer (N+2) pace the pipeline the gates create.

## Affected Files
| File | Changes Made | Decision ID | Commit ID |
|---|---|---|---|
| [AGENTS.md](../AGENTS.md) | workshop ethic, gates, taxonomy rules | 0005-1 – 3 | a079fc1 |
| [process/workflows/scene-status.toml](../process/workflows/scene-status.toml) | gates as data | 0005-3 | cb9de32 |
| [templates/coverage.md](../templates/coverage.md) | report form | 0005-4 | cb9de32 |
| [skills/coverage/SKILL.md](../skills/coverage/SKILL.md), [process/roles/dramaturg.md](../process/roles/dramaturg.md) | pass procedure, role axioms | 0005-1, 2, 4 | 793fb35 / cb9de32 |
