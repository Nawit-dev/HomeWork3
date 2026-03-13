from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Keys, ActionChains


"""Задание 5"""


class MainPageSlider:
    TIMEOUT = 10

    HEAD_TEXT = (By.XPATH, "//*[@id='content']//h3")
    SLIDER = (By.XPATH, "//input[@type='range']")
    NUMBER_SLIDER = (By.ID, "range")

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        WebDriverWait(self.driver, MainPageSlider.TIMEOUT).until(
            ec.presence_of_element_located(MainPageSlider.HEAD_TEXT))

    def change_number_slider(self, steps) -> None:
        """Устанавливаем случайное значение слайдера"""
        slider = WebDriverWait(self.driver, MainPageSlider.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageSlider.SLIDER))
        slider.click()
        action = ActionChains(self.driver)
        for _ in range(steps):
            action.send_keys(Keys.ARROW_LEFT)
        action.perform()

    def get_number_slider(self) -> float:
        """Получаем номер слайдера"""
        number = WebDriverWait(self.driver, MainPageSlider.TIMEOUT).until(
            ec.presence_of_element_located(MainPageSlider.NUMBER_SLIDER))
        result = float(number.text)
        return result
