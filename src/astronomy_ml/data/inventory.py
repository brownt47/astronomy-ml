"""Utilities for discovering image files."""

from pathlib import Path

SUPPORTED_IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".fits",
    ".fit",
    ".fts",
}


def find_image_files(directory: Path) -> list[Path]:
    """
    Recursively find supported image files beneath a directory.

    Parameters
    ----------
    directory
        Directory to search.

    Returns
    -------
    list[Path]
        Sorted list of image file paths.

    Raises
    ------
    FileNotFoundError
        If the directory does not exist.
    """

    if not directory.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    image_files = [
        path
        for path in directory.rglob("*")
        if path.is_file() and path.suffix.lower() in SUPPORTED_IMAGE_EXTENSIONS
    ]

    return sorted(image_files)