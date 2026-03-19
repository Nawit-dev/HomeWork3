from browser.browser import Browser
from elements.base_elements import BaseElement
from selenium.webdriver.common.by import By


class MainPage:

    TEXT = (By.XPATH, "//*[@id='content']//p")

    def __init__(self, browser: Browser):
        self.browser = browser
        self.text_element = BaseElement(browser, self.TEXT, description="Main text")

    def get_text(self):
        self.text_element.wait_for_presence()
        return self.text_element.get_text()



