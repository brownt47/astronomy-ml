from pathlib import Path
from PIL import UnidentifiedImageError

import pytest

from astronomy_ml.data.image_loader import load_image

def test_load_image_raises_error_for_invalid_image(tmp_path: Path)-> None:
    
        # Create a file with a .jpg extension but invalid image contents.
    
    image_path = tmp_path / "not_an_image.jpg"
        
    image_path.write_text("Ceci n'est pas une pipe", encoding="utf-8")
    
    with pytest.raises(UnidentifiedImageError):
        load_image(image_path)