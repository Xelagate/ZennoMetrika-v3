'''

## Задача 4 - medium
### Условие:
Напишите функцию, которая принимает кортеж и возвращает кортеж с
перемешанными элементами входного кортежа.
'''


def shuffle_tuple(data: tuple) -> tuple:
    """
    Функция перемешивает элементы кортежа
    :param data: кортеж
    :return: перемешанный кортеж
    """
    import random
    data = list(data)
    random.shuffle(data)
    return tuple(data)
