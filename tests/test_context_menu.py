from pages.main_page_contex_menu import MainPageContexMenu

"""Задание 4"""


def test_context_menu(open_page_context_menu):
    true_text_alert = "You selected a context menu"

    driver = MainPageContexMenu(open_page_context_menu)
    driver.check_page_load()
    text_alert = driver.right_click_box()
    assert text_alert == true_text_alert, f"Текущий результат {text_alert}, ожидаемый результат {true_text_alert}"
