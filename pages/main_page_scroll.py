from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

"""Задание 10"""


class MainPageScroll:
    TIMEOUT = 10
    HEAD_TEXT = (By.XPATH, "//*[@id='content']//h3")
    TEXT = (By.XPATH, "//*[contains(@class, 'jscroll-added')]")

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        WebDriverWait(self.driver, MainPageScroll.TIMEOUT).until(
            ec.presence_of_element_located(MainPageScroll.HEAD_TEXT))

    def scroll_page(self) -> int:
        """скроллить до тех пор, пока количество абзацев не станет равно нужному числу"""
        while True:
            paragraphs = WebDriverWait(self.driver, self.TIMEOUT).until(
                ec.presence_of_all_elements_located(MainPageScroll.TEXT))
            if len(paragraphs) == 50:
                return len(paragraphs)
            ActionChains(self.driver).scroll_by_amount(0, 50).perform()

