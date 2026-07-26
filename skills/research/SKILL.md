---
name: research
description: Investigate a question and file a sourced research note. Usage - /research <question>
---

# /research — sourced research note

Procedure:

1. Restate the question and identify what it informs (event, character,
   location, technology, theme).
2. Investigate. Distinguish and label: historical fact / plausible
   extrapolation / invention. Follow the researcher axioms
   (`process/roles/researcher.md`).
3. File the note from `templates/research-note.md` into `research/notes/`,
   with `status:` per claim quality (`unverified` until sources
   corroborate; testimony alone never verifies — see rule 10) and full
   `sources:`.
4. Reference images or media: store under `assets/` named by owning
   slug; record `{path, caption, source, license}` in the note's
   `media:` block; scraped material is `license: reference-only`.
5. Cross-link: add `informs:` slugs; if findings suggest canon, add an
   item to `world/backlog/` (canon enters only via backlog → DR —
   never write `world/` entries directly from research).
6. Open questions that remain go in the note's Open questions section
   AND the appropriate backlog.
