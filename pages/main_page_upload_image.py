from browser.browser import Browser
from elements.label import Label
from elements.button import Button
import os

"""Задание 11"""


class MainPageUploadImage:
    HEAD_TEXT = "//*[@id='content']//h3"
    FILE_UPLOAD = "file-upload"
    BUTTON_UPLOAD = "file-submit"
    IMG_NAME = "uploaded-files"
    IMG_PATH = os.path.join(os.getcwd(), "images", "img1.png")

    def __init__(self, browser: Browser):
        self.browser = browser
        self.head_text = Label(browser, MainPageUploadImage.HEAD_TEXT)
        self.file_upload = Button(browser, MainPageUploadImage.FILE_UPLOAD)
        self.btn_upload = Button(browser, MainPageUploadImage.BUTTON_UPLOAD)
        self.img_name = Label(browser, MainPageUploadImage.IMG_NAME)

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        self.head_text.wait_for_presence()

    def load_img(self) -> None:
        """Загружаем картинку"""
        self.file_upload.send_keys(MainPageUploadImage.IMG_PATH)
        self.btn_upload.click()

    def get_text(self) -> tuple[str, str]:
        """Получаем текст о загрузке"""

        head_text = self.head_text.get_text()
        img_name = self.img_name.get_text()

        return head_text, img_name
