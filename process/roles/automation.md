---
type: role
---
# Role: Automation

What process automation must never do silently. Axioms:

1. **Fail closed at apertures.** The exporter whitelists; anything not
   explicitly public stays private. A bug should under-publish, never
   over-publish.
2. **Generated means regenerable — and untouched.** ⚙️ outputs
   (`publish/`, `archive/`, `assets/generated/`, timeline views) are
   never hand-edited by anyone, human or agent.
3. **Destructive or public actions show their diff** and wait for the
   author: publishing, releasing, anything leaving the repo.
4. **No silent caps or skips.** If a pass bounds its coverage or skips a
   file, it says so in its report.
5. **State machines are read from `process/workflows/`** — tools never
   hardcode states, gates, or transitions (Layering Rule).
6. **Doc upkeep is visible.** Automated updates to changelogs, indexes,
   or status fields happen in their own commits with honest messages,
   categorized per the commit taxonomy.
