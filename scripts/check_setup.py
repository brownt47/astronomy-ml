from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_DIR))

from astronomy_ml.config import CONFIG_DIR, DATA_DIR, LOG_DIR


def main():
    print(f"Project root: {PROJECT_ROOT}")
    print(f"Data folder: {DATA_DIR}")
    print(f"Config folder: {CONFIG_DIR}")
    print(f"Log folder: {LOG_DIR}")


if __name__ == "__main__":
    main()