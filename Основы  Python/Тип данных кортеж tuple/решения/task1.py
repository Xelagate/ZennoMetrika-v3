'''## Задача 1 - lite
### Условие:
Напишите функцию, которая:
- принимает кортеж чисел любой длинны
- возвращает кортеж из двух элементов: первого и последнего элемента входного кортежа

'''

def first_and_last(numbers: tuple) -> tuple[int, int]:
    """
    Функция принимает кортеж чисел любой длинны и возвращает кортеж из двух элементов: первого и последнего элемента входного кортежа
    :param numbers: кортеж чисел
    :return: кортеж из двух элементов: первого и последнего элемента входного кортежа
    """
    return numbers[0], numbers[-1]
