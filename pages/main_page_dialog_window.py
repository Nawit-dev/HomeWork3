from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import os
import pyautogui
import time

"""Задание 12"""


class MainPageDialogWindow:
    TIMEOUT = 10
    HEAD_TEXT = (By.XPATH, "//*[@id='content']//h3")
    FILE_UPLOAD = (By.ID, "drag-drop-upload")
    BUTTON_UPLOAD = (By.ID, "file-submit")
    IMG_PATH = os.path.join(os.getcwd(), "images", "img1.png")
    IMG_NAME = (By.XPATH, "//span[@data-dz-name]")
    CHECK_SPAN = (By.XPATH, "//span[contains(text(), '✔')]")

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        WebDriverWait(self.driver, MainPageDialogWindow.TIMEOUT).until(
            ec.presence_of_element_located(MainPageDialogWindow.HEAD_TEXT))

    def load_img(self) -> None:
        """Загружаем картинку через диалоговое окно"""
        upload_file = WebDriverWait(self.driver, MainPageDialogWindow.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageDialogWindow.FILE_UPLOAD))
        ActionChains(self.driver).click(upload_file).perform()
        time.sleep(1)
        pyautogui.typewrite(MainPageDialogWindow.IMG_PATH)
        pyautogui.hotkey("enter")

    def get_text(self) -> tuple[str, str]:
        """Получаем название картинки"""
        element_text_img_name = WebDriverWait(self.driver, MainPageDialogWindow.TIMEOUT).until(
            ec.presence_of_element_located(MainPageDialogWindow.IMG_NAME))
        img_text = element_text_img_name.text
        element_img = WebDriverWait(self.driver, MainPageDialogWindow.TIMEOUT).until(
            ec.presence_of_element_located(MainPageDialogWindow.CHECK_SPAN))
        check_span = element_img.text
        return img_text, check_span
