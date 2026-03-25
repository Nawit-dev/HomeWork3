from pages.base_page import BasePage
from elements.label import Label
from browser.browser import Browser
from elements.button import Button

"""Задание 4"""


class PageContexMenu(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    BOX = "hot-spot"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="unique element")
        self.box = Button(browser, self.BOX, description='button_box')

    def right_click_box(self):
        """Выполняем клик пкм и открываем alert"""
        self.box.context_click_via_actions()
        return self.browser.get_alert_text()
