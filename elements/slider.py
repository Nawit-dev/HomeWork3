from selenium.webdriver import Keys, ActionChains
from logger.logger import Logger
from .input import BaseElement


class Slider(BaseElement):

    def move_slider_left(self, steps):
        """Двигаем слайдер влево на определенное кол-во шагов"""
        self.wait_for_clickable()
        actions = ActionChains(self.browser.driver)
        Logger.info(f"{self}: move slider left by {steps} steps")
        actions.send_keys(Keys.ARROW_LEFT * steps)
        actions.perform()

    def get_min(self) -> str:
        element = self.wait_for_visible()
        min_value = element.get_attribute("min")
        return min_value

    def get_max(self) -> str:
        element = self.wait_for_visible()
        max_value = element.get_attribute("max")
        return max_value
