---
type: readme
---
# world/ — the story universe

Decided canon only, impartial and multi-work. When a scene and canon
conflict, canon wins until a DR rules otherwise (AGENTS.md rule 4).

**How canon enters** — per `process/workflows/canon-lifecycle.toml`
(DR-0010). Free thinking lives in `research/explorations/` (dimensions
and theses, multi-position, nothing binding); **distillation** — the
author's intentional selection of which theses to champion — creates a
`proposed` entry here citing its explorations; the DR gate (scope:
world) flips it to `canon`, after which scenes are bound and canonical
content changes only via DR. Simple entities may go `backlog/` →
`proposed` directly. Continuity lint checks scenes against `canon`
entities only. Nothing lands as canon directly from a research session
or conversation.

| Folder | Holds (template) |
|---|---|
| `events/` | impartial POV-free facts (`event`) — one event may generate many scenes |
| `artifacts/` | in-world text specs (`artifact`); canonical texts in `texts/` are **human-only** |
| `characters/<name>/` | `profile.md` + `voice.md` per character |
| `factions/` | families, companies, movements (`faction`) |
| `motifs/` | recurring images and their meaning (`motif`) |
| `themes/` | what the recurrence *means* — claim/question, tensions, exploration (`theme`) |
| `locations/` | places, with state-by-era (`location`) |
| `technology/` | sci-fi canon: capability, limits, what it forbids (`technology`) |

`style-guide.md` holds **cross-work conventions only** (romanization,
terminology, spelling of invented terms) — per-work aesthetics live in
`works/<work>/style.md`. `timeline.md` is a chronology view over
`events/`; it becomes generated once events accumulate
(process/backlog/).
