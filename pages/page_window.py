from .base_page import BasePage
from elements.label import Label
from browser.browser import Browser
from elements.button import Button

"""Задание 7"""


class PageWindow(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    LINK = "//a[@href='/windows/new']"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="unique element")
        self.button_link = Button(browser, self.LINK, description="button link")

    def open_new_tabs(self) -> None:
        """Открываем новую вкладку"""
        self.button_link.click()

