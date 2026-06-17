# AGENTS.md - Python Project Blueprint

Canonical instructions for coding agents in this repository. Read this file first, then load only the context files needed for the task.

## Purpose

This repository is a Python project template. It provides:

- agent operating rules
- Python quality gates
- CI and pre-commit automation
- reusable scaffold for future Python services, CLIs, and libraries

Treat the repository itself as the product. Most changes here affect future projects that adopt this blueprint.

## Engineering Priorities

Use these priorities in order:

1. Correctness and safety.
2. Simplicity of design and implementation.
3. Test evidence for changed behavior.
4. Consistency with existing repo rules and automation.
5. Speed of implementation.

If two options both work, choose the one that is easier to read, easier to test, and easier for the next agent to extend.

## Read Order

Before editing:

1. Read this file.
2. Read [README.md](README.md).
3. Check the worktree with `git status --short`.
4. Read the smallest relevant context files under `.agents/context/`.
5. Make a short plan before editing.

Start with these context files:

- [.agents/context/project.md](.agents/context/project.md) for repository scope and current state.
- [.agents/context/architecture.md](.agents/context/architecture.md) for layout and dependency direction.
- [.agents/context/testing.md](.agents/context/testing.md) for commands and testing bar.
- [.agents/context/python-style.md](.agents/context/python-style.md) for coding conventions.
- [.agents/context/review-checklist.md](.agents/context/review-checklist.md) before handoff.

Use the prompt files under `.agents/prompts/` when the task matches them.

## For Humans Adopting This Template

Setup checklist after cloning or forking:

1. Rename the distribution in `pyproject.toml`.
2. Rename the import package under `src/`.
3. Update placeholder URLs, author metadata, and descriptions in `pyproject.toml` and `README.md`.
4. Update the package references in `tests/` and any example modules.
5. Install dependencies with `uv sync --group dev`.
6. Install the git hook with `uv run pre-commit install`.
7. Run `make ci-check` once to confirm everything is green.

Keep `AGENTS.md` canonical. Tool-specific files should bridge to it instead of duplicating rules.

## Current Repository State

- The package name is still the placeholder `python_project_blueprint`.
- The distribution name is still the placeholder `python-project-blueprint`.
- The repo uses `pyproject.toml` with `hatchling` for builds and `uv` for environment and command management.
- The `src/python_project_blueprint/` package and `tests/test_smoke.py` exist to keep lint, type check, test, and build workflows green in a fresh clone.

Do not invent application-specific architecture. If a task needs product code, either scaffold it explicitly or update the template docs and rules that govern future code.

## Operating Rules

- Keep changes scoped. Prefer the smallest coherent change that improves the template.
- Do not overwrite user changes.
- Do not add broad always-loaded instructions when a narrower context file is enough.
- Prefer straightforward solutions over clever ones.
- Do not add a new abstraction, helper, or dependency unless it removes repeated or proven complexity.
- Keep repo facts in files, not in tool-specific chat history.
- Update docs when commands, expectations, structure, or workflow change.
- For production-code changes, add or update tests in the same change.
- For production behavior changes, write the test before the implementation when feasible. If you do not, explain why in the handoff.
- Explain new dependencies, generated artifacts, workflow permission changes, and public behavior changes in the final handoff.

## Plan First

Before editing, write a short plan that covers:

- files to create or update
- why each file is needed
- validation commands
- risks or assumptions

The plan must also state:

- why the chosen approach is the simplest correct one
- what test will prove the behavior change
- whether the test can be written before implementation

Proceed without waiting only for small, obvious, low-risk changes. Pause for human review if the change is broad, destructive, security-sensitive, architectural, or dependency-changing.

## Architecture Overview

Expected layout for repositories that adopt this blueprint:

- `pyproject.toml` for package metadata and tool configuration
- `src/<package>/` for importable Python code
- `tests/` for pytest test suites
- `docs/` for durable reference docs
- `scripts/` for operational helpers when needed

Recommended package split for application logic:

- `<package>/cli.py` or `<package>/__main__.py` for CLI entrypoints
- `<package>/config.py` for settings loading and validation
- `<package>/models.py` or `<package>/domain/` for core types
- `<package>/services/` for business logic and use cases
- `<package>/adapters/` for file, database, HTTP, or queue integrations

Dependency direction:

- entrypoints call services
- services depend on core types and narrow adapter interfaces
- adapters handle external I/O
- tests verify behavior through public APIs when practical

See [.agents/context/architecture.md](.agents/context/architecture.md) for the concise version agents should actually load.

## Build, Test, and Lint

Primary commands:

- `uv sync --group dev`
- `make ci-check`
- `uv run --python 3.12 --group dev pytest`
- `uv run --python 3.12 --group dev ruff check .`
- `uv run --python 3.12 --group dev mypy src tests`
- `uv build`
- `git diff --check`
- `uv run --python 3.12 --group dev pre-commit run --all-files`

Important template behavior:

- `uv` is the expected tool for environment, dependency, and command management.
- `pytest` uses `--import-mode=importlib`, which pytest recommends for new projects.
- `mypy` runs in strict mode by default.
- `ruff` handles both formatting and linting.

See [.agents/context/testing.md](.agents/context/testing.md) for the testing and validation bar.

## Python Standards

- Add type hints to public functions, methods, and module-level constants where appropriate.
- Prefer `pathlib.Path` over stringly-typed filesystem paths.
- Use dataclasses or small explicit classes before reaching for framework-heavy abstractions.
- Raise specific exceptions and keep error messages actionable.
- Prefer standard library modules before adding new dependencies.
- Keep modules focused and side effects minimal.

See [.agents/context/python-style.md](.agents/context/python-style.md) for the repo-specific style rules.

## Forbidden Changes

- Do not add secrets, credentials, or machine-specific private data.
- Do not add network calls to unit tests.
- Do not add abstraction layers "for future flexibility" without a current concrete need.
- Do not replace direct code with indirection unless at least one current pain point is removed.
- Do not add top-level dependencies without clear justification.
- Do not create duplicate canonical agent files such as `CODEX.md`.
- Do not broaden repository instructions with vague policy that cannot be enforced or reviewed.
- Do not do unrelated refactors while touching template files.

## Definition Of Done

A task is done when:

- the requested scope is complete
- the change is specific to this repository and useful to future agents
- the chosen implementation is the simplest correct version that fits current needs
- tests and docs are updated when required
- validation commands were run at the appropriate scope
- skipped or failing checks are explained clearly
- instructions remain concise and non-duplicative

## Review Checklist

Before handoff:

1. Re-read changed files for vague or duplicated guidance.
2. Confirm `AGENTS.md` points to smaller context files instead of absorbing everything.
3. Confirm commands in docs match `Makefile`, `pyproject.toml`, and CI behavior.
4. Confirm tests were added for production-code changes.
5. Confirm complexity was justified and unnecessary abstraction was avoided.
6. Confirm tests prove the changed behavior, not just raise coverage.
7. Run the relevant validation commands and record failures accurately.
8. Summarize changed files, validation, remaining risks, and suggested next improvements.

Use [.agents/context/review-checklist.md](.agents/context/review-checklist.md) as the final self-review pass.
