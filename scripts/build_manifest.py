
from astronomy_ml.config import load_config
from astronomy_ml.paths import create_project_directories, get_project_root
from astronomy_ml.data.manifest import build_manifest

PROJECT_ROOT = get_project_root()

def main() -> None:
            
    config = load_config("configs/local.yaml")
    create_project_directories(config, PROJECT_ROOT)

    raw_dir = PROJECT_ROOT / config["paths"]["raw_data"]
    manifest_file =  PROJECT_ROOT / config["paths"]["manifests"] / "manifest.parquet"
    
    manifest = build_manifest(raw_dir)
    manifest.to_parquet(manifest_file, index=False)

    valid = manifest["is_valid"].sum()
    invalid = len(manifest) - valid

    print(f"Wrote {len(manifest)} records to {manifest_file}")
    print(f"Valid images:   {valid}")
    print(f"Invalid images: {invalid}")
        

if __name__ == "__main__":
    main()