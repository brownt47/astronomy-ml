from pathlib import Path

import pytest
import numpy as np
from PIL import Image
from astropy.io import fits



from astronomy_ml.data.image_loader import load_image


def test_load_image_raises_for_missing_file(tmp_path: Path) -> None:
    nonexistent_image = tmp_path / "missing-image.png"

    with pytest.raises(FileNotFoundError):
        load_image(nonexistent_image)

def test_load_png_image(tmp_path: Path) -> None:
    image_path = tmp_path / "test.png"

    Image.new("RGB", (100,100)).save(image_path)

    image = load_image(image_path)

    assert isinstance(image, np.ndarray)
    assert image.shape ==  (100,100, 3)


def test_load_fits_image(tmp_path: Path) -> None:
    image_path = tmp_path / "test1.fits"

    test_data = np.zeros((100, 200))
    
    hdu = fits.PrimaryHDU(data = test_data)
    hdu.writeto(image_path)

    image = load_image(image_path)

    assert isinstance(image, np.ndarray)
    assert image.shape == (100, 200)
    assert np.array_equal(image, test_data)

def test_load_fits_no_data(tmp_path: Path) -> None:
    image_path = tmp_path / "test2.fits"

    hdu = fits.PrimaryHDU()
    hdu.writeto(image_path)

    with pytest.raises(ValueError, match="Primary HDU contains no image data"):
        load_image(image_path)