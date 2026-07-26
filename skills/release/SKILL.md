---
name: release
description: Cut a version milestone - changelog, git tag, archive snapshot, retro scaffold. Usage - /release <work> <vX.Y.Z>
---

# /release — version milestone

Procedure:

1. **Semver check** (AGENTS.md rule 6): confirm the bump matches the
   change — MAJOR structural break / MINOR new or rewritten scenes /
   PATCH line fixes. Challenge a mismatch before proceeding.
2. Update `works/<work>/CHANGELOG.md`: new `## vX.Y.Z — <date>` section
   summarizing what shipped (keep-a-changelog style), citing DRs for
   the why.
3. Snapshot: copy `works/<work>/drafts/*` to
   `works/<work>/archive/vX.Y.Z/` (generated path — /release is its
   only writer).
4. Update the work's `ROADMAP.md` (milestone done; promote next/later).
5. Commit as `works: release <work> vX.Y.Z`; then
   `git tag <work>/vX.Y.Z`.
6. Scaffold the retro: create `process/retros/<work>-vX.Y.Z.md` from
   `templates/retro.md` with frontmatter filled, sections empty — the
   author fills it (offer to discuss, don't fill it for them).
7. Check the WIP limit and serial buffer for the next cycle; note
   violations in the roadmap.
