"""
## Задача 5 - hard
### Условие:
Написать функцию generate_password(), которая:
- принимает 2 необязательных аргумента, минимальную и максимальную длину пароля в int
- должен генерироваться пароль длиной от минимальной до максимальной длины:
  - должен состоять из цифр, букв в нижнем и верхнем регистре, спецсимволов
  - должен быть хотя бы один символ из каждой категории
  - при генерации должен использоваться рандом из пакета secret (`import secrets`)
- сгенерированный пароль должен возвращаться в виде строчки
- включите фантазию, чтобы сделать пароль максимально рандомным
- используйте строгую / явную типизацию (аннотацию типов)
- напишите документацию по функции (под функцией в тройных кавычках)
"""
import random
import string
import secrets

def safe_shuffle(unshuffle_list: list) -> list:
    """
    Перемешивает переданный список
    :param unshuffle_list: список для перемешивания
    :return: перемешанный список
    """
    shuffled_list = []

    # Перемешиваем список пока не закончатся символы
    while unshuffle_list:
        # Выбираем случайный элемент из списка
        random_el = secrets.choice(unshuffle_list)
        # добавляем его в перемешанный список
        shuffled_list.append(random_el)
        # удаляем его из старого списка
        unshuffle_list.remove(random_el)
    return shuffled_list


def generate_password(length_min: int = 25, length_max: int = 35) -> str:
    """
    Генератор случайного пароля
    :param length_min: минимальная длина пароля
    :param length_max: максимальная длина пароля
    :return: пароль
    """
    password = []

    # Генерируем случайную длину пароля в диапазоне от length_min до length_max
    length = secrets.choice(range(length_min, length_max + 1))  # Генерируем случайную длину пароля

    # Определяем наборы символов
    all_characters = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]

    # добавляем по одному символу из каждого набора
    types_symbol = safe_shuffle([0, 1, 2, 3])
    for i in types_symbol:
        password.append(secrets.choice(all_characters[i]))

    # Добавляем случайные символы в пароль
    while len(password) < length:
        characters = secrets.choice(all_characters)
        password.append(secrets.choice(characters))

    # Перемешиваем пароль, чтобы сделать его менее предсказуемым
    shuffled_password = safe_shuffle(password)

    return ''.join(shuffled_password)


for _ in range(10000):
    print(generate_password(25, 35))
