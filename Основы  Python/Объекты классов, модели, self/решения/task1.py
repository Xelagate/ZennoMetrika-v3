'''
## Задача 1 - lite
### Условие:

Создайте класс Accuunt, который принимает:
- номер профиля
- адрес кошелька
- приватный ключ
- сид фразу
- пароль от метамаска
- прокси

В атрибуте объекта с номером профиля должно быть число в формате int,
даже если при инициализации передается строка. Реализуйте в методе init
проверку на тип данных и преобразование в int.

'''
from typing import Optional


class Account:
    """
    Модель для хранения данных аккаунта
    """

    def __init__(
            self,
            profile_number: int,
            address: Optional[str] = None,
            password: Optional[str] = None,
            private_key: Optional[str] = None,
            seed: Optional[str] = None,
            proxy: Optional[str] = None
    ) -> None:
        """
        Инициализация класса Account
        :param profile_number: номер профиля, если передается строка, то преобразовается в int
        :param address: адрес кошелька
        :param password: пароль от метамаска
        :param private_key: приватный ключ
        :param seed: сид фраза
        :param proxy: прокси
        """
        self.profile_number = profile_number if isinstance(profile_number, int) else int(profile_number)
        self.address = address
        self.private_key = private_key
        self.password = password
        self.seed = seed
        self.proxy = proxy


def test():
    account = Account(1, 'address', 'password', 'private_key', 'seed', 'proxy')
    assert account.profile_number == 1
    assert account.address == 'address'
    assert account.password == 'password'
    assert account.private_key == 'private_key'
    assert account.seed == 'seed'
    assert account.proxy == 'proxy'

    account = Account('2', 'address')
    assert account.profile_number == 2
    assert account.address == 'address'
    assert account.password is None
    assert account.private_key is None
    assert account.seed is None
    assert account.proxy is None

