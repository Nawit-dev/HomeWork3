from pages.main_page_windows import MainPageWindows


def test_windows(open_page_windows):
    true_text_new_window = "New Window"
    true_name_tab = "New Window"
    test = MainPageWindows(open_page_windows)
    test.check_page_load()
    text_new_window, name_tab = test.open_new_tabs()
    test.back_to_original_window()
    text_new_window2, name_tab2 = test.open_new_tabs()
    test.back_to_original_window()
    test.close_tabs()

    assert text_new_window == true_text_new_window, (f"Фактический результат {true_text_new_window}, "
                                                     f"ожидаемый результат {true_text_new_window}")
    assert name_tab == true_name_tab, (f"Фактический результат {name_tab}, "
                                       f"ожидаемый результат {true_name_tab}")
    assert text_new_window2 == true_text_new_window, (f"Фактический результат {true_text_new_window}, "
                                                      f"ожидаемый результат {true_text_new_window}")
    assert name_tab2 == true_name_tab, (f"Фактический результат {name_tab}, "
                                        f"ожидаемый результат {true_name_tab}")
