---
name: research
description: Investigate a question and file a sourced note in research/notes/, or re-review an existing note against current reality. Usage - /research <question> | /research review <note-slug>
---

# /research — sourced notes (and their curation)

Governed by `process/roles/researcher.md`. For interviews use
`/interview`; for thesis work use `/explore`.

## Filing a new note

1. Restate the question; identify what it informs (world entities,
   backlog items) and its `subjects:` bins (registry:
   `research/README.md`).
2. Investigate. Label every finding: historical fact / plausible
   extrapolation / invention.
3. File from `templates/research-note.md` into `research/notes/`:
   paper-style body (dimension sections; Contents only if long;
   References carrying full citations), `status:` per claim quality
   (`unverified` until sources corroborate; testimony alone never
   verifies), `date-created:` today, `sources:` complete.
4. Media: store under `assets/` named by owning slug; record
   `{path, caption, source, license}` in `media:`; scraped material is
   `license: reference-only`.
5. Cross-link `informs:` — world slugs this feeds and/or backlog IDs it
   addresses. Canon suggestions go to `world/backlog/` (canon enters
   only via backlog → DR).
6. Remaining questions → Open questions section AND `research/backlog/`
   entries.

## Re-reviewing a note (curation, DR-0011)

1. Re-verify the note's claims against current reality and its sources.
2. Update content where reality moved; adjust `status:` honestly
   (verification can downgrade).
3. Stamp `last-reviewed:` with today — only if a genuine
   re-verification happened; the stamp means exactly that.
4. New gaps or invalidated canon → backlog entries (continuity impact
   → the affected work's backlog).
