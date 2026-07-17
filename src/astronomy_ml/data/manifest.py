from pathlib import Path
from PIL import UnidentifiedImageError
import pandas as pd

from astronomy_ml.data.inventory import find_image_files
from astronomy_ml.data.metadata import extract_metadata
from astronomy_ml.data.schema import MANIFEST_COLUMNS

def build_manifest(image_dir: Path) -> pd.DataFrame:
    records = []
    image_files = find_image_files(image_dir)

    for image_path in image_files:
        record = {}
        record = {
                   "filepath": str(image_path),
                   "filename": image_path.name,
                   "extension": image_path.suffix.lower(),
                 }
        
        try:
            record |= extract_metadata(image_path)
            record["is_valid"] = True
            record["error_message"] = None
    
        except FileNotFoundError as error:
            record["is_valid"] = False
            record["error_message"] = str(error)
    
        except UnidentifiedImageError as error:
            record["is_valid"] = False
            record["error_message"] = str(error)
    
        except OSError as error:
            record["is_valid"] = False
            record["error_message"] = str(error)
    
        records.append(record)
    
    manifest = pd.DataFrame(records, columns=MANIFEST_COLUMNS)

    return manifest[MANIFEST_COLUMNS]

