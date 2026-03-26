from .base_page import BasePage
from browser.browser import Browser
from elements.label import Label
from elements.multy_web_element import MultiWebElement

"""Задание 9"""


class PageScroll(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    TEXT = "(//*[contains(@class,'jscroll-added')])[{}]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description='unique_element')
        self.text = MultiWebElement(browser, self.TEXT, description='text scroll elements')

    def scroll_page(self, age_engineer) -> int:
        """скроллить до тех пор, пока количество абзацев не станет равно нужному числу"""

        while True:
            paragraphs_list = list(self.text)
            last_paragraph = paragraphs_list[-1]
            if len(paragraphs_list) == age_engineer:
                return len(paragraphs_list)
            last_paragraph.scroll_into_view()
