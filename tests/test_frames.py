from pages.main_page_frames import MainPageFrames

"""Задание 8"""
LINK_SITE7 = "https://demoqa.com/frames"


def test_frames(test_driver):
    true_text = "Parent frame"
    child_text = "Child Iframe"

    test_driver.get(LINK_SITE7)
    test = MainPageFrames(test_driver)
    test.check_page_load()
    text, text_two = test.open_nested_frames()
    assert true_text == text, f"Фактический результат {text}, ожидаемы результат{true_text}"
    assert child_text == text_two, f"Фактический результат {text}, ожидаемы результат{text_two}"
