from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.benchmark import create_baseline_report
from src.dataset_io import load_content_collections


def main() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))
    report = create_baseline_report(contents, Path("reports/baselines"))
    print(f"rows: {report.rows_json}")
    print(f"summary: {report.summary_json}")
    print(f"csv: {report.rows_csv}")
    print(f"collage: {report.collage_png}")


if __name__ == "__main__":
    main()
