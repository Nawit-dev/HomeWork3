import pytest
from selenium import webdriver
from credentials import Credentials

LINK_SITE = f"http://{Credentials.LOGIN}:{Credentials.PASSWORD}@the-internet.herokuapp.com/basic_auth"
LINK_SITE2 = "https://the-internet.herokuapp.com/javascript_alerts"
LINK_SITE3 = "https://the-internet.herokuapp.com/context_menu"
LINK_SITE4 = "https://the-internet.herokuapp.com/horizontal_slider"
LINK_SITE5 = "http://the-internet.herokuapp.com/hovers"
LINK_SITE6 = "http://the-internet.herokuapp.com/windows"
LINK_SITE7 = "https://demoqa.com/frames"
LINK_SITE8 = "http://the-internet.herokuapp.com/dynamic_content"
LINK_SITE9 = "http://the-internet.herokuapp.com/infinite_scroll"
LINK_SITE10 = "http://the-internet.herokuapp.com/upload"


@pytest.fixture()
def driver():
    """Задание 1"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def open_main_page(driver):
    """Задание 2"""
    driver.get(LINK_SITE)
    return driver


@pytest.fixture()
def open_page_alert(driver):
    """Задание 3"""
    driver.get(LINK_SITE2)
    return driver


@pytest.fixture()
def open_page_context_menu(driver):
    """Задание 4"""
    driver.get(LINK_SITE3)
    return driver


@pytest.fixture()
def open_page_slider(driver):
    """Задание 5"""
    driver.get(LINK_SITE4)
    return driver


@pytest.fixture()
def open_page_hover(driver):
    """Задание 6"""
    driver.get(LINK_SITE5)
    return driver


@pytest.fixture()
def open_page_windows(driver):
    """Задание 7"""
    driver.get(LINK_SITE6)
    return driver


@pytest.fixture()
def open_page_frames(driver):
    """Задание 8"""
    driver.get(LINK_SITE7)
    return driver


@pytest.fixture()
def open_page_fork_dynamic_content(driver):
    """Задание 9"""
    driver.get(LINK_SITE8)
    return driver


@pytest.fixture()
def open_page_infinite_scroll(driver):
    """Задание 10"""
    driver.get(LINK_SITE9)
    return driver


@pytest.fixture()
def open_page_upload_image(driver):
    """Задание 11,12,13"""
    driver.get(LINK_SITE10)
    return driver
