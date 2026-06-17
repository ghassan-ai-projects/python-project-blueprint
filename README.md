# Python Project Blueprint

Production-ready scaffolding for Python projects that expect humans and coding agents to work in the same repository.

This template gives agents a crisp operating contract, gives humans reproducible quality gates, and keeps the two aligned through `AGENTS.md`, `uv`, `ruff`, `mypy`, `pytest`, pre-commit hooks, CI, and a small set of bridge files.

## What's Included

This repository is a template, not an application. Fork it, replace the project identity, add your Python code, and keep the quality gates intact.

It includes:

- `AGENTS.md` - the canonical instructions for agents and humans; Codex reads this natively.
- `.agents/context/` - small, task-targeted context files for project, architecture, testing, style, and review.
- `.agents/prompts/` - reusable prompts for planning, implementation, review, feature work, and bugfixes.
- `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` - thin bridge files that point popular agents at the canonical instructions.
- `pyproject.toml` - package metadata, build backend, dependency groups, and tool configuration.
- `Makefile` - reproducible local commands for daily development and CI parity.
- `.pre-commit-config.yaml` - local hooks for formatting, linting, typing, and file hygiene.
- `.github/workflows/ci.yml`, `.github/dependabot.yml` - GitHub Actions pipeline and dependency update automation.
- `src/` and `tests/` - a minimal typed package and test so the template is green from day one.

## Why

Most Python repositories drift into avoidable inconsistency: mixed tooling, weak typing expectations, unclear project layout, no shared test discipline, and agent instructions that are either vague or duplicated across tools.

This blueprint makes the contract explicit:

- Agents read one canonical instruction file before editing.
- Agents can then load only the smallest relevant `.agents/context/*.md` file instead of re-reading the full policy surface.
- Humans get a short setup checklist and reproducible commands.
- `uv`, `ruff`, `mypy`, `pytest`, and CI enforce what prose alone cannot.
- Tool-specific files stay tiny and delegate to `AGENTS.md`, avoiding drift.

## Tooling Choices

This template uses current Python community defaults that are both high quality and widely adopted:

- `uv` for fast environment and dependency management
- `hatchling` as a modern build backend
- `src/` layout per Python packaging guidance
- `pytest` with `--import-mode=importlib` for new projects
- `ruff` for formatting and linting
- `mypy --strict` for type safety
- `pre-commit` for local hygiene

## Quick Start

Prerequisites:

- `uv`
- Python 3.12+ (or let `uv` manage Python for you)

Setup:

```bash
git clone https://github.com/your-org/python-project-blueprint.git
cd python-project-blueprint
uv sync --group dev
uv run pre-commit install
make ci-check
```

Then replace the template placeholders called out in `AGENTS.md`, `README.md`, `pyproject.toml`, and `src/python_project_blueprint/`.

## Quality

```bash
make ci-check
make format-check
make lint
make typecheck
make test
make test-cov
make build
```

CI runs the same core quality gates on a Python version matrix.

## For Coding Agents

Read [AGENTS.md](AGENTS.md) before editing. It contains the entrypoint rules and points to the smaller context files under `.agents/context/` for architecture, testing, style, and review.

## License

MIT - see [LICENSE](LICENSE).
