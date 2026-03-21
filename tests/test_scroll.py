from pages.main_page_scroll import MainPageScroll

"""Задание 9"""

LINK_SITE9 = "http://the-internet.herokuapp.com/infinite_scroll"


def test_scroll(test_driver):
    age_engineer = 50
    x = 0
    y = 50

    test_driver.get(LINK_SITE9)
    test = MainPageScroll(test_driver)
    test.check_page_load()
    len_paragraphs = test.scroll_page(age_engineer, x, y)
    assert len_paragraphs == age_engineer, f"Фактический результат {len_paragraphs}, Ожидаемый результат {age_engineer}"
