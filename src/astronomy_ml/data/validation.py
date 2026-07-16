from pathlib import Path
from PIL import Image


def validate_image(path: Path) -> None:
    with Image.open(path) as image:
        image.verify()