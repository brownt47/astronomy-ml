from pathlib import Path
from typing import Any

def get_project_root() -> Path:
    """Return the root directory of the project."""

    return Path(__file__).resolve().parents[2]

def create_project_directories(
    config: dict[str, Any],
    project_root: Path,
) -> list[Path]:
    """Create configured project directories if they do not already exist."""

    created_paths = []

    for relative_path in config["paths"].values():
        full_path = project_root / relative_path
        full_path.mkdir(parents=True, exist_ok=True)
        created_paths.append(full_path)

    return created_paths