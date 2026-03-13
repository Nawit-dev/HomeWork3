from faker import Faker
"""Задание 2"""

faker = Faker("en_US")


def get_random_text() -> str:
    """Возвращаем рандомное слово"""
    text = faker.word()
    return text
