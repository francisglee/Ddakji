---
type: readme
---
# research/ — sourced material feeding the bible

Story research: South Korean culture and history, near-future
extrapolation grounding, thematic material. (Research about *craft and
process* lives in `process/reading/` instead.) One folder per document
type; each type has its own epistemic mode and machinery:

**`notes/`** (`templates/research-note.md`) — **verifiable claims.**
Every claim carries `status: unverified | verified | disputed` plus
sources, and is labeled historical fact / plausible extrapolation /
invention (AGENTS.md rule 10, `process/roles/researcher.md`). The
publish checklist lints against unverified load-bearing claims.
Findings feed canon only via `world/backlog/` → DR.

**`interviews/`** (`templates/interview.md`) — **testimony under
consent.** Oral history from real people — family, friends, and others
whose experience informs the story. The consent block (recorded /
quotable / anonymize) governs all downstream use and is checked
mechanically at publish. Testimony corroborates but never verifies by
itself: claims sourced only to an interview stay `unverified`. Raw
recordings beyond a few MB live outside the repo, linked from the doc;
the transcript here is the durable artifact.

**`explorations/`** (`templates/exploration.md`, DR-0010) — **positions
to be argued.** Free thinking space around candidate world entities:
dimensions and theses argued from multiple sides, typed by `explores:`
(theme, character, technology…). Not claims — nothing here carries
verification status, and nothing here binds. Distillation — the author
choosing which theses to champion — creates the `world/` entry, which
cites its explorations; `informs:` is backfilled here. The roads not
taken stay on record.

**`backlog/`** (`templates/backlog-item.md`, DR-0008) — **intake.**
Research *work*: interviews to conduct, claims to verify, sources to
find. *Canon* questions (what should be true in the world) belong in
`world/backlog/` instead.

Media: reference images go in `assets/`, recorded in the referencing
doc's `media:` block with source and license; scraped material defaults
`reference-only` and never publishes.
