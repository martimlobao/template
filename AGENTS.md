# Agent Instructions

## Bootstrap Handoff

> [!IMPORTANT]
> If a `BOOTSTRAP.md` file exists at the repository root, read and apply it
> before all other instructions in this file.
>
> Exception: if the current repository directory basename is exactly
> `template`, ignore `BOOTSTRAP.md` entirely and continue with normal template
> maintenance behavior. In this case, do not execute bootstrap actions and do
> not delete `BOOTSTRAP.md`.
>
> In non-`template` repositories, treat `BOOTSTRAP.md` as one-time bootstrap
> instructions and delete it after bootstrap is completed, along with the
> Bootstrap Handoff section from this file.

## Tooling & Environment

> [!IMPORTANT]
> **ALWAYS USE [`uv`](https://docs.astral.sh/uv/) EXCLUSIVELY.**
> Do **not** invoke `pip` under any circumstance.

> [!IMPORTANT]
> **ALWAYS run the full suite of quality checks whenever making any changes.**

- The project targets **Python 3.13** and uses `uv` for dependency
  management and command execution
- Run `uv lock` after modifying `pyproject.toml`
- Use `uv run <command>` to execute Python entrypoints or tooling

## Quality Checks

Before committing changes and when creating a PR, run:

```bash
make fix       # Auto-apply formatting and fixes
make lint      # Linting checks
make typecheck # Type checking
make test      # Test suite
```

Use `make fix` to auto-apply formatting before addressing remaining lint findings.

Any changes will be rejected if quality checks fail.

## Code Quality Best Practices

### Refactoring Over Patching

When code becomes complex or shows signs of spaghetti code, refactor for
clarity rather than adding patches. Shorter implementations are preferred
over longer ones. If you notice code becoming unwieldy, take time to
refactor it properly rather than applying quick fixes.

### Minimize Duplication

Look for opportunities to reduce code duplication and use modular
patterns. Extract common logic into reusable functions or modules.

### Reduce Lines of Code

Actively look for opportunities to reduce LOC without resorting to obscure
implementations. Prefer concise, readable code over verbose solutions.

### Planning

For complex changes, create detailed plans before coding, especially for multi-file refactors.
Research the codebase first using search tools to understand existing patterns and architecture.
Always ask the user for guidance on intended direction and desired outcome unless and until you are
confident in your understanding of the codebase and the user's intent. Push back if the request
does not seem possible or feasible, and propose alternative solutions if appropriate.

> [!IMPORTANT]
> Be biased towards asking more questions rather than making assumptions.

### Test-Driven Development

When implementing new features, write tests first, confirm they fail, then
implement. Iterate until all tests pass. Tests provide clear targets for
implementation.

### Codebase Understanding

Before adding new code, use search tools to understand existing patterns
and follow them. Maintain consistency with the codebase architecture and
conventions.

### Write Tests

Always write tests for new features or bug fixes. Maintain at least 80%
coverage. Use pytest fixtures in `tests/conftest.py` to share setup.

## PR Guidelines

- PR titles should follow the [semantic pull request](https://github.com/apps/semantic-pull-request)
  format: `feat: <description>`, `fix: <description>`, etc.
- Descriptions should be concise and reflect all changes in the PR, not just the last commit
- Include high-level description of main changes in the PR body

## Repository Layout

- Source code follows the `src/` layout (primary package lives under `src/<package_name>/`)
- Tests reside under `tests/` and use **pytest**
- Tooling configuration lives alongside project root files (e.g., `pyproject.toml`, `ruff.toml`)

## Coding Guidelines

- Adhere to SOLID principles
- Prefer explicit type hints—`ty` and `pyright` treat the codebase as fully typed
- Keep modules small and focused; shared logic should live inside the primary package namespace
- When adding new dependencies, use `uv add` (or `uv add --dev` for development dependencies)
