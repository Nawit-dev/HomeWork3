from .base_page import BasePage
from browser.browser import Browser
from elements.button import Button
from elements.multy_web_element import MultiWebElement

"""Задание 9"""


class PageDynamicContent(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    IMG = "//div//div[{}]//img"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Button(browser, self.UNIQUE_ELEMENT_LOC, description="unique_element")
        self.img = MultiWebElement(browser, self.IMG, description="img")

    def refresh_until_images_match(self) -> bool:
        """Обновляем страницу до тех пор, пока
        любых два изображения из трех не будут
        совпадать
        """
        while True:
            img_list = self.img
            src_list = []
            for img in img_list:
                src_list.append(img.get_attribute('src'))
            if len(set(src_list)) < len(src_list):
                return True
            self.browser.refresh_page()