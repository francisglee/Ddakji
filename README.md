# Ddakji

A fiction project: **Baek-il**, a short story (main narrative + flashback),
and **Ddakji**, a planned near-future/historical epic spanning multiple
characters across generations — sharing one world.

This is a **private** repository. The only public aperture is the
`publish/` directories, produced by the export pipeline. Do not make this
repo public: the manuscript is unpublished and first-publication rights
matter.

## How this repo works

All prose is written by the human author. AI agents assist with research,
worldbuilding, continuity, and editorial feedback under the constitution
in [AGENTS.md](AGENTS.md), with the reasoning in
[process/principles.md](process/principles.md). The per-domain
contribution model and contributor registry live in
[CONTRIBUTING.md](CONTRIBUTING.md).

| Area | What it is |
|---|---|
| `works/` | The stories: brief, roadmap, outline, scene specs, prose drafts, editorial, published exports |
| `world/` | The bible: decided canon — events, characters, factions, locations, technology, motifs, artifacts |
| `research/` | Sourced research and interviews feeding the bible |
| `decisions/` | decision records — every significant choice, with alternatives and rationale |
| `process/` | Why and how we work: principles, roles, workflow state machines, retros |
| `skills/` | Agent procedures (coverage, research, decision, publish, release) |
| `templates/` | The form catalog — every structured doc type |
| `tools/` | Stdlib-only Python pipeline: export, stats, lock/unlock |
| `notebooks/` | Marimo visualizations (timelines, graphs, workflow diagrams) |
| `blog/` | Public writing about the making of the book |
| `web/` | Site code — consumes `publish/` only |

## Fresh clone setup

```bash
git config core.hooksPath .githooks   # activates the prose-protection hook
```

Agent tools must have their enforcement adapter in place before running
here — see the Access Policy in AGENTS.md.

© 2026 Francis Lee. All rights reserved. See [LICENSE](LICENSE).
