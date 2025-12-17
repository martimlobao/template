# Agent Instructions

## Tooling & Environment

> [!IMPORTANT]
> **ALWAYS USE [`uv`](https://docs.astral.sh/uv/) EXCLUSIVELY.**
> Do **not** invoke `pip` under any circumstance. These instructions supersede
> any conflicting guidance.
<!-- -->
> [!IMPORTANT]
> **ALWAYS run the full suite of quality checks whenever making any changes.**

- The project targets **Python 3.13** and relies on [`uv`](https://docs.astral.sh/uv/) for
  dependency management, environment creation, and command execution.
- Run `uv lock` after modifying `pyproject.toml`.
- Use `uv run <command>` to execute Python entrypoints or tooling within the managed virtual
  environment.

## Mandatory Quality Checks

Before committing changes and ALWAYS when creating a PR, run the full suite of quality checks. You
can use the provided `Makefile` targets to run the quality checks:

```bash
make lint      # Ruff, Docformatter, Pylint, Bandit, Yamllint, and others
make typecheck # Mypy over src/ and tests/
make test      # Pytest test suite
```

Alternatively, execute the equivalent `uv run ...` commands directly if you need finer-grained
control.

Use `make fix` to auto-apply formatting (Ruff formatter and Docformatter) and re-run Ruff with
autofix enabled before addressing remaining lint findings.

Any changes you make will be rejected if the quality checks fail.

## Project Setup

To run the project, run any of the available commands listed in the `pyproject.toml` file. For
example, run `uv run api` to start the FastAPI server.

## Repository Layout

- Source code follows the `src/` layout (primary package lives under `src/foobar/`).
- Tests reside under `tests/` and use **pytest**.
- Tooling configuration lives alongside the project root files (e.g., `pyproject.toml`,
  `ruff.toml`, `mypy.ini`, `taplo.toml`). Refer to these files when adjusting linting or formatting
  behavior.

## Coding Guidelines

- Adhere to SOLID principles.
- Prefer explicit type hints—`mypy` treats the codebase as fully typed.
- Keep modules small and focused; shared logic should live inside the `foobar` package to ensure
  import paths remain consistent for both runtime and tests.
- When adding new dependencies, use `uv add` to add them to `pyproject.toml` (or `uv add --dev` for
  development dependencies).
- Tests should accompany new features or bug fixes; use pytest fixtures in `tests/conftest.py` to
  share setup. The required coverage is at least 80%.

## Additional Notes

- The repository currently exposes a basic CLI entrypoint; expanding to APIs or services should
  follow the same tooling conventions.
- These instructions apply to the entire repository—nested `AGENTS.md` files do not exist at the
  moment. If you add one in the future, ensure its scope is respected.
