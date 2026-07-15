from pathlib import Path
import sys


if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.config import DATASET_FILE
from src.dataset_builder import load_dataset, save_dataset
from src.modeling import train_and_evaluate


def main() -> None:
    if not DATASET_FILE.exists():
        save_dataset(DATASET_FILE)
    else:
        load_dataset(DATASET_FILE)

    metrics = train_and_evaluate(DATASET_FILE)
    print("Training complete")
    for key, value in metrics.items():
        if key == "top_features":
            continue
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
