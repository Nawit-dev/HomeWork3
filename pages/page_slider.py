from .base_page import BasePage
from browser.browser import Browser
from elements.slider import Slider
from elements.label import Label

"""Задание 5"""


class PageSlider(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    SLIDER = "//input[@type='range']"
    NUMBER_SLIDER = "range"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.slider = Slider(browser, self.SLIDER, description="btn slider")
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="unique element")
        self.number_slider = Label(browser, self.NUMBER_SLIDER, description="text number slider")

    def change_number_slider(self, steps) -> None:
        """Устанавливаем случайное значение слайдера"""
        self.slider.click()
        self.slider.move_slider_left(steps)

    def get_number_slider(self) -> float:
        """Получаем номер слайдера"""
        number = self.number_slider.get_text()
        result = float(number)
        return result
