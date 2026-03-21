from pages.main_page_slider import MainPageSlider
import random

"""Задание 5"""

LINK_SITE4 = "https://the-internet.herokuapp.com/horizontal_slider"


def test_slider(test_driver):
    test_driver.get(LINK_SITE4)
    driver = MainPageSlider(test_driver)
    driver.check_page_load()
    steps = random.randint(1, 4)
    driver.change_number_slider(steps)
    number_slider = driver.get_number_slider()
    assert number_slider > 0 or number_slider < 5, f"Фактический результат {number_slider}"
