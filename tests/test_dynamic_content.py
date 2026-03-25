from pages.page_fork_dynamic_content import PageDynamicContent

"""задание 9"""

LINK_SITE8 = "http://the-internet.herokuapp.com/dynamic_content"


def test_dynamic_content(test_driver):
    test_driver.get(LINK_SITE8)
    dynamic_content_page = PageDynamicContent(test_driver)
    dynamic_content_page.wait_page_load()
    result = dynamic_content_page.refresh_until_images_match()
    assert result, f"Фактический результат {result}"
