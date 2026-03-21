import time
from selenium.common import WebDriverException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from elements.base_elements import BaseElement
from logger.logger import Logger


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 120

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)

        self.main_handle = None

        self._wait = WebDriverWait(self._driver, timeout=self.DEFAULT_TIMEOUT)

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def get(self, url: str) -> None:
        Logger.info(f"{self}: get '{url}'")
        try:
            self._driver.get(url)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise
        self.main_handle = self._driver.current_window_handle

    def close(self) -> None:
        Logger.info(f"{self}: close window handle = '{self._driver.current_window_handle}'")
        self._driver.close()

    def quit(self) -> None:
        Logger.info(f"{self}: quit")
        try:
            self._driver.quit()
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")

    def execute_script(self, script: str, *args) -> None:
        Logger.info(f"{self}: execute script = '{script}' with args '{args}'")
        try:
            self._driver.execute_script(script, *args)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def switch_to_default_window(self) -> None:
        Logger.info(f"{self}: switch to default window")
        try:
            self._driver.switch_to.window(self.main_handle)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def switch_to_window(self, title: str) -> None:
        Logger.info(f"{self}: switch to window with title '{title}'")
        end_time = time.time() + self.PAGE_LOAD_TIMEOUT
        while True:
            handles = self._driver.window_handles
            for handle in handles:
                self._driver.switch_to.window(handle)
                if self._driver.title == title:
                    Logger.info(f"{self}: new window handle = '{self._driver.current_window_handle}'")
                    return
                if time.time() < end_time:
                    time.sleep(1)
                else:
                    Logger.error(f"{self}: window with '{title}' wasn't found")
                    raise ValueError(f"{self}: window with title '{title}' wasn't found")

    def switch_to_window_handle(self, handle: str) -> None:
        Logger.info(f"{self}: switch to window by handle '{handle}'")
        try:
            self._driver.switch_to.window(handle)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def wait_alert_present(self):
        expected_conditions_alert = expected_conditions.alert_is_present()
        Logger.info(f"{self}: wait alert present")
        return self._wait.until(expected_conditions_alert)

    def switch_to_alert(self):
        Logger.info(f"{self}: switch to alert")
        self.wait_alert_present()
        return self.driver.switch_to.alert

    def get_alert_text(self) -> str:
        Logger.info(f"{self}: get alert text")
        alert = self.switch_to_alert()
        return alert.text

    def accept_alert(self):
        alert = self.switch_to_alert()
        Logger.info(f"{self}: accept alert")
        alert.accept()

    def send_keys_alert(self, text: str):
        alert = self.switch_to_alert()
        Logger.info(f"{self}: send '{text} to alert'")
        alert.send_keys(text)

    def switch_to_frame(self, frame: BaseElement):
        frame_el = frame.wait_for_presence()
        Logger.info(f"{self}: switch to frame")
        return self.driver.switch_to.frame(frame_el)

    def switch_to_default_content(self):
        Logger.info(f"{self}: switch to default content")
        self.driver.switch_to.default_content()

    def refresh_page(self):
        return self._driver.refresh()

    def return_url(self):
        return self._driver.current_url

    def navigate_back(self):
        return self._driver.back()

    def current_window_handle(self) -> str:
        """Возвращает хэндл текущей вкладки"""
        return self._driver.current_window_handle

    def get_current_windows(self) -> list[str]:
        """Возвращает список текущих открытых окон/вкладок"""
        return self._driver.window_handles.copy()

    def wait_for_new_window(self, old_windows: list[str], timeout: int = None) -> str:
        """Ждём появления новой вкладки/окна и возвращаем её хэндл"""
        if timeout is None:
            timeout = self.DEFAULT_TIMEOUT

        new_window = WebDriverWait(self.driver, timeout).until(
            lambda d: next((w for w in d.window_handles if w not in old_windows), None)
        )
        return new_window


def __str__(self) -> str:
    return f"{self.__class__.__name__}[{self._driver.session_id}]"


def __repr__(self) -> str:
    return str(self)
