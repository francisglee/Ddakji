---
type: readme
---
# journal/

Your zero-structure notebook: write anything, anytime — routing happens
later, not while you're thinking. Nothing here is published.

## How to use it

1. Copy [templates/journal-entry.md](../templates/journal-entry.md) to
   `entries/YYYY-MM-DD-slug.md` and write freely. A date is the only
   requirement.
2. Commit it yours: `DRAFTS=1 git commit` with a `prose:` message.
3. Whenever you feel like it (batching days of entries is fine), say
   `/mine` — the AI routes your ideas into the right backlogs and
   seeds, and leaves a report in `mined/` telling you what went where
   and what needs your call.

**Full operator instructions:**
[process/playbooks/capture-freely.md](../process/playbooks/capture-freely.md)
— the step-by-step playbook for this workflow. (All human playbooks
live in [process/playbooks/](../process/playbooks/).)

## What lives where

| Folder | Holds | Who writes |
|---|---|---|
| `entries/` | your free capture, dated | **you only** (agents are hard-denied) |
| `mined/` | AI mining reports: idea → destination, plus "needs your call" items | AI, on `/mine` |

## Why it's protected

Entries are the **idea-provenance ledger**: timestamped evidence that
ideation originates with you, complementing the prose ledger
([DR-0015](../decisions/0015-journal-capture-layer.md),
[DR-0001](../decisions/0001-authorship-boundary.md)). "Mined" status is
never stamped on entries — a report citing an entry *is* the record.
In a live session, this whole flow collapses: talking to the AI is the
capture, and routing happens as you speak.
