from pathlib import Path
from PIL import Image

def load_image(path: Path) -> Image.Image:
    """Load an image from disk"""

    if not path.exists():
        raise FileNotFoundError(f"Image does not exist: {path}")

    return Image.open(path)