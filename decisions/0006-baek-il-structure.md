---
type: decision-record
number: 6
scope: baek-il
kind: new
status: accepted
amended-by: 0007 (retrofit)
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0006 — Baek-il structured as main narrative + flashback scene

**Description:** The short story is two scenes — a main narrative and a
shorter flashback — and serves as the vertical slice of the Ddakji
universe.

## Context
Baek-il is the project's initial pitch: a short story that serves as
the vertical slice of the Ddakji universe — testing the world, voice,
and this entire production pipeline end-to-end before committing to the
epic.

## Alternatives considered
- **Single linear narrative** — set aside: loses the temporal
  counterpoint the flashback provides.
- **Full frame story** — set aside: heavier apparatus than a short
  story wants.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0006-1 | Two-scene structure | Main narrative + shorter flashback; slugs `main-narrative`, `flashback`; wired by `outline.md` | — |
| 0006-2 | Vertical-slice mandate | At least one scene traverses the full pipeline (draft → coverage → revision → lock → export → publish) before Ddakji drafting begins | — |

### Details

**0006-1.** Flashback *placement* (opening vs interleaved) is
deliberately not decided here — open as `baek-il#0001`, to be resolved
by its own record before v0.2.0.

## Consequences
Lessons from shipping Baek-il feed Ddakji's backlog and the process
retros.

## Affected Files
| File | Changes Made | Decision ID | Commit ID |
|---|---|---|---|
| [works/baek-il/scenes/main-narrative.md](../works/baek-il/scenes/main-narrative.md), [flashback.md](../works/baek-il/scenes/flashback.md) | two scene specs at sketch | 0006-1 | 6e0aecf |
| [works/baek-il/outline.md](../works/baek-il/outline.md) | assembly wiring the two slugs | 0006-1 | 6e0aecf |
| [works/baek-il/README.md](../works/baek-il/README.md), [brief.md](../works/baek-il/brief.md), [ROADMAP.md](../works/baek-il/ROADMAP.md) | vertical-slice role and pipeline mandate | 0006-2 | 6e0aecf |
