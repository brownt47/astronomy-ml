from pathlib import Path
from PIL import Image

def extract_metadata(path: Path)-> dict:

    with Image.open(path) as image:
        metadata = {
            "width": image.width,
            "height": image.height,
            "mode": image.mode,
            "format": image.format,
        }

    return metadata