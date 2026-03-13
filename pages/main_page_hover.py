from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

"""Задание 6"""


class MainPageHover:
    TIMEOUT = 10
    HEAD_TEXT = (By.XPATH, "//*[@id='content']//h3")

    FIGURES = (By.XPATH, "//div[@class='figure']")

    TEXT_HOVER_TEMPLATE = "//div[@class='figure'][{index}]//h5"
    LINK_HOVER_TEMPLATE = "//div[@class='figure'][{index}]//a"

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self):
        """Ждем загрузку стр"""
        WebDriverWait(self.driver, MainPageHover.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageHover.HEAD_TEXT))

    def hover_mouse(self, index) -> str:
        """Наводим на картинку пользователя по индексу (1, 2, 3)"""
        img_xpath = f"(//div[@class='figure'])[{index}]/img"
        img = WebDriverWait(self.driver, MainPageHover.TIMEOUT).until(
            ec.visibility_of_element_located((By.XPATH, img_xpath)))

        action = ActionChains(self.driver)
        action.move_to_element(img)
        action.perform()

        text_xpath = self.TEXT_HOVER_TEMPLATE.format(index=index)
        text_hover = WebDriverWait(self.driver, MainPageHover.TIMEOUT).until(
            ec.presence_of_element_located((By.XPATH, text_xpath)))
        return text_hover.text

    def click_link_hover(self, index) -> str:
        """Переходим по ссылке пользователя по индексу"""
        link_xpath = self.LINK_HOVER_TEMPLATE.format(index=index)
        link = WebDriverWait(self.driver, MainPageHover.TIMEOUT).until(
            ec.element_to_be_clickable((By.XPATH, link_xpath)))
        link.click()
        return self.driver.current_url

    def go_back(self) -> None:
        """Возвращаемся на предыдущую страницу"""
        self.driver.back()
        self.check_page_load()
