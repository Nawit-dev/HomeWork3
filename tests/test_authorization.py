from pages.main_page import MainPage
from credentials import Credentials

"""Задание 1"""

LINK_SITE = f"http://{Credentials.LOGIN}:{Credentials.PASSWORD}@the-internet.herokuapp.com/basic_auth"


def test_authorization(test_driver):
    true_text = "Congratulations! You must have the proper credentials."
    test_driver.get(LINK_SITE)
    page = MainPage(test_driver)
    text_from_page = page.get_text()
    assert text_from_page == true_text, f"Текущий результат {text_from_page}, ожидаемый результат {true_text}"
