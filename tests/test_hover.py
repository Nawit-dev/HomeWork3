import pytest
from pages.page_hover import PageHover

"""Задание 6"""

LINK_SITE5 = "http://the-internet.herokuapp.com/hovers"

# Данные для всех 3 пользователей
users_data = [
    {"index": 1, "expected_name": "name: user1", "expected_url": "https://the-internet.herokuapp.com/users/1"},
    {"index": 2, "expected_name": "name: user2", "expected_url": "https://the-internet.herokuapp.com/users/2"},
    {"index": 3, "expected_name": "name: user3", "expected_url": "https://the-internet.herokuapp.com/users/3"},
]


@pytest.mark.parametrize("data", users_data)
def test_hover(test_driver, data):
    test_driver.get(LINK_SITE5)
    hover_page = PageHover(test_driver)
    hover_page.wait_page_load()

    def get_url_usr():
        return test_driver.get_url()

    def go_back() -> None:
        """Возвращаемся на предыдущую страницу"""
        test_driver.navigate_back()

    # Навести курсор и проверить имя
    user_name_hover = hover_page.hover_mouse(data["index"])
    assert user_name_hover == data["expected_name"], (
        f"Пользователь {data['index']}: Фактический результат '{user_name_hover}'"
        f"ожидаемый результат '{data['expected_name']}'"
    )

    # Перейти по ссылке и проверить URL
    hover_page.click_link_hover(data["index"])
    link_user = get_url_usr()
    assert link_user == data["expected_url"], (
        f"Пользователь {data['index']}: Фактический результат '{link_user}'"
        f"ожидаемый результат '{data['expected_url']}'"
    )

    # Вернуться на предыдущую страницу и дожидаемся загрузки
    go_back()
    hover_page.wait_page_load()
