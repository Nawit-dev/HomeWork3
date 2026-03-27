from pages.base_page import BasePage
from browser.browser import Browser
from elements.label import Label
from elements.button import Button
from utils.file_uploader import FileUploader
from pathlib import Path

"""Задание 11"""


class PageUploadImage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[@id='content']//h3"
    FILE_UPLOAD_SUCCESS = "//*[@id='content']//h3"
    FILE_UPLOAD = "file-upload"
    BUTTON_UPLOAD = "file-submit"
    IMG_NAME = "uploaded-files"
    # Задание 12
    FILE_UPLOAD_BOX = "drag-drop-upload"
    IMG_NAME2 = "//span[@data-dz-name]"
    CHECK_SPAN = "//span[contains(text(), '✔')]"

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="unique element")
        self.text_upload_success = Label(browser, self.UNIQUE_ELEMENT_LOC, description="unique element")
        self.file_upload = Button(browser, self.FILE_UPLOAD, description="input file_upload")
        self.btn_upload = Button(browser, self.BUTTON_UPLOAD, description="btn upload")
        self.img_name = Label(browser, self.IMG_NAME, description="img name")
        # Задание 12
        self.file_upload = Button(browser, self.FILE_UPLOAD_BOX, description="Upload file button")
        self.img_name2 = Label(browser, self.IMG_NAME2, description="name img")
        self.check_span = Label(browser, self.CHECK_SPAN, description="Success check mark")

    def load_img(self, img_path: Path) -> None:
        """Загружаем картинку через диалоговое окно"""
        FileUploader.load_img(self.file_upload, str(img_path))
        self.btn_upload.click()

    def get_text_head(self) -> str:
        """Получаем текст из заголовка после загрузки картинки"""
        head_text = self.text_upload_success.get_text()
        return head_text

    def get_name_img(self) -> str:
        """Получаем название картинки"""
        img_name = self.img_name.get_text()
        return img_name

    # Задание 12

    def get_name_img2(self) -> str:
        """Получаем название картинки"""
        img_name = self.img_name2.get_text()
        return img_name

    def get_text_span(self) -> str:
        """Получаем текст из span после загрузки картинки"""
        check_span = self.check_span.get_text()
        return check_span
