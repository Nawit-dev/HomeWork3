from pages.page_contex_menu import PageContexMenu

"""Задание 4"""
LINK_SITE3 = "https://the-internet.herokuapp.com/context_menu"


def test_expected_result(test_driver):
    true_text_alert = "You selected a context menu"
    test_driver.get(LINK_SITE3)
    expected_result_page = PageContexMenu(test_driver)
    expected_result_page.wait_page_load()
    text_alert = expected_result_page.right_click_box()
    assert text_alert == true_text_alert, f"Текущий результат {text_alert}, ожидаемый результат {true_text_alert}"
