import pytest
from browser.browser_factory import BrowserFactory
from browser.browser import Browser


@pytest.fixture()
def test_driver():
    driver = BrowserFactory.get_driver()
    browser = Browser(driver)
    yield browser
    browser.quit()
