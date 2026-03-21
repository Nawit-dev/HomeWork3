from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from selenium.webdriver.common.by import By

"""Задание 8"""


class MainPageFrames:
    BTN_ACCORDION = (By.XPATH, "//div[contains(text(), 'Alerts, Frame & Windows')]")
    BTN_LIGHT = (By.XPATH, "//a[contains(@href, '/nestedframes')]")
    FRAME = (By.ID, "frame1")
    FRAME_TEXT = (By.TAG_NAME, "body")
    FRAME_TWO = (By.TAG_NAME, "iframe")
    FRAME_TWO_TEXT = (By.TAG_NAME, "p")

    def __init__(self, browser: Browser):
        self.browser = browser
        self.btn_accordion = Button(browser, MainPageFrames.BTN_ACCORDION)
        self.btn_light = Button(browser, MainPageFrames.BTN_LIGHT)
        self.frame = Label(browser, MainPageFrames.FRAME)
        self.frame_text = Label(browser, MainPageFrames.FRAME_TEXT)
        self.frame_two = Label(browser, MainPageFrames.FRAME_TWO)
        self.frame_two_text = Label(browser, MainPageFrames.FRAME_TWO_TEXT)

    def check_page_load(self) -> None:
        """Ждем загрузку стр"""
        self.btn_accordion.wait_for_clickable()

    def open_nested_frames(self) -> tuple[str, str]:
        self.btn_light.click()

        # frame родитель
        self.browser.switch_to_frame(self.frame)
        parent_text = self.frame_text.wait_for_presence().text

        # Дочерний frame
        self.browser.switch_to_frame(self.frame_two)
        child_text = self.frame_two_text.wait_for_presence().text

        self.browser.switch_to_default_content()

        return parent_text, child_text
