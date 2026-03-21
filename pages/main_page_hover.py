from browser.browser import Browser
from elements.button import Button
from elements.label import Label
import time
"""Задание 6"""


class MainPageHover:
    HEAD_TEXT = "//*[@id='content']//h3"
    IMG_XPATH = "(//div[@class='figure'])[{}]/img"

    FIGURES = "//div[@class='figure']"

    TEXT_HOVER_TEMPLATE = "//div[@class='figure'][{}]//h5"
    LINK_HOVER_TEMPLATE = "//div[@class='figure'][{}]//a"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.label = Label(browser, MainPageHover.HEAD_TEXT)

    def check_page_load(self):
        """Ждем загрузку стр"""
        self.label.wait_for_visible()

    def hover_mouse(self, index) -> str:
        """Наводим на картинку пользователя по индексу (1, 2, 3)"""
        img_xpath = self.IMG_XPATH.format(index)
        img = Button(self.browser, img_xpath)

        img.move_to_element()

        time.sleep(2)

        text_xpath = self.TEXT_HOVER_TEMPLATE.format(index)
        text_hover = Label(self.browser, text_xpath)
        return text_hover.get_text()

    def click_link_hover(self, index) -> str:
        """Переходим по ссылке пользователя по индексу"""
        link_xpath = self.LINK_HOVER_TEMPLATE.format(index)
        link = Button(self.browser, link_xpath)
        link.click()
        return self.browser.return_url()

    def go_back(self) -> None:
        """Возвращаемся на предыдущую страницу"""
        self.browser.navigate_back()
        self.check_page_load()
