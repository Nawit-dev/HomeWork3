from browser.browser import Browser
from elements.button import Button


"""Задание 3"""


class AlertScriptConstants:
    ALERT = "alert('I am a JS Alert')"
    CONFIRM = "confirm('I am a JS Confirm')"
    PROMPT = "prompt('I am a JS prompt')"


class MainPageJS:
    BUTTON_JS_ALERT = "//button[@onclick='jsAlert()']"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.button_js_alert = Button(browser, MainPageJS.BUTTON_JS_ALERT)

    def check_page_load(self) -> None:
        """Ждем появления кнопки на стр"""
        self.button_js_alert.wait_for_clickable()

    def alert_js(self) -> str:
        """Вызываем alert через js и получает текст alert"""
        self.browser.execute_script(AlertScriptConstants.ALERT)
        text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text

    def confirm_js(self) -> str:
        """Вызываем confirm через js и получает текст confirm"""
        self.browser.execute_script(AlertScriptConstants.CONFIRM)
        text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text

    def prompt_js(self, random_text) -> str:
        """Вызываем prompt через js и получает текст prompt"""
        self.browser.execute_script(AlertScriptConstants.PROMPT)
        self.browser.send_keys_alert(random_text)
        text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text
