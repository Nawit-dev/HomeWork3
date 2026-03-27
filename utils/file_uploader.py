from logger.logger import Logger
import pyautogui
import time


class FileUploader:

    @staticmethod
    def load_img(element, img_path: str) -> None:

        """Загружаем картинку через диалоговое окно"""
        element.click_via_actions()
        Logger.info(f"Upload file: path={img_path}, element={element}")
        time.sleep(2)
        pyautogui.typewrite(img_path)
        pyautogui.hotkey("enter")
