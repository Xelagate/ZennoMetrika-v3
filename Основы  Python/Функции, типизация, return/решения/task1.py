"""
## Задача 1 - light
### Условие:
Напишите функцию check_balance(), которая:
- принимает на вход адрес кошелька
- проверяет что передан корректный адрес с помощью функции is_address_correct()
  - 42 знака
  - начинается с 0x
  - в адресе только цифры и буквы a-f
  - если адрес не корректный, печатает сообщение "Invalid address" и возращает 0.00
- генерирует случайный баланс
- возвращает баланс в формате float
- используйте строгую / явную типизацию (аннотацию типов)
- напишите документацию по функции (под функцией в тройных кавычках)

"""
import random


def is_address_correct(wallet: str) -> bool:
    """
    Проверяет корректность адреса кошелька, должен быть длиной 42 символа, начинаться с 0x и содержать только цифры и буквы a-f.
    :param wallet: адрес кошелька в любом регистре
    :return: True если адрес корректный, иначе False
    """
    wallet = wallet.lower()
    if len(wallet) != 42:
        return False
    if not wallet.startswith('0x'):
        return False
    for char in wallet[2:]:
        if char not in '0123456789abcdef':
            return False
    return True


def check_balance(wallet: str) -> float:
    """
    Возвращает баланс кошелька.
    :param wallet: адрес кошелька в любом регистре
    :return: псевдо-баланс
    """
    if not is_address_correct(wallet):
        print("Invalid address")
        return 0.00
    return round(random.uniform(0, 100), 2)
