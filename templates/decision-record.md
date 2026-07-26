---
template: decision-record
target: decisions/
---
<!-- One INDEPENDENTLY REVERSIBLE decision per record; itemize facets as
     NNNN-K (facets must reverse together — else split records).
     Lifecycle (process/workflows/decision-lifecycle.toml): draft in
     working tree → author approval → commit. decisions/ contains no
     drafts. Records are immutable; legal edits (each updates
     last-updated): status: superseded-by NNNN · amended-by: NNNN (NNNN-K).
     status: records VALIDITY only; phase (in-progress, closed) is
     derived from citing commits + Commit ID cells — never stored.
     Implementing commits cite DR-NNNN. Close-out: fill Commit ID cells
     right after landing. Filename: NNNN-<title-slug>.md -->
---
type: decision-record
number:
scope:                # baek-il | ddakji | world | research | blog | process | infrastructure
kind:                 # new | improvement | reversal | retirement
status: accepted      # accepted | superseded-by NNNN  (+ amended-by: NNNN (NNNN-K))
date-created:
last-updated:
---
# NNNN — Title (short functional headline)

**Description:** one line stating the substance.

## Context
<!-- the situation and the discussion that led here -->

## Alternatives considered
<!-- each serious option, and why rejected -->

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| NNNN-1 |  |  | <domain>#NNNN or — |

### Details
<!-- ONLY where a row can't carry the substance; omit otherwise -->

## Consequences
<!-- what changes; canon/scenes invalidated; follow-ups → backlog entries -->

## Affected Files
<!-- actual changes, completed when the change lands; links; close out
     with commit hashes after landing -->
| File | Changes Made | Decision ID | Commit ID |
|---|---|---|---|
|  |  |  | *pending* |
