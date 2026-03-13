from tests.conftest import open_main_page
from pages.main_page import MainPage

"""Задание 1"""


def test_authorization(open_main_page):
    true_text = "Congratulations! You must have the proper credentials."
    test = MainPage(open_main_page)
    text_from_page = test.get_text()
    assert text_from_page == true_text, f"Текущий результат {text_from_page}, ожидаемый результат {true_text}"
