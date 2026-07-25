---
type: sdr
number: 5
scope: process
status: accepted
date: 2026-07-25
---
# 0005 — Editorial system: workshop ethic, status gates, four-level passes

## Context
AI editorial help is wanted, but feedback had to be scoped, safe for
early drafts, and structurally incapable of drifting into ghostwriting.
Borrowed from: Milford/Clarion workshop norms, publishing's staged
edit levels, film's script coverage and picture lock.

## Alternatives considered
- **Free-form feedback on request** — rejected: unscoped, drifts into
  prescription, no protection for early drafts.
- **Feedback rules only in skills** — rejected: skills load on
  invocation; the ethic must bind ambiently (the casual-paste moment),
  so it lives in AGENTS.md with procedures in `skills/coverage`.

## Decision
- Workshop ethic: feedback = reader experience + diagnosis; prescriptions
  only on explicit request; replacement prose never.
- Four-level taxonomy: developmental / line / copy / proof; every pass
  declares one and stays in scope.
- Status gates per `process/workflows/scene-status.toml`: sketch — no
  feedback; drafted — dev/line; revised — copy/proof; locked — reopening
  SDR required; published — errata only. Picture lock has teeth.
- Coverage reports use `templates/coverage.md`, filed in `editorial/`,
  anchored first to the scene doc's purpose/turns.
- Mechanical fixes: suggested diffs in `editorial/`, author-applied
  (per 0001, Option A).

## Consequences
Feedback is comparable across scenes, scoped by request, and cannot
touch prose. WIP limit (≤3 drafted) and serial buffer (N+2) pace the
pipeline the gates create.
