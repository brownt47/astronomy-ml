from pathlib import Path
from PIL import Image


from astronomy_ml.data.metadata import extract_metadata

def test_extract_metadata(tmp_path: Path) -> None:
    # create image object
    image_path = tmp_path / "test.png"
    Image.new("RGB", (123, 456)).save(image_path)

    metadata = extract_metadata(image_path)

    assert metadata["filename"] == "test.png"   
    assert metadata["width"] == 123
    assert metadata["height"] == 456
    assert metadata["mode"] == "RGB"
    assert metadata["format"] == "PNG"
    

                      
