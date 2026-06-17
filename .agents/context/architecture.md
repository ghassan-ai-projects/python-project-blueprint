# Architecture Context

## Repository Architecture

This repository has two layers of architecture:

1. The current template repository.
2. The recommended architecture for projects that adopt the template.

Do not confuse them.

## Current Template Structure

- `AGENTS.md` is the canonical agent entrypoint.
- `README.md` explains what the template includes and how to adopt it.
- `pyproject.toml` defines package metadata, dependency groups, and tool configuration.
- `Makefile` defines the authoritative local commands.
- `.github/workflows/ci.yml` defines CI parity for core checks.
- `.pre-commit-config.yaml` enforces local hygiene, formatting, and typing.

## Recommended Adopted-Project Structure

- `src/<package>/`: importable application or library code
- `tests/`: pytest suites
- `docs/`: durable reference docs
- `scripts/`: operational or developer helpers when needed

Recommended package split:

- `cli.py` or `__main__.py`: CLI entrypoints
- `config.py`: settings loading and validation
- `models.py` or `domain/`: core types and validation
- `services/`: use cases and business logic
- `adapters/`: HTTP, database, filesystem, and queue integrations

## Dependency Direction

- entrypoints call services
- services depend on core types and narrow adapter interfaces
- adapters perform external I/O
- tests prove behavior from stable seams

Avoid:

- circular imports
- business logic in CLI or HTTP entrypoints
- adapter details leaking into core models
- speculative package splits with no current need
