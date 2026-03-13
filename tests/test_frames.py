from pages.main_page_frames import MainPageFrames
"""Задание 8"""

def test_frames(open_page_frames):
    true_text = "Parent frame"
    child_text = "Child Iframe"
    test = MainPageFrames(open_page_frames)
    test.check_page_load()
    text, text_two = test.open_nested_frames()
    assert true_text == text, f"Фактический результат {text}, ожидаемы результат{true_text}"
    assert true_text == text_two, f"Фактический результат {text}, ожидаемы результат{text_two}"
