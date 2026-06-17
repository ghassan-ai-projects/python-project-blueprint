# Testing Context

## Authoritative Commands

Use these commands unless the task is documentation-only:

- `uv sync --group dev`
- `make hooks`
- `make ci-check`
- `make test`
- `make typecheck`
- `make lint`
- `make build`
- `git diff --check`

## Template-Specific Behavior

- `pytest` is configured with `--import-mode=importlib`, which pytest recommends for new projects.
- Coverage is part of the default pytest run.
- `mypy` runs in strict mode by default.
- `ruff` handles both formatting and linting.
- Installed pre-commit hooks run formatting, linting, and typing checks on commit, then tests and builds on push.

## Test Quality Bar

For production-code changes:

- write a failing or expectation-setting test before implementation when feasible
- add or update `test_*.py` files in every modified package area
- cover new public behavior and meaningful branches
- keep tests typed and readable
- use pytest fixtures such as `tmp_path`, `monkeypatch`, and parametrization when they clarify intent
- avoid network calls in unit tests

If test-first is not feasible:

- say why explicitly in the plan or handoff
- still add the proving test in the same change
- make sure the test demonstrates the behavior change, not just execution

For documentation-only changes:

- run the narrowest useful checks
- still run `git diff --check`
- explain skipped commands in the final handoff

## Failure Handling

- Fix failures caused by your changes before stopping.
- If a command fails for an existing repo issue or environment restriction, say so clearly and do not misreport it as validated.
