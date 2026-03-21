from pages.main_page_fork_dynamic_content import MainPageDynamicContent

"""задание 9"""

LINK_SITE8 = "http://the-internet.herokuapp.com/dynamic_content"


def test_dynamic_content(test_driver):
    test_driver.get(LINK_SITE8)
    test = MainPageDynamicContent(test_driver)
    test.check_page_load()
    result = test.refresh_page()
    assert result is True, f"Фактический результат {result}"
