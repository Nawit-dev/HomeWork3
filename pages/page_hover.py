from .base_page import BasePage
from browser.browser import Browser
from elements.button import Button
from elements.label import Label
import time

"""Задание 6"""


class PageHover(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    IMG_XPATH = "(//div[contains(@class, 'figure')])[{}]/img"

    FIGURES = "//div[contains(@class, 'figure')]"

    TEXT_HOVER_TEMPLATE = "//div[contains(@class, 'figure')][{}]//h5"
    LINK_HOVER_TEMPLATE = "//div[contains(@class, 'figure')][{}]//a"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description='unique_element')

    def hover_mouse(self, index) -> str:
        """Наводим на картинку пользователя по индексу (1, 2, 3)"""
        img_xpath = self.IMG_XPATH.format(index)
        img = Button(self.browser, img_xpath)

        img.move_to_element()

        text_xpath = self.TEXT_HOVER_TEMPLATE.format(index)
        text_hover = Label(self.browser, text_xpath)
        return text_hover.get_text()

    def click_link_hover(self, index) -> None:
        """Переходим по ссылке пользователя по индексу"""
        link_xpath = self.LINK_HOVER_TEMPLATE.format(index)
        link = Button(self.browser, link_xpath)
        link.click()

    def get_url_usr(self):
        return self.browser.get_url()

    def go_back(self) -> None:
        """Возвращаемся на предыдущую страницу"""
        self.browser.navigate_back()
