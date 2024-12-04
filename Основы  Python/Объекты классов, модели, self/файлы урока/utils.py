import random
import time


def get_list_from_file(file_path: str) -> list:
    """
    Метод для получения списка из файла
    :param file_path: путь к файлу
    :return: список
    """
    with open(file_path, 'r') as file:
        return file.read().splitlines()


class RandomUtils:

    @staticmethod
    def sleep(min_delay: float = 0.5, max_delay: float = 1.5) -> None:
        """
        Метод для случайной задержки
        :param min_delay: минимальная задержка
        :param max_delay: максимальная задержка
        """
        delay = random.uniform(min_delay, max_delay)
        time.sleep(delay)

    @staticmethod
    def amount(min_amount: float = 0.1, max_amount: float = 1.0, round_: int = 2) -> float:
        """
        Метод для получения случайного значения
        :param min_amount: минимальное значение
        :param max_amount: максимальное значение
        :param round_: количество знаков после запятой
        :return: случайное значение
        """
        return round(random.uniform(min_amount, max_amount), round_)

    @staticmethod
    def password(length: int = 8) -> str:
        """
        Метод для генерации случайного пароля
        :param length: длина пароля
        :return: пароль
        """
        return ''.join(
            random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))
