---
type: sdr
number: 3
scope: process
status: accepted
date: 2026-07-25
---
# 0003 — Fact/view split: events are facts, scenes are views, artifacts split spec/text

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

## Decision
- `world/events/` holds impartial, POV-free facts (dates, participants,
  constraints, sources). Canon enters via backlog → SDR.
- Scene **docs** (`works/*/scenes/`, collaborative: pov, date,
  characters, events, artifacts, status, purpose, turns, publish) pair
  by slug with scene **drafts** (`works/*/drafts/`, human-only prose).
  `outline.md` wires order; order never lives in filenames.
- In-world artifacts split the same way: spec (`world/artifacts/`) vs
  canonical text (`world/artifacts/texts/`, human-only), typed by
  `medium:` frontmatter.
- The principle applies to the system itself: `process/workflows/*.toml`
  are facts; AGENTS.md prose, diagrams, and lint are views.

## Consequences
Continuity becomes queryable: date lint, undramatized events,
cross-scene contradiction, quote-checks against canonical artifact
texts. Style guides layer: `world/style-guide.md` (cross-work
conventions) + `works/<work>/style.md` (per-work aesthetics).
