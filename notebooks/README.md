---
type: readme
---
# notebooks/ — marimo visualizations

Marimo notebooks are plain `.py` files: they diff and version like
everything else here. Each notebook declares its own dependencies inline
(PEP 723), so there is no shared environment to maintain.

## Running

```bash
uv run marimo edit --sandbox notebooks/workflows.py   # interactive
uv run --script notebooks/workflows.py                # headless render
```

(`uv` required — https://docs.astral.sh/uv/. The stdlib-only guarantee
applies to `tools/`, not here.)

## Conventions

- Read-only over the repo; write only to `assets/generated/`.
- Parse repo files via `tools/lib.py` — never re-implement parsing.
- State machines come from `process/workflows/*.toml`, never hardcoded.

## Index

| Notebook | Renders |
|---|---|
| `workflows.py` | state-machine diagrams from `process/workflows/` → `assets/generated/` |

Planned (build when the data exists — see process/backlog/): timeline
from `world/events/`, character/faction relation graphs, event→scene
coverage matrix, word-count burndown from git history.
