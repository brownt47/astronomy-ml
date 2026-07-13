"""Check image discovery against the configured raw data directory."""

from astronomy_ml.config import load_config
from astronomy_ml.inventory import find_image_files
from astronomy_ml.paths import get_project_root


def main() -> None:
    """Load the project configuration and report discovered image files."""

    project_root = get_project_root()
    config = load_config(project_root / "configs" / "local.yaml")

    raw_data_dir = project_root / config["paths"]["raw_data"]

    image_files = find_image_files(raw_data_dir)

    print(f"Directory: {raw_data_dir}")
    print(f"Images found: {len(image_files)}")

    for image_path in image_files[:5]:
        print(image_path)


if __name__ == "__main__":
    main()