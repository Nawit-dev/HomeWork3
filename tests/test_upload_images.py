from pages.page_dialog_window import PageUploadImage
from pathlib import Path

"""Задание 11"""
LINK_SITE10 = "http://the-internet.herokuapp.com/upload"
IMG_PATH = (Path.cwd() / "images" / "img1.png").resolve()


def test_upload_images(test_driver):
    true_head_text = 'File Uploaded!'
    true_img_name = 'img1.png'

    test_driver.get(LINK_SITE10)
    upload_images_page = PageUploadImage(test_driver)

    upload_images_page.wait_page_load()
    upload_images_page.load_img(IMG_PATH)

    head_text = upload_images_page.get_text_head()
    img_name = upload_images_page.get_name_img()
    assert head_text == true_head_text, f'Фактический результат {head_text}, ожидаемый результат {true_head_text}'
    assert img_name == true_img_name, f'Фактический результат {img_name}, ожидаемый результат {true_img_name}'
