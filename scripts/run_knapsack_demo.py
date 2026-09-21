from __future__ import annotations

import json
import mimetypes
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.dataset import Paragraph
from src.dataset_io import load_content_collections
from src.knapsack_trace import build_knapsack_trace, manual_question, parse_manual_paragraphs
from src.semantic_features import SentenceTransformerSemanticScorer


DEMO_ROOT = PROJECT_ROOT / "web" / "knapsack_demo"
DATASET_PATH = PROJECT_ROOT / "data" / "limits_dataset.json"


class DemoState:
    def __init__(self) -> None:
        self.contents = load_content_collections(DATASET_PATH)
        self.scorer = SentenceTransformerSemanticScorer()


STATE = DemoState()


class KnapsackDemoHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/contents":
            self._json(_contents_payload())
            return
        path = DEMO_ROOT / (parsed.path.lstrip("/") or "index.html")
        if not path.resolve().is_relative_to(DEMO_ROOT.resolve()) or not path.exists():
            self.send_error(404)
            return
        content_type = mimetypes.guess_type(path)[0] or "application/octet-stream"
        data = path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/api/trace":
            self.send_error(404)
            return
        try:
            payload = json.loads(self.rfile.read(int(self.headers.get("Content-Length", "0"))))
            trace = _trace_payload(payload)
        except Exception as exc:  # pragma: no cover - defensive server boundary
            self._json({"error": str(exc)}, status=400)
            return
        self._json(trace)

    def log_message(self, format: str, *args) -> None:
        return

    def _json(self, payload, status: int = 200) -> None:
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


def _contents_payload() -> dict:
    contents = []
    for index, content in enumerate(STATE.contents, start=1):
        contents.append(
            {
                "key": f"content{index}",
                "label": f"Content {index}",
                "contentId": content.id,
                "text": "\n\n".join(paragraph.text for paragraph in content.paragraphs),
                "questions": [
                    {"id": question.id, "text": question.text, "category": question.category}
                    for question in content.questions
                ],
            }
        )
    return {"contents": contents}


def _trace_payload(payload: dict) -> dict:
    source = payload.get("source", "manual")
    budget = int(payload.get("budget", 256))
    question_text = str(payload.get("question", "")).strip()
    if not question_text:
        raise ValueError("question is required")

    if source.startswith("content"):
        content_index = int(source.replace("content", "")) - 1
        content = STATE.contents[content_index]
        paragraphs = content.paragraphs
        question = next(
            (item for item in content.questions if item.text == question_text),
            manual_question(question_text),
        )
    else:
        paragraphs = parse_manual_paragraphs(str(payload.get("content", "")))
        if not paragraphs:
            raise ValueError("content requires at least one paragraph")
        question = manual_question(question_text)
    trace = build_knapsack_trace(
        question=question,
        paragraphs=tuple(_renumber_manual(paragraphs) if source == "manual" else paragraphs),
        budget=budget,
        semantic_scorer=STATE.scorer,
    )
    trace["source"] = source
    return trace


def _renumber_manual(paragraphs: tuple[Paragraph, ...]) -> tuple[Paragraph, ...]:
    return tuple(
        Paragraph(id=f"m{index:02d}", text=paragraph.text, tokens=paragraph.tokens)
        for index, paragraph in enumerate(paragraphs, start=1)
    )


def main() -> None:
    server = ThreadingHTTPServer(("127.0.0.1", 8765), KnapsackDemoHandler)
    print("LIMITS knapsack demo: http://127.0.0.1:8765")
    server.serve_forever()


if __name__ == "__main__":
    main()
