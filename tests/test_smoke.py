from __future__ import annotations

from python_project_blueprint import project_name


def test_project_name() -> None:
    assert project_name() == "python-project-blueprint"
