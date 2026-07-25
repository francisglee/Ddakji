---
type: readme
---
# web/ — site code

Hosts published content on the web. Not yet initialized — framework
choice is deferred until publishing begins.

Two rules bind whatever gets built here (AGENTS.md Access Policy):

1. **Reads `publish/` directories ONLY** — never `drafts/`, `scenes/`,
   `world/`, or `research/`. The exporter is the single aperture.
2. **Self-contained ecosystem**: own `package.json`, lockfile, and
   configs; nothing here leaks into the writing pipeline's tooling.

Before first deploy, resolve the process backlog item on deployment:
hosting providers get the whole repo at build time — extract this
folder to its own repo consuming `publish/`, or restrict deploy paths.
