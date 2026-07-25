@AGENTS.md

## Claude Code specifics

- Enforcement adapter: `.claude/settings.json` implements the Access
  Policy deny rules. Do not weaken or bypass them.
- Skills are discovered via the `.claude/skills` symlink → `skills/`.
- Personal overrides belong in `.claude/settings.local.json` (gitignored).
