---
type: readme
---
# research/

Story research feeding [world/](../world/README.md). Craft and process
reading lives in [process/reading/](../process/reading/) instead.

## Types

| Folder | Holds | Epistemics | Template | Skill |
|---|---|---|---|---|
| `notes/` | verifiable claims | `status: unverified \| verified \| disputed`; sources required; `verified` needs two lenses; `last-reviewed` horizon | [research-note](../templates/research-note.md) | `/research` |
| `streams/` | standing intent for a body of notes | questions and coverage intent only; coverage is derived from note frontmatter | [research-stream](../templates/research-stream.md) | `/research` (per cell) |
| `interviews/` | testimony from real people | consent block governs all use; corroborates, never verifies alone | [interview](../templates/interview.md) | `/interview` |
| `explorations/` | dimensions & theses for candidate world entities | positions, argued multi-sided; nothing binds | [exploration](../templates/exploration.md) | `/explore` |
| `backlog/` | research work to do | intake — `research#NNNN` | [backlog-item](../templates/backlog-item.md) | — |

Canon entry: [canon-lifecycle.toml](../process/workflows/canon-lifecycle.toml)
— findings → [world/backlog/](../world/backlog/) → DR, or exploration →
distillation → `proposed` → DR. Nothing lands as canon directly.

## Notes — subject bins

Controlled vocabulary for the `subjects:` field (multi-valued; extend
this table deliberately):

| Bin | Scope |
|---|---|
| culture | customs, arts, food, daily life, games |
| history | events, eras, collective memory |
| demographics | population, family structure, internal migration |
| diaspora | Korean populations abroad — by wave (`waves:` registry below) |
| government-politics | state, policy, law, geopolitics |
| economy | macro, labor, class, housing |
| industries | specific sectors — shipping, tech, entertainment… |
| climate | environment, climate futures, disasters |
| religion | practice, institutions, syncretism |
| social-issues | education, gender, generational conflict |
| language | usage, dialect, romanization, naming |
| technology-science | present capabilities and near-future trajectories |

## Notes — periods

Controlled vocabulary for `periods:` (multi-valued; DR-0017). Keyed to
rupture years shared across the peninsula where possible; labels after
1961 describe the South. North-specific periodization enters by DR
when North research begins. `near-future` is bounded only when
world#0003 resolves (constraints recorded there).

| Key | Span | Rupture |
|---|---|---|
| pre-1910 | Joseon, Korean Empire | background only |
| colonial | 1910–1945 | annexation → liberation |
| division-war | 1945–1953 | liberation, division, war → armistice |
| postwar | 1953–1961 | Rhee, April Revolution, Chang Myon → coup |
| developmental | 1961–1987 | Park, Yushin, Chun → June Struggle |
| democratization | 1987–1997 | direct elections, globalization → IMF crisis |
| imf-era | 1997–2008 | restructuring, neoliberal turn → financial crisis |
| platform-era | 2008–present | smartphones, K-wave, demographic cliff, Sewol, candlelight |
| near-future | after divergence | bounded by the DR resolving world#0003 |

`cohorts:` (optional) tags lived experience by birth decade: `b1930s`
… `b2020s`. Era tags events; cohort tags who lived them.

## Notes — diaspora waves

Controlled vocabulary for `waves:`, used only when `diaspora` is among
the subjects (DR-0017):

| Key | Who |
|---|---|
| zainichi | Japan — colonial-era migration and the postwar remainder |
| koryo-saram | Russian Far East → 1937 deportation to Central Asia |
| chosonjok | Manchuria / Yanbian — 19th c. and colonial-era settlement |
| early-us | 1903–05 Hawaii plantation labor, picture brides |
| postwar-us | military spouses, students, post-1965 Immigration Act |
| germany-guest-workers | miners and nurses, 1963–77 |
| latin-america | 1960s agricultural emigration — Brazil, Argentina, Paraguay |
| adoptees | international adoption, 1953– |
| defectors | 탈북민, 1990s– |
| recent-skilled | 1990s– emigration, study abroad, return migration |

## Notes — lenses

Controlled vocabulary for `lenses:` — the *kinds* of evidence a note
draws on (DR-0017). `verified` requires corroboration from at least
two lenses; two sources of one kind are one lens.

| Key | Evidence | Discipline |
|---|---|---|
| numbers | official statistics | each citation carries agency, series, unit, coverage, definition changes, retrieval date |
| scholarship | peer-reviewed work, academic reviews | |
| media | journalism, general media | never verifies alone |
| testimony | interviews, oral history, memoir, archival primary documents | consent governs; never verifies alone |
| artifacts | film, fiction, music, games as cultural memory | evidence of how an era is remembered, not of what happened |

Korean-language sources are sought for every cell before it counts as
covered; the note's Method section records languages searched
(researcher ethic, bias review — DR-0016).

## Streams — open

Standing research programs (intent, not inventory — notes self-locate
via `streams:`):

| Stream | Anchor |
|---|---|
| [history](streams/history.md) | world#0003, ddakji#0001 |
| [demographics](streams/demographics.md) | ddakji#0001, world#0003 |
| [diaspora](streams/diaspora.md) | ddakji#0001, baek-il#0002 |
| [government-politics](streams/government-politics.md) | world#0003 |
| [economy](streams/economy.md) | ddakji#0001 |
| [industries](streams/industries.md) | ddakji#0001, world#0002 |
| [climate](streams/climate.md) | world#0003 |
| [religion](streams/religion.md) | baek-il#0002 |
| [social-issues](streams/social-issues.md) | ddakji#0002 |
| [language](streams/language.md) | world#0003 |
| [technology-science](streams/technology-science.md) | world#0002 |
| [culture](streams/culture.md) | world#0001, baek-il#0002 |

## Interviews — coverage targets

Author-curated sampling frame (intent, not inventory — what testimony
we seek):

| Target | Why |
|---|---|
| family memory & 백일 traditions | anchors [baek-il#0002](../works/baek-il/backlog/0002-baek-il-meaning.md) |
| generational / diaspora experience | the epic's spine |
| *(extend as the story's needs emerge)* | |

## Explorations — open territories

Anchored to stable backlog IDs (intent, not inventory):

| Territory | Anchor |
|---|---|
| inheritance, fate & the ddakji game | [world#0001](../world/backlog/0001-ddakji-motif.md) |
| what 백일 anchors thematically | [baek-il#0002](../works/baek-il/backlog/0002-baek-il-meaning.md) |

## Roles

| Role | Applies to |
|---|---|
| [researcher](../process/roles/researcher.md) | all work here — evidence, consent, found-vs-invented labeling |
| [dramaturg](../process/roles/dramaturg.md) | explorations — thinking partner; conclusions are the author's |

## Media

Reference media → [assets/](../assets/), recorded in the referencing
doc's `media:` block with source and license; scraped material defaults
`reference-only` and never publishes.
