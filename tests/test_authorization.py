from pages.basic_auth_page import PageBasicAuth
from credentials import Credentials

"""Задание 1"""

LINK_SITE = f"http://{Credentials.LOGIN}:{Credentials.PASSWORD}@the-internet.herokuapp.com/basic_auth"


def test_authorization(test_driver):
    true_text = "Congratulations! You must have the proper credentials."
    test_driver.get(LINK_SITE)
    authorization_page = PageBasicAuth(test_driver)
    authorization_page.wait_page_load()
    text_from_page = authorization_page.get_text_after_basic_auth()
    assert text_from_page == true_text, f"Текущий результат {text_from_page}, ожидаемый результат {true_text}"
