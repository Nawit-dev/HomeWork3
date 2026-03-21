from browser.browser import Browser
from elements.label import Label

"""Задание 10"""


class MainPageScroll:
    HEAD_TEXT = "//*[@id='content']//h3"
    TEXT = "//*[contains(@class, 'jscroll-added')]"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.head_text = Label(browser, MainPageScroll.HEAD_TEXT)
        self.text = Label(browser, MainPageScroll.TEXT)

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        self.head_text.wait_for_presence()

    def scroll_page(self, age_engineer, x: int, y: int) -> int:
        """скроллить до тех пор, пока количество абзацев не станет равно нужному числу"""

        while True:
            paragraphs = self.text.wait_for_all_presence()
            if len(paragraphs) == age_engineer:
                return len(paragraphs)
            self.text.scroll_by_amount(x, y)
