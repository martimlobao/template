.PHONY: check
check: lint typecheck test

.PHONY: lint
lint:
	uv run ruff check
	uv run docformatter --check -r src tests
	uv run pylint src
	uv run bandit -r src
	uv run yamllint --strict .
	uv run rumdl check
	uv run tombi check

.PHONY: typecheck
typecheck:
	uv run mypy src tests
	uv run pyright src tests

.PHONY: test
test:
	uv run pytest

.PHONY: fix
fix:
	uv run ruff format
	uv run ruff check --fix
	uv run docformatter -r src tests
	uv run rumdl fmt
	uv run rumdl check --fix
	uv run tombi format

.PHONY: repl
repl:
	uv run ipython
