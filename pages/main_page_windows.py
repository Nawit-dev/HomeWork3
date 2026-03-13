from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""Задание 6"""


class MainPageWindows:
    TIMEOUT = 10
    LINK = (By.XPATH, "//a[@href='/windows/new']")
    TEXT_NEW_TAB = (By.XPATH, "//h3[contains(text(),'New Window')]")

    def __init__(self, driver):
        self.driver = driver
        self.first_window = self.driver.current_window_handle
        self.second_window = None
        self.third_window = None

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        WebDriverWait(self.driver, MainPageWindows.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageWindows.LINK))

    def open_new_tabs(self) -> tuple[str, str]:
        """Открываем новую вкладку и получаем текст"""
        link = WebDriverWait(self.driver, MainPageWindows.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageWindows.LINK))
        new_windows_before = len(self.driver.window_handles)
        link.click()
        WebDriverWait(self.driver, MainPageWindows.TIMEOUT).until(lambda d: len(d.window_handles) > new_windows_before)
        for window in self.driver.window_handles:
            if window != self.first_window and window != self.second_window:
                self.third_window = window
            elif window != self.first_window and self.second_window is None:
                self.second_window = window

        if self.third_window:
            self.driver.switch_to.window(self.third_window)
        elif self.second_window:
            self.driver.switch_to.window(self.second_window)

        text_new_tab = WebDriverWait(self.driver, MainPageWindows.TIMEOUT).until(
            ec.presence_of_element_located(MainPageWindows.TEXT_NEW_TAB)
        ).text
        title = self.driver.title
        return text_new_tab, title

    def back_to_original_window(self) -> None:
        """Возвращаемся на предыдущую страницу"""
        self.driver.switch_to.window(self.first_window)
        WebDriverWait(self.driver, MainPageWindows.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageWindows.LINK))

    def close_tabs(self) -> None:
        """Закрываем вкладки"""
        for win in [self.third_window, self.second_window]:
            if win and win in self.driver.window_handles:
                self.driver.switch_to.window(win)
                self.driver.close()

        self.driver.switch_to.window(self.first_window)
