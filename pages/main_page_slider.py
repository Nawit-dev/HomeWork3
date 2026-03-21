from browser.browser import Browser
from elements.button import Button
from elements.label import Label

"""Задание 5"""


class MainPageSlider:
    HEAD_TEXT = "//*[@id='content']//h3"
    SLIDER = "//input[@type='range']"
    NUMBER_SLIDER = "range"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.button = Button(browser, MainPageSlider.SLIDER)
        self.head_text = Label(browser, MainPageSlider.HEAD_TEXT)
        self.number_slider = Label(browser, MainPageSlider.NUMBER_SLIDER)

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        self.head_text.wait_for_visible()

    def change_number_slider(self, steps) -> None:
        """Устанавливаем случайное значение слайдера"""
        self.button.click()
        self.button.move_slider_left(steps)

    def get_number_slider(self) -> float:
        """Получаем номер слайдера"""
        number = self.number_slider.get_text()
        result = float(number)
        return result
