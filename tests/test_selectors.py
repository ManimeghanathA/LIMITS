from src.dataset import Paragraph
from src.selectors import budget_fill_selector, keyword_overlap_selector, random_selector


def make_paragraphs() -> tuple[Paragraph, ...]:
    return (
        Paragraph("p01", "Atlas calibration starts at 06:30.", 20),
        Paragraph("p02", "The sensor cart is staged beside Hangar 2.", 25),
        Paragraph("p03", "Lunch delivery uses Bay 7.", 30),
        Paragraph("p04", "Binder Blue stores the battery printout.", 22),
        Paragraph("p05", "Unrelated catering note.", 40),
    )


def token_sum(selected: tuple[str, ...], paragraphs: tuple[Paragraph, ...]) -> int:
    by_id = {paragraph.id: paragraph for paragraph in paragraphs}
    return sum(by_id[item].tokens for item in selected)


def test_budget_fill_selector_adds_candidates_in_order_until_budget_is_full() -> None:
    paragraphs = make_paragraphs()

    selected = budget_fill_selector(paragraphs, budget=50)

    assert selected == ("p01", "p02")
    assert token_sum(selected, paragraphs) <= 50


def test_keyword_overlap_selector_prefers_query_matching_chunks_under_budget() -> None:
    paragraphs = make_paragraphs()

    selected = keyword_overlap_selector(
        query="Where is the sensor cart staged for calibration?",
        paragraphs=paragraphs,
        budget=50,
    )

    assert selected == ("p02", "p01")
    assert token_sum(selected, paragraphs) <= 50


def test_random_selector_is_seeded_and_budget_valid() -> None:
    paragraphs = make_paragraphs()

    first = random_selector(paragraphs, budget=45, seed=7)
    second = random_selector(paragraphs, budget=45, seed=7)

    assert first == second
    assert token_sum(first, paragraphs) <= 45


def test_selectors_skip_items_that_cannot_fit_budget() -> None:
    paragraphs = (
        Paragraph("p01", "Too large.", 100),
        Paragraph("p02", "Small enough.", 20),
    )

    assert budget_fill_selector(paragraphs, budget=30) == ("p02",)
    assert keyword_overlap_selector("small enough", paragraphs, budget=30) == ("p02",)
