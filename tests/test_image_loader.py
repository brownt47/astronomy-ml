from pathlib import Path

import pytest
from PIL import Image


from astronomy_ml.data.image_loader import load_image


def test_load_image_raises_for_missing_file(tmp_path: Path) -> None:
    nonexistent_image = tmp_path / "missing-image.png"

    with pytest.raises(FileNotFoundError):
        load_image(nonexistent_image)

def test_load_image_success(tmp_path: Path) -> None:
    image_path = tmp_path / "test.png"

    Image.new("RGB", (100,100)).save(image_path)

    image = load_image(image_path)

    assert isinstance(image, Image.Image)
    assert image.size ==  (100,100)
    assert image.mode == ("RGB")