'''Создайте класс RandomUtils (не подсматривайте в уроке), в котором есть методы:
- возвращает рандомное целое число, принимает минимальное и максимальное значение, по умолчанию 0 и 100
- возвращает рандомное число с плавающей точкой и указанным округлением, принимает минимальное и максимальное значение, по умолчанию 0 и 1, округление по умолчанию 2
- возвращает рандомное число в диапазоне +-10% от переданного значения, принимает значение, по умолчанию 1 (вернет от 0,9 до 1,1)
- встает на рандомную паузу, принимает минимальное и максимальное значение, по умолчанию 0,5 и 1,5 секунды
- возвращает True/False с рандомной вероятностью, по умолчанию 50%, принимает вероятность возврата True в процентах от 0 до 100'''

import random
import time


class RandomUtils:
    """
    Класс для работы с рандомом
    """

    @staticmethod
    def random_int(min_value: int = 0, max_value: int = 100) -> int:
        """
        Метод для получения рандомного целого числа
        :param min_value: минимальное значение
        :param max_value: максимальное значение
        :return: рандомное число
        """
        return random.randint(min_value, max_value)

    @staticmethod
    def random_float(min_value: float = 0, max_value: float = 1, round_value: int = 2) -> float:
        """
        Метод для получения рандомного числа с плавающей точкой
        :param min_value: минимальное значение
        :param max_value: максимальное значение
        :param round_value: округление
        :return: рандомное число
        """
        return round(random.uniform(min_value, max_value), round_value)

    @staticmethod
    def random_percent(value: float = 1) -> float:
        """
        Метод для получения рандомного числа в диапазоне +-10% от переданного значения
        :param value: переданное значение
        :return: рандомное число
        """
        return random.uniform(value * 0.9, value * 1.1)

    @staticmethod
    def sleep(min_value: float = 0.5, max_value: float = 1.5) -> None:
        """
        Метод для встания на рандомную паузу
        :param min_value: минимальное значение
        :param max_value: максимальное значение
        """
        time_sleep = random.uniform(min_value, max_value)
        time.sleep(time_sleep)

    @staticmethod
    def random_bool(probability: int = 50) -> bool:
        """
        Метод для получения True/False с рандомной вероятностью
        :param probability: вероятность возврата True в процентах от 0 до 100
        :return: True/False
        """
        return random.randint(0, 100) < probability
