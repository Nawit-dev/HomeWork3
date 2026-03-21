import pytest
from credentials import Credentials
from browser.browser_factory import BrowserFactory
from browser.browser import Browser

LINK_SITE = f"http://{Credentials.LOGIN}:{Credentials.PASSWORD}@the-internet.herokuapp.com/basic_auth"

LINK_SITE3 = "https://the-internet.herokuapp.com/context_menu"









@pytest.fixture()
def test_driver():
    driver = BrowserFactory.get_driver()
    browser = Browser(driver)
    yield browser
    browser.quit()



