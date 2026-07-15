from pathlib import Path
import sys


if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.config import DATASET_FILE
from src.dataset_builder import save_dataset


def main() -> None:
    dataset = save_dataset(DATASET_FILE)
    print(f"Dataset created at {DATASET_FILE}")
    print(f"Rows: {len(dataset)}")
    print(dataset.head(5).to_string(index=False))


if __name__ == "__main__":
    main()
