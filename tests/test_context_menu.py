from pages.main_page_contex_menu import MainPageContexMenu

"""Задание 4"""
LINK_SITE3 = "https://the-internet.herokuapp.com/context_menu"


def test_context_menu(test_driver):
    true_text_alert = "You selected a context menu"
    test_driver.get(LINK_SITE3)
    test = MainPageContexMenu(test_driver)
    test.check_page_load()
    text_alert = test.right_click_box()
    assert text_alert == true_text_alert, f"Текущий результат {text_alert}, ожидаемый результат {true_text_alert}"
