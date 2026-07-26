---
type: decision-record
number: 15
scope: process
kind: new
status: accepted
date-created: 2026-07-26
last-updated: 2026-07-26
---
# 0015 — Add the journal capture layer

**Description:** `journal/` as the zero-structure human-only entry
point — free capture, then an AI mining pass routes content to
backlogs, explorations, blog, and world proposals; entries double as
the idea-provenance ledger. Token-spend tracking filed as cost
disclosure, explicitly not a contribution metric.

## Context
Every structured entry point (backlog entries, exploration docs,
templates) demands the human know where things go. In collab sessions
the AI is the free-form entry point — the author speaks intent, the AI
routes. Solo and turn-based work lacked the mirror: a capture surface
with zero structural demands, mined later. Separately, the author asked
whether AI contribution could be quantified by token spend.

## Alternatives considered
- **Convention-only (no deny) journal** — rejected: hard-denied entries
  make the journal an *idea-provenance ledger* — timestamped evidence
  that ideation originates with the author, complementing the prose
  ledger (DR-0001); a convention can't carry that evidentiary weight.
- **Naming the AI-side folder `editorial/`** — rejected: nothing is
  being critiqued or improved; the pass mines and routes. `mined/`.
- **A `mined:` flag on entries** — rejected: derivable (a mining report
  cites the entry); don't store derivables.
- **Token spend as a contribution metric** — rejected: spend measures
  compute consumed (thinking, failed attempts, ephemeral conversation),
  not contribution landed; identical spends differ 100× in effect.
  Contribution stays artifact-based (Author, `source:`, prose ledger,
  commits). Spend is retained as *cost disclosure* — a different,
  legitimate claim — via backlog item.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0015-1 | journal/ | Root folder: `entries/` (✍️ human-only, hard-denied, dated filenames `YYYY-MM-DD-slug.md`) + `mined/` (🤝 mining reports) + README. Chronology is fact, not reorderable order — dated names are legal | — |
| 0015-2 | Zero-friction template | `templates/journal-entry.md`: date + free body; nothing else required at capture | — |
| 0015-3 | /mine skill | On invocation with a pointer: read entries → mining report in `mined/` — backlog entries filed directly (`source: francis`, citing the entry), exploration/blog/research seeds, items needing author decision. AI acts only when invoked (DR-0013-4) | — |
| 0015-4 | Enforcement extension | `journal/entries/**` joins the Access Policy human-only paths: deny adapter, pre-commit hook, `prose:` commit category | — |
| 0015-5 | Pre-intake in the lifecycle | `idea-lifecycle.toml` notes journal capture as legal pre-backlog entry; the capture → mine → route flow precedes all structured intake | — |
| 0015-6 | Token spend = cost, not contribution | Any token tracking is a disclosure metric, never cited as contribution; contribution remains artifact-based (DR-0009). Mechanism filed as `process#0009` (vendor-adapter capture → neutral ledger) | — |

## Consequences
- Per DR-0013's definition-of-done: ships with skill (`/mine`),
  playbook (*capture freely*), and the lifecycle note — all three
  lanes.
- `.claude/settings.json`, `.githooks/pre-commit`, `tools/lock|unlock`,
  AGENTS.md Access Policy + commit taxonomy gain the journal path.
- `process#0009` filed: session token-usage ledger (Claude Code hook →
  neutral log), labeled cost-disclosure-only.
- CONTRIBUTING.md prose-paths row gains journal entries.

## Affected Files
| File | Changes Made | Decision ID | Author | Commit ID |
|---|---|---|---|---|
| [journal/](../journal/) | README, `entries/`, `mined/` | 0015-1 | claude-fable-5 | ae108b3 |
| [templates/journal-entry.md](../templates/journal-entry.md) | new template | 0015-2 | claude-fable-5 | ae108b3 |
| [skills/mine/SKILL.md](../skills/mine/SKILL.md) | new skill | 0015-3 | claude-fable-5 | ae108b3 |
| [process/playbooks/capture-freely.md](../process/playbooks/capture-freely.md) | new playbook (lands with/after DR-0013) | 0015-3 | claude-fable-5 | ae108b3 |
| [.claude/settings.json](../.claude/settings.json), [.githooks/pre-commit](../.githooks/pre-commit), [tools/lock](../tools/lock), [tools/unlock](../tools/unlock) | journal/entries deny + guard + lock; hook exempts `.gitkeep` placeholders (not prose — discovered when the hook correctly blocked this record's own landing) | 0015-4 | claude-fable-5 | ae108b3 |
| [AGENTS.md](../AGENTS.md), [CONTRIBUTING.md](../CONTRIBUTING.md) | Access Policy path, commit taxonomy, contribution row, workflow index | 0015-1, 3, 4 | claude-fable-5 | ae108b3 |
| [process/workflows/idea-lifecycle.toml](../process/workflows/idea-lifecycle.toml) | journal pre-intake note | 0015-5 | claude-fable-5 | ae108b3 |
| [process/automation.md](../process/automation.md) | `/mine` row in the skill table | 0015-3 | claude-fable-5 | ae108b3 |
| [process/backlog/0009-token-usage-ledger.md](../process/backlog/0009-token-usage-ledger.md) | new entry — cost disclosure only | 0015-6 | claude-fable-5 | ae108b3 |
