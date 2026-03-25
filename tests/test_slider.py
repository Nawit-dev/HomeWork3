from pages.base_page import BasePage
from pages.page_slider import PageSlider
from elements.button import Button
import random

"""Задание 5"""

LINK_SITE4 = "https://the-internet.herokuapp.com/horizontal_slider"


class RangeSlider(BasePage):
    SLIDER = "//input[@type='range']"

    def __init__(self, browser):
        super().__init__(browser)
        self.slider = Button(browser, self.SLIDER)

    def get_min(self) -> str:
        min_value = self.slider.get_attribute("min")
        return min_value

    def get_max(self) -> str:
        max_value = self.slider.get_attribute("max")
        return max_value


def test_slider(test_driver):
    test_driver.get(LINK_SITE4)

    slider = RangeSlider(test_driver)
    slider_min = float(slider.get_min())
    slider_max = float(slider.get_max())

    slider_page = PageSlider(test_driver)
    slider_page.wait_page_load()

    steps = random.randint(int(slider_min), int(slider_max))
    slider_page.change_number_slider(steps)
    number_slider = slider_page.get_number_slider()
    assert int(slider_min) < number_slider < int(slider_max), f"Фактический результат {number_slider}"
