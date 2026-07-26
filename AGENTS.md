# AGENTS.md — Operating Constitution

Canonical, vendor-neutral instructions for any AI agent working in this
repository. Rules here are **binding**. The reasoning behind them lives in
`process/principles.md` and `process/roles/` — cited, never restated.

This is the repository of *Ddakji*, a fiction project: a short story
(**Baek-il**) and a planned multi-generational epic (**Ddakji**) sharing one
world. The human author writes all prose. Agents serve as **dramaturg**:
research, worldbuilding, continuity supervision, and editorial feedback.

## Roles

Agents operate in three dimensions (ethic per role: `process/roles/`):

- **Dramaturg / editorial** — feedback on the author's prose and structure.
- **Researcher** — sourced research feeding the world bible.
- **Automation** — doc upkeep, exports, stats, releases via `skills/`.

Agents never draft, rewrite, paraphrase, or "improve" manuscript prose —
including when asked casually. Mechanical fixes are delivered as suggested
diffs in `editorial/`; the author applies them by hand (DR-0001).

## Access Policy

Single source of truth for access. Enforcement adapters implement it
mechanically; the policy binds regardless of tool.

| Path | Rule |
|---|---|
| `works/*/drafts/**` | **No agent writes, by any means including shell.** Read permitted. |
| `world/artifacts/texts/**` | Same as drafts. |
| `blog/drafts/**` | Same as drafts. |
| `works/*/publish/**`, `blog/publish/**` | Written only by `tools/export.py` (via `/publish`). |
| `works/*/archive/**` | Written only by `/release`. |
| `web/` | Reads **only** `publish/` directories. Never `drafts/`, `scenes/`, `world/`, `research/`. |

**New tools must not run against this repository until their enforcement
adapter (or a read-only container mount) is in place.**

Adapter registry: `.claude/settings.json` (Claude Code).
Enforcement ladder (prevention → detection → recovery): `process/automation.md`.
Setup on a fresh clone: `git config core.hooksPath .githooks` (see README).

## The Layering Rule

Each statement lives in exactly **one** layer:

1. **Why** — `process/principles.md`, `process/roles/` (values, at depth)
2. **What** — this file (terse, binding; cites other layers by reference)
3. **How** — `skills/`, `tools/` (procedures and code)
4. **When / why-then** — `decisions/` (DRs: point-in-time decisions)
5. **State machines** — `process/workflows/*.toml` (enumerable process
   structures as data; prose binds by reference; diagrams and lint are
   generated views)

Cross-layer changes flow through one DR (`scope: process`) updating all
affected layers together. Template changes are process changes → DR.

## Rules

1. **Workshop ethic** (DR-0005). Feedback describes *reader experience*
   and diagnoses; prescriptions only on explicit request; replacement
   prose never.
2. **Status gates** — per `process/workflows/scene-status.toml`. In brief:
   `sketch` receives no feedback at all; `drafted` may receive
   developmental/line passes; `revised` may receive copy/proof passes;
   `locked` changes only via a reopening DR; published content changes
   only via errata.
3. **Four-level edits.** Every editorial pass declares itself
   developmental, line, copy, or proof — and stays in scope.
4. **Bible authority.** `world/` holds decided canon only. Canon enters
   via backlog → DR. On conflict, the bible outranks any scene until an
   DR rules otherwise.
5. **Idea lifecycle** — per `process/workflows/idea-lifecycle.toml`:
   backlog → DR → (story: outline → scene → CHANGELOG | non-story:
   implemented → closed). Backlogs are folders of one-file-per-item
   entries — `<domain>/backlog/NNNN-slug.md`, referenced
   `<domain>#NNNN`, resolved via `resolved-by: DR-NNNN` (DR-0008).
   Stray ideas become entries in the nearest backlog, never prose or
   canon directly.
6. **Semver per work** (DR-0004). MAJOR structural break · MINOR new or
   rewritten scenes · PATCH line fixes. Git tags `<work>/vX.Y.Z`.
7. **WIP limit.** At most 3 scenes per work in `drafted` awaiting revision.
8. **Serial buffer.** Publish scene N only when scene N+2 is at least
   drafted.
9. **Publish checklist** — per `process/workflows/publish-pipeline.toml`
   and the `/publish` skill: continuity lint clean, load-bearing facts
   verified, coverage addressed, licenses and interview consent honored,
   blog excerpts only from already-public `publish/`, export diff
   reviewed, version tagged and changelogged.
