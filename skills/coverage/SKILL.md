---
name: coverage
description: Run a scoped editorial pass on a scene and file a coverage report. Usage - /coverage <scene-slug> [developmental|line|copy|proof]
---

# /coverage — editorial pass

Procedure (vendor-neutral; any agent or human can follow it):

1. Locate the scene doc `works/<work>/scenes/<slug>.md` and its paired
   draft `works/<work>/drafts/<slug>.md`.
2. **Gate check.** Read the scene's `status:` and the `[feedback]` table
   in `process/workflows/scene-status.toml`. If the requested pass is
   not permitted for this status, STOP and report why — do not proceed
   "just this once". No pass argument given: default to the highest
   pass the status permits.
3. Load context: the scene doc (purpose, turns, events, artifacts),
   `world/style-guide.md`, the work's `style.md`, the POV character's
   `voice.md`, and any `world/events/` docs the scene references.
4. Read the draft's prose (above `<!-- END SCENE -->`). Never quote the
   Evolution log in the report.
5. Write the report from `templates/coverage.md` to
   `works/<work>/editorial/<slug>--<pass>-<date>.md`, honoring the
   workshop ethic (AGENTS.md rule 1): reader experience and diagnosis;
   no rewritten prose; prescriptions only if the author explicitly
   asked. Anchor first to the scene doc's stated purpose and turn.
6. Copy/proof passes: list mechanical fixes as line-ref → issue →
   suggested replacement. The author applies them by hand (DR-0001).
   Never edit the draft.
7. Continuity or fact findings that exceed this scene's scope: file
   them in the work's `backlog.md` as continuity-bugs and note the
   cross-reference in the report.
