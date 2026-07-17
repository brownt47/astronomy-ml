from pathlib import Path
from PIL import Image, UnidentifiedImageError
import pandas as pd
import pytest

from astronomy_ml.data.manifest import build_manifest

def test_build_manifest(tmp_path: Path) -> None:
    # create image object
    image_path = tmp_path / "test1.png"
    Image.new("RGB", (123, 456)).save(image_path)
    image_path = tmp_path / "test2.jpg"
    Image.new("RGB", (123, 456)).save(image_path)

    manifest = build_manifest(tmp_path)

    assert isinstance(manifest, pd.DataFrame)
    assert len(manifest) == 2
    assert "filepath" in manifest.columns
    assert "extension" in manifest.columns
    assert "is_valid" in manifest.columns
    assert "error_message" in manifest.columns


    png_row = manifest[manifest["filename"] == "test1.png"].iloc[0]
    assert png_row["filename"] == "test1.png"   
    assert png_row["width"] == 123
    assert png_row["height"] == 456
    assert png_row["mode"] == "RGB"
    assert png_row["format"] == "PNG"
    assert png_row["is_valid"] == True
    assert png_row["error_message"] is None
    
    jpg_row = manifest[manifest["filename"] == "test2.jpg"].iloc[0]
    assert jpg_row["filename"] == "test2.jpg"   
    assert jpg_row["width"] == 123
    assert jpg_row["height"] == 456
    assert jpg_row["mode"] == "RGB"
    assert jpg_row["format"] == "JPEG"
    assert jpg_row["is_valid"] == True
    assert jpg_row["error_message"] is None

                      
def test_build_manifest_invalid_image(tmp_path: Path) -> None:
    image_path = tmp_path / "bad.jpg"
        
    image_path.write_text("Ceci n'est pas une pipe", encoding="utf-8")
    
    manifest = build_manifest(tmp_path)

    row = manifest.iloc[0]

    assert isinstance(manifest, pd.DataFrame)
    assert len(manifest) == 1
    assert "filepath" in manifest.columns
    assert "extension" in manifest.columns
    assert "is_valid" in manifest.columns
    assert "error_message" in manifest.columns
    assert row["is_valid"] == False
    assert row["error_message"] is not None