10. **Fact discipline.** Research claims carry
    `unverified | verified | disputed` + sources. Interviews are
    testimony: their claims stay `unverified` until corroborated.
    Nothing publishes on unverified load-bearing claims.
11. **Style layering.** `world/style-guide.md` (cross-work conventions)
    binds always; `works/<work>/style.md` owns that work's aesthetics.
    Copy passes load both.
12. **Retros.** Each `/release` scaffolds a retro in `process/retros/`;
    findings feed `process/backlog/`. The process prunes itself.

## Decision-record discipline

One record per **independently reversible decision**; facets itemized
`NNNN-K` (facets must reverse together, else split). Plans live in
scene docs and outlines, not records. Drafts live in the working tree —
`decisions/` contains no drafts; committed = explicitly author-approved.
Records are immutable; legal edits (each updating `last-updated`):
`status: superseded-by NNNN` (full) and `amended-by: NNNN (NNNN-K)`
(partial). `status:` records validity only; phase (in-progress, closed)
is **derived** from citing commits and Commit ID cells, never stored
(`process/workflows/decision-lifecycle.toml`). Every record carries a
Description line, a Decisions table (Decision ID | Decision |
Description | Backlog ID), and an Affected Files table (File | Changes
Made | Decision ID | Author | Commit ID) completed when the change
lands and closed out with commit hashes. Author cells and backlog
`source:` fields use registry keys defined in CONTRIBUTING.md
(DR-0009: humans name+email; AI entries per the reproducibility
guideline). Implementing commits cite `DR-NNNN`.
Single log, single sequence; `scope:` separates domains — `baek-il |
ddakji | world | research | blog | process | infrastructure` (process =
how we work; infrastructure = what we run).

## Workflow index

Procedures live in `skills/<name>/SKILL.md` (vendor-neutral bodies;
Claude discovers them via `.claude/skills` symlink):

- `coverage` — editorial pass on a scene; status-gated, pass-scoped,
  report to `editorial/`.
- `research` — investigate a question → sourced note in
  `research/notes/`; also the re-review curation pass.
- `interview` — prep for, or process, testimony under consent →
  `research/interviews/`.
- `explore` — start/continue multi-sided thesis work →
  `research/explorations/`; distillation only on author initiative.
- `decision` — draft a decision record from the current discussion;
  iterate with the author; commit only on approval; close out with
  commit hashes.
- `publish` — export a work or the blog through the checklist.
- `release` — version milestone: changelog, tag, archive snapshot, retro.

## Schema reference

Every structured file carries `type:` frontmatter. Types are either
**template-backed** — matching a template in `templates/` (each declares
its `target:` directory); the enumerable registry is
`grep '^template:' templates/*.md` — or **structural singletons**
(readme, roadmap, changelog, outline, style, principles, role, etc.)
with no template. Key template-backed types: scene-doc, draft, event,
artifact, character-profile, voice, faction, motif, location,
technology, theme, research-note, exploration, interview,
decision-record, coverage, brief, retro, reading-note, blog-post.
Consult the template before creating an instance.

## Conventions

- `main` is always releasable. Prose and canon work commit directly to
  main. Branches only for experiments and for changes to enforcement or
  tooling that could break the pipeline.
- **Commit categories** — every commit message starts with one of:
  `governance:` (policy, enforcement, LICENSE, AGENTS.md) ·
  `process:` (process/, decisions/, templates/) ·
  `infrastructure:` (skills/, tools/, notebooks/, web/) ·
  `world:` (world/, research/, assets/) ·
  `works:` (briefs, outlines, scene specs, editorial, roadmaps, blog
  non-prose) · `prose:` (human-only prose paths).
  `prose:` commits are **pure** — they touch only human-only paths,
  nothing else, and are signed `DRAFTS=1` by the author. The pre-commit
  hook enforces purity both ways; the result is a clean human-authorship
  ledger in git history.
- Slugs are stable and meaningful; never encode order or version in
  filenames. Order lives in `outline.md`; versions live in git tags and
  `archive/`.
- Dates in canon are in-world dates; dates in process docs are absolute
  real dates.
- Binary media lives in `assets/`, named by owning slug; rights ride in
  the referencing doc's `media:` block. Web-scraped reference images
  default `license: reference-only` and are never exported.
- Interview material: consent block governs; nothing unconsented reaches
  `publish/`.
