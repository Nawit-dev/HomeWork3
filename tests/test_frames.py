from pages.page_frames import PageFrames

"""Задание 8"""
LINK_SITE7 = "https://demoqa.com/frames"


def test_frames(test_driver):
    true_parent_text = "Parent frame"
    true_child_text = "Child Iframe"

    test_driver.get(LINK_SITE7)
    frames_page = PageFrames(test_driver)
    frames_page.wait_page_load()

    frames_page.open_nested_frames()

    text_parent_frame = frames_page.get_parent_frame_text()
    text_child_frame = frames_page.get_child_frame_text()
    assert true_parent_text == text_parent_frame, (f"Фактический результат {text_parent_frame}, "
                                                   f"ожидаемы результат{true_parent_text}")
    assert true_child_text == text_child_frame, (f"Фактический результат {text_child_frame}, "
                                                 f"ожидаемы результат{true_child_text}")
