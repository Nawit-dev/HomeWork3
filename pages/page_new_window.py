from .base_page import BasePage
from elements.label import Label
from browser.browser import Browser
from elements.button import Button

"""Задание 7"""


class PageNewWindow(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    TEXT_NEW_TAB = "//h3[contains(text(),'New Window')]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="unique element")
        self.button_link = Button(browser, self.TEXT_NEW_TAB, description="button link")

    def get_text(self) -> str:
        """Получает текст с новой стр"""
        text_new_tab = Button(self.browser, self.TEXT_NEW_TAB).wait_for_presence().text
        return text_new_tab
