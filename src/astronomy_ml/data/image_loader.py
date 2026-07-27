from pathlib import Path
from PIL import Image
from astropy.io import fits
import numpy as np

def load_image(path: Path) -> np.ndarray:
    """Load an image from disk"""

    if path.suffix.lower() in {".jpg",".jpeg",".png"}:
        return _load_standard_image(path)
    elif path.suffix.lower() in {".fits",".fit",".fts"}:
        return _load_fits_image(path)
    
def _load_standard_image(path: Path) -> np.ndarray:
    if not path.exists():
        raise FileNotFoundError(f"Image does not exist: {path}")

    with Image.open(path) as image:
        image_array = np.asarray(image.copy())
        return image_array

def _load_fits_image(path: Path) -> np.ndarray:
    if not path.exists():
        raise FileNotFoundError(f"Image does not exist: {path}")
    
    with fits.open(path) as hdul:
        image_array = np.asarray(hdul[0].data)
                  
        return image_array



