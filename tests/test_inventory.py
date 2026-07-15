from pathlib import Path

import pytest

from astronomy_ml.data.inventory import find_image_files


def test_find_image_files_raises_for_missing_directory()-> None:
    nonexistent_image = Path("missing-image.png")

    with pytest.raises(FileNotFoundError):
        find_image_files(nonexistent_image)

def test_find_image_files_returns_supported_images(tmp_path: Path)-> None:
    image1 = tmp_path / "galaxy1.jpg"
    image1.touch()
    image2 = tmp_path / "galaxy2.png"
    image2.touch()
    image3 = tmp_path / "galaxy3.fit"
    image3.touch()
    
    images = find_image_files(tmp_path)

    assert len(images) == 3
    assert image1 in images
    assert image2 in images
    assert image3 in images

def test_find_image_files_ignores_unsupported_files(tmp_path: Path)-> None:
    file1 = tmp_path / "notes.txt"
    file1.touch()
    file2 = tmp_path / "report.pdf"
    file2.touch()
    file3 = tmp_path / "readme.md"
    file3.touch()    

    images = find_image_files(tmp_path)

    assert len(images) == 0

def test_find_image_files_empty_directory(tmp_path: Path)-> None:
    images = find_image_files(tmp_path)

    assert images == []