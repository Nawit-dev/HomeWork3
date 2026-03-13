from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""Задание 1"""


class MainPage:
    TIMEOUT = 10
    TEXT = (By.XPATH, "//*[@id='content']//p")

    def __init__(self, driver):
        self.driver = driver

    def get_text(self):
        text_from_page = WebDriverWait(self.driver, MainPage.TIMEOUT).until(
            ec.presence_of_element_located(MainPage.TEXT))
        return text_from_page.text
