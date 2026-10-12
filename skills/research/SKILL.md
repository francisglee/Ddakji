---
name: research
description: Investigate a question and file a sourced note in research/notes/, or re-review an existing note against current reality. Usage - /research <question> | /research review <note-slug>
---

# /research — sourced notes (and their curation)

Governed by `process/roles/researcher.md`. For interviews use
`/interview`; for thesis work use `/explore`.

## Filing a new note

1. Restate the question; identify what it informs (world entities,
   backlog items), the stream it serves (`streams:`, if any), and its
   `subjects:`, `periods:`, optional `cohorts:`, and — for diaspora —
   `waves:` (registries: `research/README.md`).
2. Investigate across lenses (numbers, scholarship, media, testimony,
   artifacts). Seek Korean-language sources for every cell; where none
   exist, say so in Method. Label every finding: historical fact /
   plausible extrapolation / invention.
3. File from `templates/research-note.md` into `research/notes/`:
   paper-style body (dimension sections; Contents only if long; Method
   recording questions, databases and queries, languages, date, model
   ID and effort, exclusions; References carrying full citations —
   numbers-lens entries with agency, series, unit, coverage, definition
   changes, retrieval date), `lenses:` listing the kinds of evidence
   actually used, `status:` per claim quality (`unverified` until
   corroborated by at least two lenses — DR-0017; testimony alone never
   verifies, nor does any other single lens), `date-created:` today,
   `sources:` complete.
4. Media: store under `assets/` named by owning slug; record
   `{path, caption, source, license}` in `media:`; scraped material is
   `license: reference-only`.
5. Cross-link `informs:` — world slugs this feeds and/or backlog IDs it
   addresses. Canon suggestions go to `world/backlog/` (canon enters
   only via backlog → DR).
6. Remaining questions → Open questions section AND `research/backlog/`
   entries.

## Working a stream (DR-0017)

A stream (`research/streams/<slug>.md`, from
`templates/research-stream.md`) holds the question set and which
period × lens (or wave × lens) cells matter. Opening one is the
author's act; the agent proposes questions and cells, never decides
them. Each `/research` call then files a note tagged `streams:`; the
stream's Gaps section is updated when a note leaves a cell at one lens
or without Korean-language sources. Coverage is derived from note
frontmatter (process#0012), never listed in the stream doc. Human
lane: `process/playbooks/run-a-research-stream.md`.

## Re-reviewing a note (curation, DR-0011)

1. Re-verify the note's claims against current reality and its sources.
2. Update content where reality moved; adjust `status:` honestly
   (verification can downgrade). Re-check the two-lens rule: a
   `verified` claim whose corroborating lens has fallen away goes back
   to `unverified`.
3. Stamp `last-reviewed:` with today — only if a genuine
   re-verification happened; the stamp means exactly that.
4. New gaps or invalidated canon → backlog entries (continuity impact
   → the affected work's backlog).
