from browser.browser import Browser
from elements.base_elements import BaseElement
from selenium.webdriver.common.by import By


"""Задание 4"""


class MainPageContexMenu:
    TIMEOUT = 10
    BOX = (By.ID, "hot-spot")

    def __init__(self, browser: Browser):
        self.browser = browser
        self.alert = BaseElement(browser, MainPageContexMenu.BOX)

    def right_click_box(self):
        """Выполняем клик пкм и открываем alert"""
        clickable = self.alert.wait_for_visible()
        self.browser.action_chains(clickable, action_type="context_click")
        return self.browser.get_alert_text()

    # def check_page_load(self) -> None:
    #     """Ждем появление квадрата на стр"""
    #     WebDriverWait(self.driver, MainPageContexMenu.TIMEOUT).until(
    #         ec.visibility_of_element_located(MainPageContexMenu.BOX))
    #
    # def right_click_box(self) -> str:
    #     """Выполняем клик пкм и открываем alert"""
    #     clickable = WebDriverWait(self.driver, MainPageContexMenu.TIMEOUT).until(
    #         ec.visibility_of_element_located(MainPageContexMenu.BOX))
    #     action = ActionChains(self.driver)
    #     action.context_click(clickable).perform()
    #
    #     alert = WebDriverWait(self.driver, MainPageContexMenu.TIMEOUT).until(lambda d: d.switch_to.alert)
    #     text = alert.text
    #     alert.accept()
    #     return text
