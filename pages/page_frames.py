from .base_page import BasePage
from browser.browser import Browser
from elements.button import Button
from elements.label import Label
from selenium.webdriver.common.by import By

"""Задание 8"""


class PageFrames(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(text(), 'Alerts, Frame & Windows')]"
    BTN_LIGHT = "//a[contains(@href, '/nestedframes')]"
    FRAME = "frame1"
    FRAME_TEXT = (By.TAG_NAME, "body")
    FRAME_TWO = (By.TAG_NAME, "iframe")
    FRAME_TWO_TEXT = (By.TAG_NAME, "p")

    def __init__(self, browser: Browser):
        super().__init__(browser)
        self.unique_element = Button(browser, PageFrames.UNIQUE_ELEMENT_LOC, description="unique_element")
        self.btn_light = Button(browser, PageFrames.BTN_LIGHT, description="btn_nested_frames")
        self.frame = Label(browser, PageFrames.FRAME, description="frame 1")
        self.frame_text = Label(browser, PageFrames.FRAME_TEXT, description="text frame 1")
        self.frame_two = Label(browser, PageFrames.FRAME_TWO, description="frame 2")
        self.frame_two_text = Label(browser, PageFrames.FRAME_TWO_TEXT, description="text frame 2")

    def open_nested_frames(self) -> tuple[str, str]:
        self.btn_light.click()
        return self.get_parent_frame_text(), self.get_child_frame_text()

    def get_parent_frame_text(self) -> str:
        self.browser.switch_to_frame(self.frame)
        text = self.frame_text.wait_for_presence().text
        self.browser.switch_to_default_content()
        return text

    def get_child_frame_text(self) -> str:
        self.browser.switch_to_frame(self.frame)  # сначала в parent
        self.browser.switch_to_frame(self.frame_two)  # потом в child
        text = self.frame_two_text.wait_for_presence().text
        self.browser.switch_to_default_content()
        return text
