from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

"""Задание 8"""


class MainPageFrames:
    TIMEOUT = 10
    BTN_ACCORDION = (By.XPATH, "//div[contains(text(), 'Alerts, Frame & Windows')]")
    BTN_LIGHT = (By.XPATH, "//a[contains(@href, '/nestedframes')]")
    FRAME = (By.ID, "frame1")
    FRAME_TEXT = (By.TAG_NAME, "body")
    FRAME_TWO = (By.TAG_NAME, "iframe")
    FRAME_TWO_TEXT = (By.TAG_NAME, "p")

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        WebDriverWait(self.driver, MainPageFrames.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageFrames.BTN_ACCORDION))

    def open_nested_frames(self) -> tuple[str, str]:
        """Открываем страницу в левом меню кликаем пункт Nested Frames"""
        btn = WebDriverWait(self.driver, MainPageFrames.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageFrames.BTN_LIGHT))
        btn.click()
        time.sleep(2)
        iframe = WebDriverWait(self.driver, MainPageFrames.TIMEOUT).until(
            ec.presence_of_element_located(MainPageFrames.FRAME))
        self.driver.switch_to.frame(iframe)
        element = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.presence_of_element_located(MainPageFrames.FRAME_TEXT))
        time.sleep(2)
        self.driver.switch_to.default_content()
        iframe_two = WebDriverWait(self.driver, MainPageFrames.TIMEOUT).until(
            ec.presence_of_element_located(MainPageFrames.FRAME_TWO))
        self.driver.switch_to.frame(iframe_two)
        element_two = WebDriverWait(self.driver, self.TIMEOUT).until(
            ec.presence_of_element_located(MainPageFrames.FRAME_TWO_TEXT))

        return element.text, element_two.text
