---
type: readme
---
# tools/ — the stdlib-only pipeline

Every script here runs on bare Python 3.11+ (`tomllib`) with **no
installs** — that is a guarantee, not a preference: these tools guard
privacy and rights boundaries and must work on any machine, forever.
What runs when: `process/automation.md`. Mechanics: read the code.

| Tool | Invocation | Does |
|---|---|---|
| `export.py` | `python3 tools/export.py baek-il\|ddakji\|blog` | Composes `publish/` output — whitelisted metadata + prose above the END marker, © stamped. Fails closed. Called via `/publish`. |
| `stats.py` | `python3 tools/stats.py` | Scene table (pov, date, status, turns, words), totals, and lint: invalid statuses, missing draft/spec pairs, dangling event refs. |
| `lock` / `unlock` | `tools/lock` · `tools/unlock` | Flip read-only file bits on all human-only prose paths (cheap kernel-level prevention). `unlock` before your writing session, `lock` after. |
| `lib.py` | imported | Shared parsing: frontmatter, workflow TOML, repo walking. The one definition of "how our files parse" — notebooks import it too. |

Reserve (not yet built, see `process/backlog/`): `check-policy`
adapter-drift lint — when a second agent tool is adopted.
