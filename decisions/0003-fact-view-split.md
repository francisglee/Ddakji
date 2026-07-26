---
type: decision-record
number: 3
scope: process
kind: new
status: accepted
amended-by: 0007 (retrofit)
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0003 — Fact/view split: events are facts, scenes are views, artifacts split spec/text

**Description:** Impartial world facts separated from perspectival
tellings, at every level — including the process itself.

## Context
A multi-POV, multi-generational epic needs impartial structural truth
that many tellings can share: one historical event may generate several
scenes across works, styles, and perspectives. Worldbuilding must stay
POV-free; prose must stay human-only; planning metadata must stay
agent-maintainable.

## Alternatives considered
- **Combined scene files (metadata + prose in one)** — rejected: puts
  status/purpose behind the write-deny; agents can't maintain the
  planning layer.
- **Chronology maintained directly in timeline.md** — rejected as end
  state: duplicates event data; timeline becomes a generated view.
- **Per-medium folders for in-world texts** — rejected: taxonomy
  belongs in metadata (`medium:`), not tree structure.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0003-1 | Events as facts | `world/events/` holds impartial POV-free facts; canon enters via backlog → DR | — |
| 0003-2 | Scene spec/prose split | Scene docs (collaborative planning layer) pair by slug with drafts (human-only prose); order lives in `outline.md`, never filenames | — |
| 0003-3 | Artifact spec/text split | In-world texts: spec collaborative, canonical text human-only; typed by `medium:` | — |
| 0003-4 | Self-application | Process state machines live as data (`process/workflows/`); prose, diagrams, lint are views | — |
| 0003-5 | Timeline as view | `world/timeline.md` is a chronology view over events; generated once events accumulate | — |

## Consequences
Continuity becomes queryable: date lint, undramatized events,
cross-scene contradiction, quote-checks against canonical artifact
texts. Style guides layer: `world/style-guide.md` (cross-work
conventions) + `works/<work>/style.md` (per-work aesthetics).

## Affected Files
| File | Changes Made | Decision ID | Commit ID |
|---|---|---|---|
| [world/events/](../world/events/), [world/artifacts/](../world/artifacts/), [world/timeline.md](../world/timeline.md) | events, artifact spec/text folders, timeline-as-view | 0003-1, 3, 5 | 076a897 |
| [works/baek-il/scenes/](../works/baek-il/scenes/) + drafts/, [outline.md](../works/baek-il/outline.md) (both works) | spec/prose pairing, order-in-manifest | 0003-2 | 6e0aecf |
| [process/workflows/](../process/workflows/) | state machines as data | 0003-4 | cb9de32 |
| [templates/scene-doc.md](../templates/scene-doc.md), [templates/event.md](../templates/event.md), [templates/artifact.md](../templates/artifact.md) | the split encoded in forms | 0003-1 – 3 | cb9de32 |
