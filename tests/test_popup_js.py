from pages.main_page_popup_js import MainPageJS
from utils.faker_text import get_random_text
"""Задание 3"""


def test_alert(open_page_alert):
    true_text_alert = "I am a JS Alert"
    true_text_js_confirm = "I am a JS Confirm"
    true_text_alert_js_prompt = "I am a JS prompt"

    test = MainPageJS(open_page_alert)
    test.check_page_load()
    text_alert = test.alert_js()
    text_js_confirm = test.confirm_js()
    random_text = get_random_text()
    text_js_prompt = test.prompt_js(random_text)

    assert text_alert == true_text_alert, f"Фактический результат {text_alert}, ожидаемый результат {true_text_alert}"  # Задание 2.2
    assert text_js_confirm == true_text_js_confirm, (f"Фактический результат {text_js_confirm}, ожидаемый результат "
                                                     f"{true_text_js_confirm}")  # Задание 2.4
    assert text_js_prompt == true_text_alert_js_prompt, (f"Фактический результат {text_js_prompt}, "
                                                         f"ожидаемый результат {true_text_alert_js_prompt}")  # Задание 2.6
