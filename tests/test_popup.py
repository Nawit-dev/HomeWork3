from pages.main_page_popup import MainPage
from utils.faker_text import get_random_text

"""Задание 2"""


def test_alert(open_page_alert):
    true_text_alert = "I am a JS Alert"
    true_text_result = "You successfully clicked an alert"
    true_text_js_confirm = "I am a JS Confirm"
    true_text_result_js_confirm = "You clicked: Ok"
    true_text_alert_js_prompt = "I am a JS prompt"

    test = MainPage(open_page_alert)
    test.check_page_load()
    text_alert = test.click_alert()
    text_result = test.get_text_result()
    text_js_confirm = test.click_button_js_confirm()
    text_result_js_confirm = test.get_text_result()
    random_text = get_random_text()
    text_js_prompt = test.click_button_js_prompt(random_text)
    text_result_js_prompt = test.get_text_result().replace("You entered: ", "")

    assert text_alert == true_text_alert, f"Фактический результат {text_alert}, ожидаемый результат {true_text_alert}"  # Задание 2.2
    assert text_result == true_text_result, f"Фактический результат {text_result}, ожидаемый результат {true_text_result}"  # Задание 2.3
    assert text_js_confirm == true_text_js_confirm, (f"Фактический результат {text_js_confirm}, ожидаемый результат "
                                                     f"{true_text_js_confirm}")  # Задание 2.4
    assert text_result_js_confirm == true_text_result_js_confirm, (f"Фактический результат {text_result_js_confirm}, "
                                                                   f"ожидаемый результат {true_text_result_js_confirm}")  # Задание 2.5
    assert text_js_prompt == true_text_alert_js_prompt, (f"Фактический результат {text_js_prompt}, "
                                                         f"ожидаемый результат {true_text_alert_js_prompt}")  # Задание 2.6
    assert text_result_js_prompt == random_text, (f"Фактический результат {text_result_js_prompt}, "
                                                  f"ожидаемый результат {random_text}")
