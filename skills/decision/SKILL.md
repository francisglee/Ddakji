---
name: decision
description: Draft a decision record from the current discussion, iterate with the author, commit only on approval. Usage - /decision [short title]
---

# /decision — decision record

Procedure (lifecycle data: `process/workflows/decision-lifecycle.toml`):

1. **Granularity check** (AGENTS.md): one independently reversible
   decision per record; itemize its facets as `NNNN-K` only if they
   would reverse *together* — otherwise propose separate records. If
   the discussion contains a *plan* (scene detail, outline order), STOP
   — that belongs in scene docs or outlines, not the log.
2. Number = highest existing in `decisions/` + 1 (4 digits). Title = a
   short functional headline; filename slugs it. Fill `scope:`
   (best-fit) and `kind:` (new | improvement | reversal | retirement).
3. Draft from `templates/decision-record.md`: Description line; Context
   from the actual discussion; Alternatives genuinely considered with
   why rejected; Decisions as the 4-column table (Backlog ID links the
   entry a decision resolves, `—` for discussion-born decisions) with
   `### Details` only where a row can't carry the substance;
   Consequences; Affected Files (File | Changes Made | Decision ID |
   Commit ID) — *actual* changes, `*pending*` commit cells.
4. **The draft stays in the working tree.** Present it to the author;
   iterate on their feedback. Commit ONLY on explicit approval —
   `decisions/` contains no drafts.
5. **Supersession / amendment.** Full reversal: new record; set the old
   record's `status: superseded-by NNNN`. Partial: add
   `amended-by: NNNN (NNNN-K)` to the amended record. These are the
   only legal edits to accepted records; each updates `last-updated`,
   both files change in one commit.
6. Process/infrastructure-scoped decisions: update every affected layer
   (AGENTS.md, workflows TOML, templates, skills) in the same change
   set — the Layering Rule. Implementing commits cite `DR-NNNN`.
7. **Close-out.** Immediately after implementation lands, fill the
   Commit ID cells (short hash, linked) and `last-updated` in a small
   follow-up commit. A record isn't closed until its cells are filled;
   phase (in-progress, closed) is derived, never stored.
8. Close resolved backlog entries: `status: decided`,
   `resolved-by: DR-NNNN`.
