"""
## Задача 2 - middle
### Условие:
Написать функцию get_stat(), которая:
- принимает на вход словарь со статистикой в формате {wallet:{activity:count}}
- принимает на вход адрес кошелька
- принимает на вход название активности
- проверяет корректность переданного кошелька используя функцию is_address_correct()
- если адрес не корректный, печатает сообщение "Invalid address" и выходит из функции возвращая 0
- если адрес не найден в словаре, печатает сообщение "Address not found" и выходит из функции возвращая 0
- если адрес и активность найдена возвращает счетчик по данному адресу и активности из словаря
- используйте строгую / явную типизацию (аннотацию типов)
- напишите документацию по функции (под функцией в тройных кавычках)
"""
stat = {
    '0xac8ce8fbc80115a22a9a69e42f50713aae9ef2f7': {
        'activity1': 1,
        'activity2': 2,
        'activity3': 3,
    },
    '0xac8ce8fbc80115a22a9a69e42f50713aae9ef2f8': {
        'activity1': 3,
        'activity2': 4,
        'activity3': 5,
    }}


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


def get_stat(data: dict, wallet: str, activity: str) -> int:
    """
    Функция для получения статистики по кошельку и активности из словаря stat.
    :param data: словарь со статистикой
    :param wallet: кошелек
    :param activity: активность
    :return: статистика
    """

    if not is_address_correct(wallet):
        print("Invalid address")
        return 0

    if wallet not in data:
        print("Address not found")
        return 0

    return data.get(wallet, {}).get(activity, 0)
