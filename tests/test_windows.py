from pages.page_window import PageWindow
from pages.page_new_window import PageNewWindow

LINK_SITE6 = "http://the-internet.herokuapp.com/windows"

"""Задание 7"""


def switch_to_new_tab(browser, first_window, second_window=None):
    """Получает список вкладок и переключается на новую"""
    third_window = None
    handles = browser.get_current_windows()
    for handle in handles:
        if handle not in [first_window, second_window]:
            third_window = handle
        elif handle != first_window and second_window is None:
            second_window = handle

    # переключаемся на новую вкладку
    target_window = third_window or second_window
    browser.driver.switch_to.window(target_window)

    return second_window, third_window  # возвращаем новые окна


def get_title_new_tabs(browser) -> str:
    """Получает title новой вкладки"""
    return browser.driver.title


def back_to_original_window(browser, first_window) -> None:
    """Возвращает на первую вкладку"""
    browser.switch_to_window_handle(first_window)


def close_tabs(browser, first_window, second_window=None, third_window=None) -> None:
    """Закрывает дополнительные вкладки"""
    handles = browser.get_current_windows()
    for win in [third_window, second_window]:
        if win and win in handles:
            browser.switch_to_window_handle(win)
            browser.close()
    browser.switch_to_window_handle(first_window)


def test_windows(test_driver):
    true_text_new_window = "New Window"
    true_name_tab = "New Window"

    test_driver.get(LINK_SITE6)
    windows_page = PageWindow(test_driver)
    windows_page.wait_page_load()

    windows_new_page = PageNewWindow(test_driver)
    windows_new_page.wait_page_load()

    first_window = test_driver.get_current_window_handle()
    second_window = third_window = None

    # Первый запуск
    windows_page.open_new_tabs()
    second_window, third_window = switch_to_new_tab(test_driver, first_window, second_window)
    text_new_window = windows_new_page.get_text()
    name_tab = get_title_new_tabs(test_driver)
    back_to_original_window(test_driver, first_window)

    # Второй запуск
    windows_page.open_new_tabs()
    second_window, third_window = switch_to_new_tab(test_driver, first_window, second_window)
    text_new_window2 = windows_new_page.get_text()
    name_tab2 = get_title_new_tabs(test_driver)
    back_to_original_window(test_driver, first_window)

    # Закрываем вкладки
    windows_page.open_new_tabs()
    close_tabs(test_driver, first_window, second_window, third_window)

    assert text_new_window == true_text_new_window, f"Фактический результат {text_new_window}, ожидаемый результат {true_text_new_window}"
    assert name_tab == true_name_tab, f"Фактический результат {name_tab}, ожидаемый результат {true_name_tab}"
    assert text_new_window2 == true_text_new_window, f"Фактический результат {text_new_window2}, ожидаемый результат {true_text_new_window}"
    assert name_tab2 == true_name_tab, f"Фактический результат {name_tab2}, ожидаемый результат {true_name_tab}"
