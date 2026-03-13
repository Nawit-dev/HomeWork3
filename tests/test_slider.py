from pages.main_page_slider import MainPageSlider
import random

"""Задание 5"""


def test_slider(open_page_slider):
    driver = MainPageSlider(open_page_slider)
    driver.check_page_load()
    steps = random.randint(1, 4)
    driver.change_number_slider(steps)
    number_slider = driver.get_number_slider()
    assert number_slider > 0 or number_slider < 5, f"Фактический результат {number_slider}"

