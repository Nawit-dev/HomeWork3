from browser.browser import Browser
from elements.label import Label

"""Задание 9"""


class MainPageDynamicContent:
    LINK = "//a[@href='https://github.com/tourdedave/the-internet']"
    IMG = "//div[contains(@class, 'large-2 columns')]//img"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.link = Label(browser, MainPageDynamicContent.LINK)
        self.img = Label(browser,MainPageDynamicContent.IMG)

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        self.link.wait_for_presence()

    def refresh_page(self) -> bool:
        """Обновляем страницу до тех пор, пока
        любых два изображения из трех не будут
        совпадать
        """
        while True:
            img_list = self.img.wait_for_all_presence()
            src_list = []
            for img in img_list:
                src_list.append(img.get_attribute('src'))
            if src_list[0] == src_list[1] or src_list[0] == src_list[2] or src_list[1] == src_list[2]:
                return True
            self.browser.refresh_page()
