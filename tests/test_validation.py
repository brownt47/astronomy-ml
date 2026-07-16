from pathlib import Path
from PIL import Image, UnidentifiedImageError

import pytest

from astronomy_ml.data.validation import validate_image

def test_validate_image_accepts_valid_image(tmp_path: Path) -> None:
    image_path = tmp_path / "test.png"

    Image.new("RGB", (100, 100)).save(image_path)

    assert validate_image(image_path) is None

def test_validate_image_rejects_invalid_image(tmp_path: Path) -> None:
    image_path = tmp_path / "not_an_image.jpg"
        
    image_path.write_text("Ceci n'est pas une pipe", encoding="utf-8")
    
    with pytest.raises(UnidentifiedImageError):
        validate_image(image_path)

def test_validate_image_raises_for_missing_file(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing-image.png"
    
    with pytest.raises(FileNotFoundError):
        validate_image(missing_path)