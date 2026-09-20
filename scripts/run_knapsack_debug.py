from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.dataset_io import load_content_collections
from src.knapsack_debug import create_knapsack_debug_report


def main() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))
    output = create_knapsack_debug_report(contents, Path("reports/baselines"))
    print(f"Wrote {output.debug_json}")
    print(f"Wrote {output.debug_md}")


if __name__ == "__main__":
    main()
