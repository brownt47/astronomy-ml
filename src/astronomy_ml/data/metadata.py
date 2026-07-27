from pathlib import Path
from PIL import Image

from astronomy_ml.data.formats import FITS_EXTENSIONS

def extract_metadata(path: Path)-> dict:

    if path.suffix.lower() in FITS_EXTENSIONS:
        return _extract_fits_metadata(path)

    return _extract_standard_metadata(path)

def _extract_standard_metadata(path: Path) -> dict:
    with Image.open(path) as image:
            metadata = {
                "width": image.width,
                "height": image.height,
                "mode": image.mode,
                "format": image.format,
            }

    return metadata

def _extract_fits_metadata(path: Path) -> dict:
         raise NotImplementedError