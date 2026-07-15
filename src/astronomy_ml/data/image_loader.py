from pathlib import Path
from PIL import Image

def load_image(path: Path) -> Image.Image:
    """Load an image from disk"""

    if not path.exists():
        raise FileNotFoundError(f"Image does not exist: {path}")

    with Image.open(path) as image:
        return image.copy()