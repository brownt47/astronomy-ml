from pathlib import Path

from astronomy_ml.data.inventory import find_image_files
from astronomy_ml.data.image_loader import load_image

raw_dir = Path("data/raw")

images = find_image_files(raw_dir)

print(f"Found {len(images)} images")

image = load_image(images[0])

print(image)
print(image.size)
print(image.mode)