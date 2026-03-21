from pages.main_page_hover import MainPageHover

"""Задание 6"""

LINK_SITE5 = "http://the-internet.herokuapp.com/hovers"


def test_hover(test_driver):
    # Данные для всех 3 пользователей
    users_data = [
        {"index": 1, "expected_name": "name: user1", "expected_url": "https://the-internet.herokuapp.com/users/1"},
        {"index": 2, "expected_name": "name: user2", "expected_url": "https://the-internet.herokuapp.com/users/2"},
        {"index": 3, "expected_name": "name: user3", "expected_url": "https://the-internet.herokuapp.com/users/3"},
    ]
    test_driver.get(LINK_SITE5)
    test = MainPageHover(test_driver)
    test.check_page_load()

    for user in users_data:
        # Навести курсор и проверить имя
        user_name_hover = test.hover_mouse(user["index"])
        assert user_name_hover == user["expected_name"], (
            f"Пользователь {user['index']}: Фактический результат '{user_name_hover}'"
            f"ожидаемый результат '{user['expected_name']}'"
        )

        # Перейти по ссылке и проверить URL
        link_user = test.click_link_hover(user["index"])
        assert link_user == user["expected_url"], (
            f"Пользователь {user['index']}: Фактический результат '{link_user}'"
            f"ожидаемый результат '{user['expected_url']}'"
        )

        # Вернуться на предыдущую страницу
        test.go_back()

        print(f"Пользователь {user['index']} проверен успешно")
