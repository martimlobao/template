# Template Bootstrap Instructions (One-Time)

> [!IMPORTANT]
> This file contains one-time bootstrap instructions for repositories created
> from the template. Apply this workflow before standard feature work, then
> delete this file when complete (unless the repository name is `template`,
> where this file must be ignored and preserved).

## Purpose

Use this bootstrap workflow to adapt template scaffolding to the real project
before implementing features.

Bootstrap goals:

- Detect template placeholders and default scaffold content.
- Ask the user for canonical naming values before any rename edits.
- Apply a full placeholder rename sweep across code, tests, docs, and config.
- Require explicit user confirmation before deleting template-only
  functions/tests.
- Run full quality checks after bootstrap changes.

## Trigger and Scope

Run bootstrap when this file exists in a repository whose basename is not
`template`.

Template-marker scan must include, at minimum:

- Package/module placeholders such as `foobar` references and imports.
- Default metadata or docs text (for example, `All things foobar`).
- Scaffold scripts or placeholder entrypoints (for example, hello-world
  functions).
- Scaffold tests and template-only references.

## Mandatory Workflow

1. Scan the repository for template markers and report findings.
2. Ask the user for canonical naming values before editing:
    - project display name
    - Python package/module name
    - CLI/script names
    - app/service names
    - author/org metadata (if needed)
3. Apply a full rename sweep consistently across:
    - `pyproject.toml`
    - `README.md`
    - `src/**`
    - `tests/**`
    - relevant instruction docs
4. Identify template-only functions/tests and propose removals. Do not delete
   anything without explicit user confirmation.
5. Run required quality checks:
    - `make fix`
    - `make lint`
    - `make typecheck`
    - `make test`
6. Report a concise bootstrap summary:
    - renames applied
    - removals proposed/performed
    - unresolved follow-ups
7. Delete `BOOTSTRAP.md` after completing bootstrap in non-`template` repos.

## Guardrails

- Never infer-and-apply canonical names without asking first.
- Never auto-delete placeholder functions/tests.
- Never skip quality checks after bootstrap modifications.
