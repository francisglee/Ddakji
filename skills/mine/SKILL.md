---
name: mine
description: Mine journal entries - route captured ideas to backlogs, explorations, blog, and world proposals; report what went where. Usage - /mine [entry-slug | since <date>]
---

# /mine — route captured ideas

Reads `journal/entries/` (never writes there — Access Policy) and
routes content into structure. Invoked with a pointer (DR-0013-4);
default scope: entries not yet cited by any `mined/` report.

1. Read the target entries closely — the author's phrasing carries
   intent; don't flatten it.
2. Route each distinct idea to its home, citing the source entry:
   - open questions / ideas / bugs → the right domain's `backlog/`
     entry (`source: francis`, body cites `journal/entries/<file>`)
   - thematic territory → seed or extend a `research/explorations/`
     doc
   - post material → `blog/backlog/` entry
   - candidate canon → `world/backlog/` entry (never directly into
     `world/` — canon-lifecycle)
   - process friction → `process/backlog/` entry
3. Anything requiring an author decision (contradicts canon, implies a
   DR, ambiguous intent) is NOT filed — it's listed in the report under
   "Needs your call."
4. Write the mining report to `journal/mined/<date>-report.md`: table
   of idea → destination (linked) → status (filed | needs your call),
   plus anything deliberately left unrouted and why.
5. Never mark entries; "mined" is derivable from reports citing them.
   Never editorialize on the writing itself — this is routing, not
   coverage.
