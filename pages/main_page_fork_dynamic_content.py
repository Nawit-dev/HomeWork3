from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""Задание 9"""


class MainPageDynamicContent:
    TIMEOUT = 10
    LINK = (By.XPATH, "//a[@href='https://github.com/tourdedave/the-internet']")
    IMG = (By.XPATH, "//div[contains(@class, 'large-2 columns')]//img")

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        WebDriverWait(self.driver, MainPageDynamicContent.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageDynamicContent.LINK))

    def refresh_page(self) -> bool:
        """Обновляем страницу до тех пор, пока
        любых два изображения из трех не будут
        совпадать
        """
        while True:
            img_list = WebDriverWait(self.driver, MainPageDynamicContent.TIMEOUT).until(
                ec.presence_of_all_elements_located(MainPageDynamicContent.IMG))
            src_list = []
            for img in img_list:
                src_list.append(img.get_attribute('src'))
            if src_list[0] == src_list[1] or src_list[0] == src_list[2] or src_list[1] == src_list[2]:
                return True
            self.driver.refresh()
