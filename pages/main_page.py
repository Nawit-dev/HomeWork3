from browser.browser import Browser
from elements.label import Label

"""Задание 1"""


class MainPage:
    TEXT = "//*[@id='content']//p"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.text_element = Label(browser, self.TEXT)

    def check_page_load(self) -> None:
        """Ждем появление квадрата на стр"""
        self.text_element.wait_for_presence()

    def get_text_after_basic_auth(self):
        return self.text_element.get_text()
