from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

"""Задание 11"""


class MainPageUploadImage:
    TIMEOUT = 10
    HEAD_TEXT = (By.XPATH, "//*[@id='content']//h3")
    FILE_UPLOAD = (By.ID, "file-upload")
    BUTTON_UPLOAD = (By.ID, "file-submit")
    IMG_NAME = (By.ID, "uploaded-files")
    IMG_PATH = os.path.join(os.getcwd(), "images", "img1.png")

    def __init__(self, driver):
        self.driver = driver

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        WebDriverWait(self.driver, MainPageUploadImage.TIMEOUT).until(
            ec.presence_of_element_located(MainPageUploadImage.HEAD_TEXT))

    def load_img(self) -> None:
        """Загружаем картинку"""
        upload_file = WebDriverWait(self.driver, MainPageUploadImage.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageUploadImage.FILE_UPLOAD))
        upload_file.send_keys(MainPageUploadImage.IMG_PATH)
        button_upload = WebDriverWait(self.driver, MainPageUploadImage.TIMEOUT).until(
            ec.element_to_be_clickable(MainPageUploadImage.BUTTON_UPLOAD))
        button_upload.click()

    def get_text(self) -> tuple[str, str]:
        """Получаем текст о загрузке"""
        element_head = WebDriverWait(self.driver, MainPageUploadImage.TIMEOUT).until(
            ec.presence_of_element_located(MainPageUploadImage.HEAD_TEXT))
        head_text = element_head.text
        element_img = WebDriverWait(self.driver, MainPageUploadImage.TIMEOUT).until(
            ec.presence_of_element_located(MainPageUploadImage.IMG_NAME))
        img_name = element_img.text
        return head_text, img_name
