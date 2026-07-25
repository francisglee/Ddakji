---
name: sdr
description: Draft a Story Decision Record from the current discussion. Usage - /sdr [short title]
---

# /sdr — decision record

Procedure:

1. **Granularity check** (AGENTS.md, SDR discipline): the record must
   capture ONE independently reversible decision. If the discussion
   contains several, propose the split and draft them separately. If it
   contains a *plan* rather than a decision (scene detail, outline
   order), STOP — that belongs in scene docs or outlines.
2. Number = highest existing in `decisions/` + 1 (zero-padded, 4
   digits). Filename `NNNN-<slug>.md`.
3. Draft from `templates/sdr.md`: context from the actual discussion;
   alternatives genuinely considered (with why rejected); the decision
   imperative; consequences including any scenes/canon invalidated and
   follow-ups routed to backlogs.
4. Set `scope:` best-fit (`baek-il | ddakji | world | process`); if it
   supersedes an earlier record, set that record's
   `status: superseded-by NNNN` — the ONLY edit ever made to an
   accepted SDR.
5. Process-scoped decisions: update every affected layer (AGENTS.md,
   workflows TOML, templates, skills) in the same change set — the
   Layering Rule.
6. Present the draft to the author for acceptance before treating the
   decision as made.
