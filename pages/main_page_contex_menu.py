from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

"""Задание 4"""


class MainPageContexMenu:
    TIMEOUT = 10
    BOX = By.ID, "hot-spot"

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self) -> None:
        """Ждем появление квадрата на стр"""
        WebDriverWait(self.driver, MainPageContexMenu.TIMEOUT).until(
            ec.visibility_of_element_located(MainPageContexMenu.BOX))

    def right_click_box(self) -> str:
        """Выполняем клик пкм и открываем alert"""
        clickable = WebDriverWait(self.driver, MainPageContexMenu.TIMEOUT).until(
            ec.visibility_of_element_located(MainPageContexMenu.BOX))
        action = ActionChains(self.driver)
        action.context_click(clickable).perform()

        alert = WebDriverWait(self.driver, MainPageContexMenu.TIMEOUT).until(lambda d: d.switch_to.alert)
        text = alert.text
        alert.accept()
        return text
