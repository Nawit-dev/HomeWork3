from pages.main_page_upload_image import MainPageUploadImage

"""Задание 11"""
LINK_SITE10 = "http://the-internet.herokuapp.com/upload"


def test_upload_images(test_driver):
    true_head_text = 'File Uploaded!'
    true_img_name = 'img1.png'

    test_driver.get(LINK_SITE10)
    test = MainPageUploadImage(test_driver)
    test.check_page_load()
    test.load_img()
    head_text, img_name = test.get_text()
    assert head_text == true_head_text, f'Фактический результат {head_text}, ожидаемый результат {true_head_text}'
    assert img_name == true_img_name, f'Фактический результат {img_name}, ожидаемый результат {true_img_name}'
