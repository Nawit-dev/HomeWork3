import pytest
from browser.browser_factory import BrowserFactory
from browser.browser import Browser


@pytest.fixture()
def test_driver():
    options = [
        "--headless",
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
    driver = BrowserFactory.get_driver(options=options)
    browser = Browser(driver)
    yield browser
    browser.quit()
