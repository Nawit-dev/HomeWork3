from browser.browser import Browser
from elements.button import Button

"""Задание 7"""


class MainPageWindows:
    LINK = "//a[@href='/windows/new']"
    TEXT_NEW_TAB = "//h3[contains(text(),'New Window')]"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.button_link = Button(browser, MainPageWindows.LINK)
        self.first_window = self.browser.current_window_handle()
        self.second_window = None
        self.third_window = None

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        self.button_link.wait_for_visible()

    def open_new_tabs(self) -> tuple[str, str]:
        """Открываем новую вкладку и получаем текст"""

        self.button_link.click()

        handles = self.browser.get_current_windows()
        for handle in handles:
            if handle not in [self.first_window, self.second_window]:
                self.third_window = handle
            elif handle != self.first_window and self.second_window is None:
                self.second_window = handle

        # переключаемся на новую вкладку
        target_window = self.third_window or self.second_window
        self.browser.driver.switch_to.window(target_window)

        text_new_tab = Button(self.browser, self.TEXT_NEW_TAB).wait_for_presence().text
        title = self.browser.driver.title
        return text_new_tab, title

    def back_to_original_window(self) -> None:
        """Возвращаемся на первую вкладку"""
        self.browser.switch_to_window_handle(self.first_window)
        self.button_link.wait_for_clickable()

    def close_tabs(self) -> None:
        """Закрываем дополнительные вкладки"""
        handles = self.browser.get_current_windows()
        for win in [self.third_window, self.second_window]:
            if win and win in handles:
                self.browser.switch_to_window_handle(win)
                self.browser.close()
        self.browser.switch_to_window_handle(self.first_window)
