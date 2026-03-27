from pages.page_scroll import PageScroll

"""Задание 9"""

LINK_SITE9 = "http://the-internet.herokuapp.com/infinite_scroll"


def test_scroll(test_driver):
    age_engineer = 3

    test_driver.get(LINK_SITE9)
    scroll_page = PageScroll(test_driver)
    scroll_page.wait_page_load()
    len_paragraphs = scroll_page.scroll_page(age_engineer)
    assert len_paragraphs == age_engineer, f"Фактический результат {len_paragraphs}, Ожидаемый результат {age_engineer}"
