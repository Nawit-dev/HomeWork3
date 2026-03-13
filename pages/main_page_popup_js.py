from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
"""Задание 3"""


class MainPageJS:
    TIMEOUT = 10
    BUTTON_JS_ALERT = (By.XPATH, "//button[@onclick='jsAlert()']")

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self) -> None:
        """Ждем появления кнопки на стр"""
        WebDriverWait(self.driver, MainPageJS.TIMEOUT).until(ec.element_to_be_clickable(MainPageJS.BUTTON_JS_ALERT))

    def alert_js(self) -> str:
        """Вызываем alert через js и получает текст alert"""
        self.driver.execute_script("alert('I am a JS Alert')")
        alert = WebDriverWait(self.driver, MainPageJS.TIMEOUT).until(lambda b: b.switch_to.alert)
        text = alert.text
        alert.accept()
        return text

    def confirm_js(self) -> str:
        """Вызываем confirm через js и получает текст confirm"""
        self.driver.execute_script("confirm('I am a JS Confirm')")
        alert = WebDriverWait(self.driver, MainPageJS.TIMEOUT).until(lambda d: d.switch_to.alert)
        text = alert.text
        alert.accept()
        return text

    def prompt_js(self, random_text) -> str:
        """Вызываем prompt через js и получает текст prompt"""
        self.driver.execute_script("prompt('I am a JS prompt')")
        alert = WebDriverWait(self.driver, MainPageJS.TIMEOUT).until(lambda d: d.switch_to.alert)
        alert.send_keys(random_text)
        text = alert.text
        alert.accept()
        return text
