---
type: decision-record
number: 17
scope: process
kind: improvement
status: accepted
date-created: 2026-09-26
last-updated: 2026-09-26
---
# 0017 — Research streams: eras, diaspora, lenses, method

**Description:** Deep research on Korea is organized as *streams*
(`research/streams/`), stratified by rupture-defined eras and birth
cohorts rather than decades or republics; `diaspora` becomes its own
subject bin with a wave vocabulary; every note declares its evidentiary
*lenses*, and `verified` requires two; statistical claims carry source
metadata; Korean-language sourcing is required; notes gain a Method
section so the research process is documented at the point of work.

## Context
The author is opening sustained research streams on Korea to feed the
epic before any world content is populated. The story's timing is not
yet fixed (world#0003 open), so the research frame must not presuppose
a divergence date. Three design questions arose in discussion:

1. **How to stratify time.** Decades are neutral but cut across the
   ruptures that actually shaped lives; South Korean republic eras
   cover only 1948 onward and lump 1987–present into one bin, precisely
   the period the story leans on most.
2. **Where diaspora lives.** Today it hides inside the `demographics`
   bin scope; the epic's spine is generational and diaspora experience
   (research README coverage targets), and diaspora does not stratify
   by Korean domestic eras at all — it stratifies by wave and
   destination.
3. **How to organize evidence and document the process.** The author
   proposed three lenses (statistical reporting with metadata, academic
   review, general media). The repo already treats testimony as a
   distinct epistemic type (DR-0010, DR-0011) and the researcher ethic
   ranks testimony and primary sources above LLM synthesis (DR-0016).
   Nothing today records *how* a note was produced.

DR-0011 fixed the governing constraints: taxonomy lives in metadata,
not folders; README sections record intent, never inventory; what
exists is derivable. This record extends that scheme rather than
replacing it.

## Alternatives considered
- **Stratify by decade** — rejected: arbitrary boundaries (1961, 1987,
  1997 all fall mid-decade); a note on the IMF crisis would straddle
  two bins for no gain. Calendar year remains available as a finer
  optional tag for statistical series, which are dated anyway.
- **Stratify by republic (First–Sixth)** — rejected: political
  periodization of one state; excludes colonial, wartime, and North
  Korean material; Sixth Republic (1987–) is undifferentiated for the
  story's most relevant forty years.
- **Eras as subfolders of `notes/`** — rejected per DR-0011: notes
  straddle eras; multi-valued `periods:` handles it, directories can't.
- **Eras keyed to the story's own timeline** — deferred: the divergence
  date is undecided (world#0003). Eras are keyed to real Korean history
  with a single open-ended `near-future` tail; when world#0003 resolves,
  the tail is bounded by that DR, and the historical eras are untouched.
- **No cohort axis** — rejected: the epic is multi-generational; a
  1940 birth and a 1965 birth lived the 1980s in different worlds. Era
  tags events; cohort tags lived experience. Cohorts are optional
  (`cohorts:` may be empty) so era-only notes carry no ceremony.
- **Diaspora as an axis on every bin rather than a bin** — rejected:
  diaspora is a subject with its own literature and its own
  periodization (waves); as a cross-cutting axis it would force every
  note to declare a diaspora position. It is a bin, and `waves:` is its
  own vocabulary, used only when `diaspora` is among the subjects.
- **Lenses as folders or as separate note types** — rejected: a good
  note triangulates across lenses; splitting by lens would defeat the
  purpose. Lenses are a multi-valued tag *and* a verification rule.
- **Three lenses (numbers, scholarship, media) as proposed** — extended:
  testimony/primary sources and cultural artifacts are added. The repo
  already privileges testimony; artifacts (film, fiction, song) are how
  an era is remembered, which for fiction is load-bearing evidence, not
  decoration. Omitting them would leave the two lenses most likely to
  correct outsider framing (DR-0016 bias review) outside the scheme.
- **Lenses as organization only, not a verification rule** — rejected:
  a tag that changes nothing drifts. Requiring two lenses for
  `verified` operationalizes AGENTS.md rule 10 ("testimony alone never
  verifies") into a general rule: *no single lens verifies*.
- **A research log file per stream** — rejected: it is inventory, and
  git is the log. The stream doc records intent (questions, which
  era × lens cells matter, gaps); coverage is derived by grepping note
  frontmatter (`streams:`, `periods:`, `lenses:`), and a generator is
  filed as a tooling follow-up.
- **Method recorded in a separate provenance file** — rejected: the
  method belongs with the claims it produced. A Method section in the
  note, consistent with DR-0009's reproducibility guideline (model ID,
  harness, dates; not sampling parameters).
- **Effort test (DR-0016).** Deep research streams are an expanded AI
  use. They pass the test only because the author owns the questions,
  reviews every note, and writes nothing from a note without having
  read the sources it cites; the Method section and Korean-language
  requirement make the AI's work auditable rather than a substitute for
  the author's reading. The playbook makes the author's review step
  explicit. Streams that run without author review would fail the
  test; that failure mode is named in the playbook.

## Decisions

| Decision ID | Decision | Description | Backlog ID |
|---|---|---|---|
| 0017-1 | Era vocabulary | Notes gain multi-valued `periods:` from a controlled vocabulary registered in `research/README.md`: `pre-1910`, `colonial` (1910–45), `division-war` (1945–53), `postwar` (1953–61), `developmental` (1961–87), `democratization` (1987–97), `imf-era` (1997–2008), `platform-era` (2008–present), `near-future` (after divergence; bounded when world#0003 resolves). Calendar years may be appended in free text where a series demands it | — |
| 0017-2 | Cohort axis | Notes gain optional multi-valued `cohorts:` — decade of birth, `b1930s` … `b2020s` — for material about lived experience rather than events | — |
| 0017-3 | Diaspora bin and waves | `diaspora` joins the subject-bin registry (removed from the `demographics` scope line). Notes with `diaspora` in `subjects:` declare `waves:` from a registered vocabulary: `zainichi`, `koryo-saram`, `chosonjok`, `early-us` (1903–05 Hawaii, picture brides), `postwar-us` (military spouses, students, post-1965), `germany-guest-workers` (1963–77), `latin-america` (1960s agricultural emigration), `adoptees` (1953–), `defectors` (탈북민, 1990s–), `recent-skilled` (1990s– emigration, study, return) | — |
| 0017-4 | Lenses | Notes gain multi-valued `lenses:` from a registered vocabulary: `numbers` (official statistics), `scholarship` (peer-reviewed and academic review), `media` (journalism, general media), `testimony` (interviews, oral history, memoir, archival primary documents), `artifacts` (film, fiction, music, games as cultural memory) | — |
| 0017-5 | Two-lens verification | AGENTS.md rule 10 gains: a claim is `verified` only when corroborated by sources from at least two lenses. Testimony alone never verifies (unchanged); neither does any other single lens | — |
| 0017-6 | Statistical metadata | Every `numbers` citation in References records: agency, series name/ID, unit, coverage (geography, population), known definition changes, retrieval date, URL. Template comment fixes the shape | — |
| 0017-7 | Korean-language sourcing | Each note's Method section records the languages searched; a stream is not considered covered on any era × lens cell until Korean-language sources have been sought for it. Operationalizes the researcher ethic's bias-review axiom (DR-0016) | — |
| 0017-8 | Method section | Research-note body gains `## Method` before References: questions asked, databases and queries run, languages, date, model ID and effort, what was excluded and why. Per DR-0009: model ID, provider, harness, dates; no sampling parameters | — |
| 0017-9 | Research streams | New doc type `research-stream` (template → `research/streams/`): topic, question set, `subjects:`, `periods:` and `waves:` in scope, `lenses:` required, `informs:`, `status: active \| dormant \| closed`; body = Questions, Coverage intent (which era × lens cells matter and why), Gaps. Notes gain `streams:` so coverage is derivable. Registry of open streams (intent, not inventory) in `research/README.md` | — |
| 0017-10 | Human lane | Playbook `process/playbooks/run-a-research-stream.md`: open a stream, run `/research` per cell, review each note for bias and read its sources, curation cadence, promotion of findings to `world/backlog/`. `capture-research.md` stays for one-off questions | — |
| 0017-11 | Coverage matrix tooling | Follow-up: a stats extension that renders era × lens (and wave × lens) coverage per stream from note frontmatter, flagging cells with a single lens or no Korean-language source | process#0012 |
| 0017-12 | Registry key for the current model | CONTRIBUTING.md gains `claude-fable-5-1` (model ID `claude-fable-5-1`, active 2026-09-26 – present); a model change is a new registry entry per DR-0009 | — |

### Details

**0017-1.** Era keys are dated by rupture years shared across the
peninsula where possible (1910, 1945, 1953). Labels after 1961 describe
the South; North Korean material uses the same calendar keys until a
North-specific periodization is needed, at which point it is added to
the registry by DR, not improvised. The author's standing constraints
on the eventual `near-future` tail (no active military aggression
between North and South; Kim Jong Un alive; the North's status quo
intact) are recorded on world#0003 and bind whichever DR fixes the
divergence date.

**0017-5.** "Two lenses" means two *kinds* of evidence, not two
sources of the same kind: two newspapers are one lens. A `numbers`
citation counts only with its metadata (0017-6) complete.

**0017-9.** A stream is to a set of notes what a brief is to a work:
the standing intent that individual notes serve. It never restates
findings; the notes hold those. Closing a stream is a curation act,
not a deletion.

## Consequences
- `templates/research-note.md` gains `periods:`, `cohorts:`, `waves:`,
  `lenses:`, `streams:` and a `## Method` section; the References
  comment shows the statistical-metadata shape.
- `templates/research-stream.md` created; `research/streams/` created.
- `research/README.md`: `diaspora` bin added, `demographics` scope
  narrowed, new registries for periods, cohorts, waves, lenses, and a
  Streams section listing open streams with their anchoring backlog
  IDs.
- `skills/research/SKILL.md`: filing steps gain the new fields, the
  Method section, the two-lens rule, and the Korean-language check;
  curation step re-checks lens count.
- `AGENTS.md` rule 10 amended (0017-5); Schema reference lists
  `research-stream`.
- `process/playbooks/run-a-research-stream.md` created; `README` of
  playbooks (if indexed) updated.
- `process/backlog/0012-coverage-matrix.md` filed (0017-11).
- `CONTRIBUTING.md` registry gains `claude-fable-5-1` (0017-12).
- Existing notes: none yet (`research/notes/` is empty), so no
  backfill.
- Not decided here: the divergence date, the bounding of
  `near-future`, any North-specific periodization, and the first
  streams' actual question sets — those are the streams' own content.

## Affected Files
| File | Changes Made | Decision ID | Author | Commit ID |
|---|---|---|---|---|
| [templates/research-note.md](../templates/research-note.md) | `periods:`, `cohorts:`, `waves:`, `lenses:`, `streams:`; Method section; stats-metadata shape in References comment | 0017-1 – 4, 6, 8, 9 | claude-fable-5-1 | *pending* |
| [templates/research-stream.md](../templates/research-stream.md) | new | 0017-9 | claude-fable-5-1 | *pending* |
| [research/README.md](../research/README.md) | diaspora bin; periods, cohorts, waves, lenses registries; Streams section | 0017-1 – 4, 9 | claude-fable-5-1 | *pending* |
| [research/streams/.gitkeep](../research/streams/.gitkeep) | new directory | 0017-9 | claude-fable-5-1 | *pending* |
| [skills/research/SKILL.md](../skills/research/SKILL.md) | new fields, Method, two-lens rule, Korean-language check, curation re-check | 0017-4 – 8 | claude-fable-5-1 | *pending* |
| [AGENTS.md](../AGENTS.md) | rule 10: two-lens verification; schema reference lists research-stream | 0017-5, 9 | claude-fable-5-1 | *pending* |
| [process/playbooks/run-a-research-stream.md](../process/playbooks/run-a-research-stream.md) | new — human lane for a stream | 0017-10 | claude-fable-5-1 | *pending* |
| [process/backlog/0012-coverage-matrix.md](../process/backlog/0012-coverage-matrix.md) | new entry — coverage matrix generator | 0017-11 | claude-fable-5-1 | *pending* |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | registry key `claude-fable-5-1` | 0017-12 | claude-fable-5-1 | *pending* |
