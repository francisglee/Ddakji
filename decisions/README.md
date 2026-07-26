---
type: readme
---
# decisions/ — the decision log

Every significant choice in this project — story, world, research,
blog, process, infrastructure — as one chronological sequence of
decision records (DRs). Read front to back, it is the story of the
project. Its purpose is receipts: evidence the book was written in
accordance with the project's ethos (`process/principles.md`).

## Reading a record

- **Number** — one sequence, all scopes (never split; DR-0004).
  Citations: `DR-NNNN`; decision items: `NNNN-K`;
  backlog origins: `<domain>#NNNN`.
- **scope:** `baek-il | ddakji | world | research | blog | process |
  infrastructure` — process = how we work; infrastructure = what we run.
- **kind:** `new | improvement | reversal | retirement`.
- **status:** validity only — `accepted`, `superseded-by NNNN`, plus
  `amended-by: NNNN (NNNN-K)` for partial supersession. Phase
  (in-progress, closed) is *derived* from implementing commits and the
  Affected Files table — never stored
  (`process/workflows/decision-lifecycle.toml`).
- **Decisions table** — itemized `NNNN-K`, each row linking the backlog
  entry it resolves (`—` = born in discussion). Details prose only
  where a row can't carry the substance.
- **Affected Files table** — files actually touched, with the commits
  that touched them. `git log --grep DR-NNNN` is the reverse index.

## Rules of the log

- One independently reversible decision per record; plans live in scene
  docs and outlines, not here.
- Drafts live in the working tree; committed = author-approved.
  This folder contains no drafts.
- Records are immutable; the legal edits are supersession and
  amendment (each updates `last-updated`), plus the close-out fill of
  Commit IDs when a change lands.
- 0001–0006 were retrofitted to this format under DR-0007 — the only
  mass edit this log will ever contain.

No index is maintained here by hand; `ls` is the index until the
generated one exists (process backlog).
