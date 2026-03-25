from .base_page import BasePage
from browser.browser import Browser
from elements.button import Button
from elements.label import Label

"""Задание 2"""


class PageJavascriptAlerts(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    BUTTON_JS_ALERT = "//button[@onclick='jsAlert()']"
    TEXT_RESULT = "result"
    BUTTON_JS_CONFIRM = "//button[@onclick='jsConfirm()']"
    BUTTON_JS_PROMPT = "//button[@onclick='jsPrompt()']"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="unique_element")
        self.button_js_alert = Button(browser, self.BUTTON_JS_ALERT, description="button_js_alert")
        self.button_js_confirm = Button(browser, self.BUTTON_JS_CONFIRM,
                                        description="button_js_confirm")
        self.button_js_prompt = Button(browser, self.BUTTON_JS_PROMPT, description="button_js_prompt")
        self.label = Label(browser, self.TEXT_RESULT, description="text result")

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
