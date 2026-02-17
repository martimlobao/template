# Agent Skill Framework

This repository centralizes reusable AI agent skills under `.agents/skills`.

To keep skills portable across tools, create tool-specific `skills` paths as
symlinks to `.agents/skills`:

- `.codex/skills -> ../.agents/skills`
- `.claude/skills -> ../.agents/skills`

Add new skills as:

```text
.agents/skills/<skill-name>/SKILL.md
```

Use optional `references/`, `scripts/`, and `assets/` folders when needed.
