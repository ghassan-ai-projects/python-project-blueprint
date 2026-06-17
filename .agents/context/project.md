# Project Context

## What This Repo Is

`python-project-blueprint` is a template repository for future Python projects. The repository itself is mostly policy, automation, packaging, and scaffold rather than application logic.

The primary output of this repo is a reusable starting point with aligned agent instructions, human contribution guidance, and reproducible quality gates.

## Current State

- `pyproject.toml` still uses placeholder project metadata and URLs.
- `src/python_project_blueprint/` is a minimal typed package that keeps tooling and CI green.
- `tests/test_smoke.py` is a minimal pytest check so a fresh clone has a passing test suite once dependencies are installed.
- `README.md`, `AGENTS.md`, `Makefile`, CI, and tool config are the main assets.

## What Agents Should Optimize For

- Improve the template, not an imaginary application.
- Keep instructions concrete, short, and reviewable.
- Prefer durable repo files over long always-loaded guidance.
- Preserve parity between prose, `Makefile`, `pyproject.toml`, and CI.

## Main Risks

- Writing generic guidance that could apply to any Python repo.
- Duplicating the same rule across `AGENTS.md`, bridge files, README, and prompt files.
- Documenting commands that do not match actual template behavior.
- Assuming application architecture exists when this template is still only scaffold.
