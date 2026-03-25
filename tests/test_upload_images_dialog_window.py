from pages.page_dialog_window import PageUploadImage
from pathlib import Path

"""Задание 12"""

LINK_SITE10 = "http://the-internet.herokuapp.com/upload"

IMG_PATH = (Path.cwd() / "images" / "img1.png").resolve()


def test_upload_images_dialog_window(test_driver):
    true_img_name = 'img1.png'
    true_check_span = '✔'

    test_driver.get(LINK_SITE10)
    upload_images_dialog_window_page = PageUploadImage(test_driver)

    upload_images_dialog_window_page.wait_page_load()
    upload_images_dialog_window_page.load_img(IMG_PATH)

    img_text = upload_images_dialog_window_page.get_name_img2()
    check_span = upload_images_dialog_window_page.get_text_span()

    assert img_text == true_img_name, f'Фактический результат {img_text}, ожидаемый результат {true_img_name}'
    assert check_span == true_check_span, f'Фактический результат {check_span}, ожидаемый результат {true_check_span}'
