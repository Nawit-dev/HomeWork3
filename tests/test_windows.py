from pages.page_window import PageWindow
from pages.page_new_window import PageNewWindow
from browser.browser import Browser

LINK_SITE6 = "http://the-internet.herokuapp.com/windows"

"""Задание 7"""


class Tabs:
    LINK = "//a[@href='/windows/new']"
    TEXT_NEW_TAB = "//h3[contains(text(),'New Window')]"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.first_window = self.browser.get_current_window_handle()
        self.second_window = None
        self.third_window = None

    def switch_to_new_tab(self) -> None:
        """получает список вкладок и переключается на новую"""

        handles = self.browser.get_current_windows()
        for handle in handles:
            if handle not in [self.first_window, self.second_window]:
                self.third_window = handle
            elif handle != self.first_window and self.second_window is None:
                self.second_window = handle

        # переключаемся на новую вкладку
        target_window = self.third_window or self.second_window
        self.browser.driver.switch_to.window(target_window)

    def get_title_new_tabs(self) -> str:
        """Получает title новой вкладки"""
        title = self.browser.driver.title
        return title

    def back_to_original_window(self) -> None:
        """Возвращает на первую вкладку"""
        self.browser.switch_to_window_handle(self.first_window)

    def close_tabs(self) -> None:
        """Закрывает дополнительные вкладки"""
        handles = self.browser.get_current_windows()
        for win in [self.third_window, self.second_window]:
            if win and win in handles:
                self.browser.switch_to_window_handle(win)
                self.browser.close()
        self.browser.switch_to_window_handle(self.first_window)


def test_windows(test_driver):
    true_text_new_window = "New Window"
    true_name_tab = "New Window"

    test_driver.get(LINK_SITE6)

    windows_page = PageWindow(test_driver)
    windows_page.wait_page_load()

    windows_new_page = PageNewWindow(test_driver)
    windows_new_page.wait_page_load()

    tab = Tabs(test_driver)

    windows_page.open_new_tabs()

    tab.switch_to_new_tab()
    text_new_window = windows_new_page.get_text()
    name_tab = tab.get_title_new_tabs()

    tab.back_to_original_window()
    windows_page.open_new_tabs()

    tab.switch_to_new_tab()
    text_new_window2 = windows_new_page.get_text()
    name_tab2 = tab.get_title_new_tabs()

    tab.back_to_original_window()
    windows_page.open_new_tabs()
    tab.close_tabs()

    assert text_new_window == true_text_new_window, (f"Фактический результат {text_new_window}, "
                                                     f"ожидаемый результат {true_text_new_window}")
    assert name_tab == true_name_tab, (f"Фактический результат {name_tab}, "
                                       f"ожидаемый результат {true_name_tab}")
    assert text_new_window2 == true_text_new_window, (f"Фактический результат {text_new_window2}, "
                                                      f"ожидаемый результат {true_text_new_window}")
    assert name_tab2 == true_name_tab, (f"Фактический результат {name_tab2}, "
                                        f"ожидаемый результат {true_name_tab}")
