from browser.browser import Browser
from elements.button import Button


"""Задание 4"""


class MainPageContexMenu:
    BOX = "hot-spot"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.box = Button(browser, MainPageContexMenu.BOX)

    def check_page_load(self) -> None:
        """Ждем появление квадрата на стр"""
        self.box.wait_for_clickable()

    def right_click_box(self):
        """Выполняем клик пкм и открываем alert"""
        self.box.context_click_via_actions()
        return self.browser.get_alert_text()

