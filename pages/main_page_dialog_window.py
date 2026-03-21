from browser.browser import Browser
from elements.label import Label
from elements.button import Button
import os
import pyautogui
import time

"""Задание 12"""


class MainPageDialogWindow:
    HEAD_TEXT = "//*[@id='content']//h3"
    FILE_UPLOAD = "drag-drop-upload"
    BUTTON_UPLOAD = "file-submit"
    IMG_PATH = os.path.join(os.getcwd(), "images", "img1.png")
    IMG_NAME = "//span[@data-dz-name]"
    CHECK_SPAN = "//span[contains(text(), '✔')]"

    def __init__(self, browser: Browser):
        self.browser = browser
        self.head_text = Label(browser, MainPageDialogWindow.HEAD_TEXT)
        self.file_upload = Button(browser, MainPageDialogWindow.FILE_UPLOAD)
        self.img_name = Label(browser, MainPageDialogWindow.IMG_NAME)
        self.check_span = Label(browser, MainPageDialogWindow.CHECK_SPAN)

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        self.head_text.wait_for_presence()

    def load_img(self) -> None:
        """Загружаем картинку через диалоговое окно"""
        self.file_upload.click_via_actions()
        time.sleep(1)
        pyautogui.typewrite(MainPageDialogWindow.IMG_PATH)
        pyautogui.hotkey("enter")

    def get_text(self) -> tuple[str, str]:
        """Получаем название картинки"""
        img_text = self.img_name.get_text()
        check_span = self.check_span.get_text()

        return img_text, check_span
