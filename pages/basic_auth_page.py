from pages.base_page import BasePage
from browser.browser import Browser
from elements.label import Label

"""Задание 1"""


class PageBasicAuth(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    SUCCESSFUL_AUTH_TEXT = "//*[@id='content']//p"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="unique element")
        self.text_element = Label(browser, self.SUCCESSFUL_AUTH_TEXT,
                                  description="The text of successful authorization")

    def get_text_after_basic_auth(self):
        return self.text_element.get_text()
