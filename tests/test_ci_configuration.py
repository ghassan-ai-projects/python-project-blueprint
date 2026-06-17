from __future__ import annotations

from pathlib import Path

REPOSITORY_ROOT = Path(__file__).resolve().parents[1]


def test_makefile_python_version_is_overridable() -> None:
    makefile = (REPOSITORY_ROOT / "Makefile").read_text(encoding="utf-8")

    assert "PYTHON ?= 3.12" in makefile
    assert "UV_RUN = uv run --python $(PYTHON) --group dev" in makefile


def test_ci_uses_matrix_python_version_for_make_targets() -> None:
    workflow = (REPOSITORY_ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")

    assert "python-version: ${{ matrix.python-version }}" in workflow
    assert "make ci-check PYTHON=${{ matrix.python-version }}" in workflow
