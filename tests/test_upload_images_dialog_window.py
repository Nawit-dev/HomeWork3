from pages.main_page_dialog_window import MainPageDialogWindow

"""Задание 12"""
LINK_SITE10 = "http://the-internet.herokuapp.com/upload"


def test_upload_images_dialog_window(test_driver):
    true_img_name = 'img1.png'
    true_check_span = '✔'

    test_driver.get(LINK_SITE10)
    test = MainPageDialogWindow(test_driver)
    test.check_page_load()
    test.load_img()
    img_text, check_span = test.get_text()
    assert img_text == true_img_name, f'Фактический результат {img_text}, ожидаемый результат {true_img_name}'
    assert check_span == true_check_span, f'Фактический результат {check_span}, ожидаемый результат {true_check_span}'
