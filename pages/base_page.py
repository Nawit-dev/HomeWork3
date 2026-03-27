from browser.browser import Browser
from logger.logger import Logger


class BasePage:
    UNIQUE_ELEMENT_LOC = None

    def __init__(self, browser: Browser):
        self.browser = browser
        self.unique_element = None

    def wait_page_load(self):
        Logger.info(f"{self}: wait for page load - waiting for {self.unique_element}")
        self.unique_element.wait_for_presence()

