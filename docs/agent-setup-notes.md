# Agent Setup Notes

This template follows the patterns that have become common across high-quality coding-agent repositories:

- Keep one canonical repository instruction file and make tool-specific files delegate to it.
- Treat Codex as the native `AGENTS.md` consumer; do not create a duplicate `CODEX.md`.
- Keep always-loaded instructions concise, specific, and testable.
- Put commands, architecture boundaries, security rules, and handoff expectations in durable files.
- Use hooks, CI, and linters for enforcement because instruction files guide behavior but do not guarantee it.
- Prefer narrower, path-scoped instructions or custom agents for specialized workflows.
- Use current Python community defaults that are fast and maintainable: `uv`, `ruff`, `pytest`, and `mypy`.
- Keep packaging aligned with Python packaging guidance: `pyproject.toml`, a build backend, and `src/` layout.

Useful public references:

- Python Packaging User Guide: https://packaging.python.org/
- pytest good practices: https://docs.pytest.org/en/stable/explanation/goodpractices.html
- Ruff docs: https://docs.astral.sh/ruff/
- uv docs: https://docs.astral.sh/uv/
- mypy docs: https://mypy.readthedocs.io/
- pre-commit docs: https://pre-commit.com/
- OpenAI Codex `AGENTS.md` guidance: https://developers.openai.com/codex/guides/agents-md

Maintenance guidance:

- Update `AGENTS.md` when review feedback reveals a repeated mistake.
- Remove stale instructions quickly; conflicting rules are worse than missing rules.
- Keep bridge files short. If a bridge file grows, ask whether the rule belongs in `AGENTS.md`, a path-scoped agent rule, or a workflow-specific custom agent.
- Keep CI tool installation and `pyproject.toml` configuration aligned.
- Audit `make ci-check`, `.github/workflows/ci.yml`, and the Quality section in `README.md` together so prose and automation stay aligned.
