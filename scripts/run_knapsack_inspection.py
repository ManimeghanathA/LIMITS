from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.dataset_io import load_content_collections
from src.knapsack_inspector import create_knapsack_inspection_report


def main() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))
    report = create_knapsack_inspection_report(contents, Path("reports/baselines"))
    print(f"json: {report.inspection_json}")
    print(f"markdown: {report.inspection_md}")


if __name__ == "__main__":
    main()
