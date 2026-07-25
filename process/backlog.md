---
type: backlog
scope: process
---
# Process backlog

Open process questions. Fed by retros; resolved via SDR (`scope: process`).

- [ ] **Web deployment & extraction** — when deploying `web/`, hosting
  providers get the whole repo at build time (manuscript exposure).
  Decide: extract `web/` to its own repo consuming `publish/`, or
  restrict deploy paths. (Raised 2026-07-25; decide before first deploy.)
- [ ] **Container recipe for tool #2** — read-only bind-mount setup for
  non-Claude agent tools, plus `tools/check-policy` adapter-drift lint.
  (Trigger: adopting a second agent tool.)
- [ ] **Generated timeline** — switch `world/timeline.md` from manual to
  generated view over `world/events/` once events accumulate.
- [ ] **Publishing format for submission** — standard manuscript format
  export variant, when querying begins.
- [ ] **Decisions index** — generated `decisions/README.md` grouped by
  scope, once the log is long enough to need it.
