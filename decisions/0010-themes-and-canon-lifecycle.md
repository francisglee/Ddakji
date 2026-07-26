---
type: decision-record
number: 10
scope: process
kind: new
status: accepted
date-created: 2026-07-25
last-updated: 2026-07-25
---
# 0010 — Add themes & codify canon refinement

**Description:** A theme entity holding championed theses; free
multi-thesis exploration in `research/explorations/`; distillation as
the intentional selection between them; the whole world-entity
refinement flow codified as data.

## Context
Thematic work needs depth the brief can't hold — the brief is an
executive summary whose Themes section should map, not explore. Themes
span works, placing them in `world/` beside motifs — one abstraction
level up: a motif is an image that recurs; a theme is what the
recurrence means. The author wants exploration and discussion (e.g.
dimensions and theses of "free will vs fate") kept distinct from the
positions the universe champions, with an intentional selection step
between — and the refinement mechanics made explicit for all world
entities, not just themes.

## Alternatives considered
- **Deep theme exploration inside brief.md** — rejected: bloats the doc
  every agent loads for context; briefs map, explorations explore.
- **Exploration embedded in world/ entries (two-tier files with a free
  Exploration section)** — the first draft of this record; rejected:
  dilutes the bible's invariant that `world/` holds decided canon only.
  Free thinking already has a home — `research/` — and moving it there
  restores purity and yields the symmetry: an exploration is to a world
  entity what a DR's Alternatives are to its Decision.
- **Per-work theme docs** — rejected: themes span works; per-work
  expression is a section inside each theme file.
- **Folders per entity type in research/ (mirroring world/'s tree)** —
  rejected: taxonomy in metadata; one `explorations/` folder typed by
  `explores:`.
- **Reusing research-note verification statuses for theses** —
  rejected: notes assert verifiable claims; theses are positions to be
  argued, not verified. Different epistemics, separate template.
- **Naming the entity-type field `type:`** — rejected: reserved for
  template identity (same collision as 0008-2); the field is
  `explores:`.
- **DR-gating exploration itself** — rejected: exploration must be free
  or it won't happen; ceremony belongs at the canonization boundary.
- **Distillation as its own DR** — rejected: immutable ceremony on a
  provisional act; `proposed` entities are drafts-of-canon meant to be
  cheap to revise, and a distillation-DR would turn every
  reconsideration into supersession churn. The event is logged by
  commit + cross-links; the rationale is required at the canonization
  DR instead (0010-4).

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0010-1 | Theme entity | `world/themes/<slug>.md`, template `theme.md`: Statement, Tensions, per-work Expression; cites its `explorations:` — no exploration content in world/ | — |
| 0010-2 | Statement discipline | A theme is the *championed thesis*, written as a claim or question, never a topic — checkable by developmental passes | — |
| 0010-3 | Explorations in research/ | `research/explorations/` + `templates/exploration.md`: dimensions and theses argued multi-sided, typed by `explores:` (entity type), `informs:` backfilled at distillation; nothing binds | — |
| 0010-4 | Distillation | The author's intentional selection of which theses to champion; creates the `proposed` world entity citing its explorations. Logged by the distilling commit + cross-links; rationale is recorded at canonization (see Details) | — |
| 0010-5 | Canon lifecycle as data | `process/workflows/canon-lifecycle.toml` for ALL world entities: backlog → exploring → proposed → canon (DR gate) → amendment; direct backlog → proposed for simple entities; research-first entry legal | — |
| 0010-6 | Brief theme convention | Briefs' Themes section holds one-liners linking `world/themes/`; exploration never lives in a brief | — |
| 0010-7 | research/notes/ | Notes move from research/ root to `research/notes/` — one folder per document type (notes, interviews, explorations, backlog), completing the type-folder pattern; classification within a type stays in metadata | — |

### Details

**0010-4.** Distillation-the-event is fully logged without a DR: the
commit creating the `proposed` entity carries timestamp, author, and
category, and the `explorations:` / `informs:` cross-links carry
provenance both ways. Distillation-the-rationale is deliberately
deferred: a `proposed` entity is a draft-of-canon meant to be cheap to
revise, and DRs are immutable — a distillation-DR would make every
provisional reconsideration a formal supersession. The rationale lands
once, at the binding moment, as a **requirement**: a world-scope DR
canonizing an entity with `explorations:` MUST engage the unchampioned
theses in its Alternatives section — cited from the exploration, with
why each was not chosen. Provisional leanings in between live freely in
the exploration's Notes. The receipts thus keep the roads not taken
(the exploration), the road taken (the entity), and the why (the
canonization DR) — with no unlogged gap.

**0010-5.** Entrypoints into world/ are multiple and converge at the
same DR gate: `world/backlog/` → proposed (direct); `world/backlog/` →
exploring → proposed; and research-first — an exploration created
straight from research work with no backlog entry, since research
intake is free. Continuity lint checks scenes against `canon` entities
only, which is what makes free exploration safe.

## Consequences
- `templates/theme.md`, `templates/exploration.md`, `world/themes/`,
  `research/explorations/` added; AGENTS.md schema list gains both
  types.
- `process/workflows/canon-lifecycle.toml` added; `world/README.md` and
  `research/README.md` bind to it by reference.
- `templates/brief.md` Themes section gains the link-out convention.
- Natural first exploration: the thematic territory around 백일 and
  inheritance/the ddakji game (baek-il#0002, world#0001 adjacency) —
  `explores: theme`, created whenever the author begins.

## Affected Files
| File | Changes Made | Decision ID | Author | Commit ID |
|---|---|---|---|---|
| [templates/theme.md](../templates/theme.md) | new template — championed-thesis form, cites explorations | 0010-1, 0010-2 | claude-fable-5 | 42a812d |
| [templates/exploration.md](../templates/exploration.md) | new template — dimensions/theses, `explores:`/`informs:` | 0010-3 | claude-fable-5 | 42a812d |
| [world/themes/](../world/themes/), [research/explorations/](../research/explorations/) | new folders | 0010-1, 0010-3 | claude-fable-5 | 42a812d |
| [process/workflows/canon-lifecycle.toml](../process/workflows/canon-lifecycle.toml) | new: refinement flow as data, incl. distillation + entrypoints | 0010-4, 0010-5 | claude-fable-5 | 42a812d |
| [world/README.md](../world/README.md) | canon-entry prose binds to the TOML; themes row | 0010-5 | claude-fable-5 | 42a812d |
| [research/README.md](../research/README.md) | restructured: parallel per-type sections (notes / interviews / explorations / backlog), each with its epistemic mode and machinery | 0010-3, 0010-4, 0010-7 | claude-fable-5 | 42a812d |
| [templates/brief.md](../templates/brief.md) | Themes link-out convention | 0010-6 | claude-fable-5 | 42a812d |
| [templates/research-note.md](../templates/research-note.md), [research/notes/](../research/notes/), [skills/research/SKILL.md](../skills/research/SKILL.md) | target → `research/notes/`; folder added (no files to migrate); filing path updated | 0010-7 | claude-fable-5 | 42a812d |
| [skills/decision/SKILL.md](../skills/decision/SKILL.md) | canonization-DR Alternatives requirement for explored entities | 0010-4 | claude-fable-5 | 42a812d |
| [AGENTS.md](../AGENTS.md) | `theme`, `exploration` in schema key-types list | 0010-1, 0010-3 | claude-fable-5 | 42a812d |
