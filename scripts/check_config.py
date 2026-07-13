from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIR))

from astronomy_ml.config import load_config
from astronomy_ml.paths import create_project_directories


def main() -> None:
    config = load_config("configs/local.yaml")
    directories = create_project_directories(config, PROJECT_ROOT)

    print(f"Project: {config['project']['name']}")
    print(f"Environment: {config['project']['environment']}")
    print(f"Sample size: {config['dataset']['sample_size']}")

    print("\nConfigured directories:")
    for directory in directories:
        print(f"  {directory}")


if __name__ == "__main__":
    main()