from pages.main_page_hover import MainPageHover

"""Задание 6"""


def test_hover(open_page_hover):
    # Данные для всех 3 пользователей
    users_data = [
        {"index": 1, "expected_name": "name: user1", "expected_url": "https://the-internet.herokuapp.com/users/1"},
        {"index": 2, "expected_name": "name: user2", "expected_url": "https://the-internet.herokuapp.com/users/2"},
        {"index": 3, "expected_name": "name: user3", "expected_url": "https://the-internet.herokuapp.com/users/3"},
    ]

    test = MainPageHover(open_page_hover)
    test.check_page_load()

    for user in users_data:
        # Шаг #2: Навести курсор и проверить имя
        user_name_hover = test.hover_mouse(user["index"])
        assert user_name_hover == user["expected_name"], (
            f"Пользователь {user['index']}: Фактический результат '{user_name_hover}', "
            f"ожидаемый результат '{user['expected_name']}'"
        )

        # Шаг #3: Перейти по ссылке и проверить URL
        link_user = test.click_link_hover(user["index"])
        assert link_user == user["expected_url"], (
            f"Пользователь {user['index']}: Фактический результат '{link_user}', "
            f"ожидаемый результат '{user['expected_url']}'"
        )

        # Шаг #4: Вернуться на предыдущую страницу
        test.go_back()

        print(f"Пользователь {user['index']} проверен успешно")
