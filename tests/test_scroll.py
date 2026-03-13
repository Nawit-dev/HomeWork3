from pages.main_page_scroll import MainPageScroll


def test_scroll(open_page_infinite_scroll):
    age_engineer = 50
    test = MainPageScroll(open_page_infinite_scroll)
    test.check_page_load()
    len_paragraphs = test.scroll_page()
    assert len_paragraphs == age_engineer, f"Фактический результат {len_paragraphs}, Ожидаемый результат {age_engineer}"