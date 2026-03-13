from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""Задание 2"""


class MainPage:
    TIMEOUT = 10
    BUTTON_JS_ALERT = (By.XPATH, "//button[@onclick='jsAlert()']")
    TEXT_RESULT = (By.ID, "result")
    BUTTON_JS_CONFIRM = (By.XPATH, "//button[@onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.XPATH, "//button[@onclick='jsPrompt()']")

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self) -> None:
        """Ждем появления кнопки на стр"""
        WebDriverWait(self.driver, MainPage.TIMEOUT).until(ec.element_to_be_clickable(MainPage.BUTTON_JS_ALERT))

    def click_alert(self) -> str:
        """Кликаем по кнопке которая вызывает alert и получаем текст alert"""
        button = WebDriverWait(self.driver, MainPage.TIMEOUT).until(
            ec.element_to_be_clickable(MainPage.BUTTON_JS_ALERT))
        button.click()
        alert = WebDriverWait(self.driver, MainPage.TIMEOUT).until(lambda b: b.switch_to.alert)
        text = alert.text
        alert.accept()
        return text

    def get_text_result(self) -> str:
        """Получаем текст из секции Result"""
        text_result = WebDriverWait(self.driver, MainPage.TIMEOUT).until(
            ec.presence_of_element_located(MainPage.TEXT_RESULT))
        return text_result.text

    def click_button_js_confirm(self) -> str:
        """Нажимаем на кнопку Click for JS Confirm и получаем текст alert"""
        button = WebDriverWait(self.driver, MainPage.TIMEOUT).until(
            ec.element_to_be_clickable(MainPage.BUTTON_JS_CONFIRM))
        button.click()

        alert = WebDriverWait(self.driver, MainPage.TIMEOUT).until(lambda d: d.switch_to.alert)
        text = alert.text
        alert.accept()
        return text

    def click_button_js_prompt(self, random_text) -> str:
        """ Нажимаем на кнопку Click for JS Prompt и получаем текст alert"""
        button = WebDriverWait(self.driver, MainPage.TIMEOUT).until(
            ec.element_to_be_clickable(MainPage.BUTTON_JS_PROMPT))
        button.click()

        alert = WebDriverWait(self.driver, MainPage.TIMEOUT).until(lambda d: d.switch_to.alert)
        alert.send_keys(random_text)
        text = alert.text
        alert.accept()
        return text
