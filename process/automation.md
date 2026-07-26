---
type: automation-map
---
# Automation Map

What runs, when, guarding what. Pointers only — mechanics live in the
code (`tools/`), procedures in `skills/`, state machines in `workflows/`.

## Enforcement ladder (Access Policy, AGENTS.md)

| Layer | Mechanism | Scope |
|---|---|---|
| Prevention (hard) | `.claude/settings.json` deny rules | Claude Code |
| Prevention (cheap) | `tools/lock` — read-only file bits on prose | any tool, kernel-level |
| Prevention (strong, reserve) | read-only bind-mount container | any tool; build via DR when adopting tool #2 |
| Detection | `.githooks/pre-commit` — DRAFTS=1 signature + prose-commit purity | vendor-agnostic |
| Recovery | git history | always |

## What runs when

| Trigger | Runs | Guarded by |
|---|---|---|
| `/coverage <scene> [pass]` | editorial pass → `editorial/` | `workflows/scene-status.toml` feedback permissions |
| `/research <question>` | sourced note → `research/notes/`; re-review pass stamps `last-reviewed` | researcher axioms, fact statuses |
| `/interview prep\|process` | testimony → `research/interviews/` | consent block first; publish checklist enforces `quotable` |
| `/explore <territory>` | theses → `research/explorations/` | multi-sided, never concludes for the author; distillation gate |
| `/decision` | decision record → `decisions/` | DR discipline (AGENTS.md) |
| `/publish <target>` | `tools/export.py` → `publish/` | `workflows/publish-pipeline.toml` checks, author-reviewed diff |
| `/release <work> <ver>` | changelog, git tag, `archive/` snapshot, retro scaffold → `process/retros/` | semver rules |
| `git commit` | `.githooks/pre-commit` | prose signature + purity |
| ad hoc | `tools/stats.py` — scene table, word counts, lint | read-only |
| ad hoc | `notebooks/` (marimo) — timelines, graphs, workflow diagrams → `assets/generated/` | read-only over repo; writes only to generated |

## Implementation notes

- Pipeline tools are **stdlib-only** Python (no environment); shared
  parsing in `tools/lib.py`. Workflow files are TOML (stdlib `tomllib`)
  for exactly this reason.
- Notebooks carry their own deps (PEP 723 inline metadata; run via
  `uv run marimo edit --sandbox <nb>.py`).
- Reserve, not yet built: `tools/check-policy` (adapter-drift lint,
  when a second agent tool is adopted); container recipe (same trigger).
