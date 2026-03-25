import pytest

from pages.base_page import BasePage
from browser.browser import Browser
from elements.button import Button
from faker import Faker

"""Задание 3"""

LINK_SITE2 = "https://the-internet.herokuapp.com/javascript_alerts"
faker = Faker("en_US")


class AlertScriptConstants:
    ALERT = "alert('I am a JS Alert')"
    CONFIRM = "confirm('I am a JS Confirm')"
    PROMPT = "prompt('I am a JS prompt')"


class PageAlertsJS(BasePage):
    UNIQUE_ELEMENT_LOC = "//button[@onclick='jsAlert()']"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Button(browser, self.UNIQUE_ELEMENT_LOC, description="unique element")

    def alert_js(self, name_alert) -> str:
        """Вызываем alert через js и получаем текст alert"""
        self.browser.execute_script(name_alert)
        text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text


@pytest.mark.parametrize("name_alert", [(AlertScriptConstants.ALERT, "I am a JS Alert"),
                                        (AlertScriptConstants.CONFIRM, "I am a JS Confirm"),
                                        (AlertScriptConstants.PROMPT, "I am a JS prompt")])
def test_alert(test_driver, name_alert):

    test_driver.get(LINK_SITE2)

    alert_page = PageAlertsJS(test_driver)
    alert_page.wait_page_load()
    text_alert = alert_page.alert_js(name_alert[0])

    assert text_alert == name_alert[1], f"Фактический результат {text_alert}, ожидаемый результат {name_alert[1]}"  # Задание 2.2 , # Задание 2.4, # Задание 2.6

