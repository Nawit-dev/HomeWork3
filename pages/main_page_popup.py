from browser.browser import Browser
from elements.button import Button
from elements.label import Label

"""Задание 2"""


class MainPage:
    BUTTON_JS_ALERT = "//button[@onclick='jsAlert()']"
    TEXT_RESULT = "result"
    BUTTON_JS_CONFIRM = "//button[@onclick='jsConfirm()']"
    BUTTON_JS_PROMPT = "//button[@onclick='jsPrompt()']"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.button_js_alert = Button(browser, MainPage.BUTTON_JS_ALERT)
        self.button_js_confirm = Button(browser, MainPage.BUTTON_JS_CONFIRM)
        self.button_js_prompt = Button(browser, MainPage.BUTTON_JS_PROMPT)
        self.label = Label(browser, MainPage.TEXT_RESULT)

    def check_page_load(self) -> None:
        """Ждем появления кнопки на стр"""
        self.button_js_alert.wait_for_clickable()

    def click_alert(self) -> str:
        """Кликаем по кнопке которая вызывает alert и получаем текст alert"""
        self.button_js_alert.click()
        text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text

    def click_button_js_confirm(self) -> str:
        """Кликаем по кнопке которая вызывает alert и получаем текст alert"""
        self.button_js_confirm.click()
        text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text

    def click_button_js_prompt(self, random_text) -> str:
        """ Нажимаем на кнопку Click for JS Prompt и получаем текст alert"""
        self.button_js_prompt.click()
        self.browser.send_keys_alert(random_text)
        text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text

    def get_text_result(self) -> str:
        """Получаем текст из секции Result"""
        return self.label.get_text()
