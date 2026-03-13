from pages.main_page_fork_dynamic_content import MainPageDynamicContent


def test_dynamic_content(open_page_fork_dynamic_content):
    test = MainPageDynamicContent(open_page_fork_dynamic_content)
    test.check_page_load()
    result = test.refresh_page()
    assert result is True, f"Фактический результат {result}"
