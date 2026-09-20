from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.dataset_io import load_content_collections
from src.failure_analysis import create_failure_analysis_report


def main() -> None:
    contents = load_content_collections(Path("data/limits_dataset.json"))
    report = create_failure_analysis_report(contents, Path("reports/baselines"))
    print(f"json: {report.analysis_json}")
    print(f"markdown: {report.analysis_md}")


if __name__ == "__main__":
    main()
