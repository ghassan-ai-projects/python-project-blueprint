# Python Style Context

## Core Rules

- Use type hints for public functions, methods, and return values.
- Prefer `pathlib.Path` over ad hoc string path handling.
- Prefer dataclasses, plain classes, or simple functions over framework-heavy abstractions.
- Keep modules focused and avoid import-time side effects.
- Raise specific exceptions and wrap context only when it helps debugging.
- Prefer standard library modules before adding new dependencies.
- Prefer direct code over indirection when both are maintainable.
- Add new abstractions only after a real second use, repeated logic, or a clear testing need appears.

## Layout Rules

- Keep entrypoints thin.
- Keep business logic in `services/` or similarly named package areas.
- Keep external I/O in adapters or boundary modules.
- Keep core models and validation independent from transport details.
- Keep package names lowercase with underscores only when needed for readability.

## Naming Rules

- Use `snake_case` for functions, modules, and variables.
- Use `PascalCase` for classes.
- Use `UPPER_CASE` for constants.
- Use `test_*.py` for pytest modules.
- Keep acronyms consistent: `HTTP`, `JSON`, `URL`, `API`, `CLI`, `SQL`.

## Avoid

- broad `except Exception` without a strong reason
- hidden global state
- helper modules that save only one or two lines while hiding behavior
- "future-proof" interface layers with no current consumer need
- unrelated refactors in the same change
