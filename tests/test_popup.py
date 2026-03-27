from pages.page_popup import PageJavascriptAlerts
from faker import Faker

"""Задание 2"""
LINK_SITE2 = "https://the-internet.herokuapp.com/javascript_alerts"

faker = Faker("en_US")


def test_alert(test_driver):
    true_text_alert = "I am a JS Alert"
    true_text_result = "You successfully clicked an alert"
    true_text_js_confirm = "I am a JS Confirm"
    true_text_result_js_confirm = "You clicked: Ok"
    true_text_alert_js_prompt = "I am a JS prompt"

    alert_page = PageJavascriptAlerts(test_driver)
    test_driver.get(LINK_SITE2)
    alert_page.wait_page_load()

    text_alert = alert_page.click_alert()
    text_result = alert_page.get_text_result()
    text_js_confirm = alert_page.click_button_js_confirm()
    text_result_js_confirm = alert_page.get_text_result()

    random_text = faker.word()
    text_js_prompt = alert_page.click_button_js_prompt(random_text)
    text_result_js_prompt = alert_page.get_text_result().replace("You entered: ", "")

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
