""""""

"""
Задача 1 - easy

Создайте класс Account, который имеет атрибут номер профиля
Создайте класс наследник AccountMetamask, который имеет атрибуты номер профиля и пароль.
Создайте класс AccountOnchain, который имеет атрибуты номер профиля и адрес кошелька.
AccountMetamask и AccountOnchain должны наследовать атрибут номер профиля от класса Account.

"""

class Account:
    def __init__(self, profile_number):
        self.profile_number = profile_number

class AccountMetamask(Account):
    def __init__(self, profile_number, password):
        super().__init__(profile_number)
        self.password = password

class AccountOnchain(Account):
    def __init__(self, profile_number, address):
        super().__init__(profile_number)
        self.address = address


"""
Задача 2 - middle

Создайте класс Account, который имеет защищенный атрибут _balance.
Напишите геттер и сеттер для атрибута _balance.
Сеттер должен проверять, что в атрибут balance записывается число,
если переданы числа как строки, то преобразовывать их в числа.

Убедитесь, что вы можете получить доступ к атрибуту _balance через геттер и сеттер.

account = Account()
account.balance = '100'
print(account.balance)  # 100

"""
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, str):
            value = int(value)
        elif not isinstance(value, (int, float)):
            raise ValueError('Balance must be a number')
        self._balance = value

account = Account()
account.balance = '100'
print(account.balance)  # 100

"""
Задача 3 - hard

У вас есть 3 биржи:
- Binance - есть токены USDT, BTC, ETH
- Okx - есть токены USDC, ZRO, ZK
- Bybit - есть токены DAI, LINK, UNI

Создайте класс Exchange, который принимает в качестве аргумента объект AccountOnchain.
Создайте атрибут класса, который будет хранить список токенов, которые есть на бирже.
Exchange должен иметь метод withdraw, который принимает название токена и количество токенов, которые
нужно вывести на кошелек из объекта AccountOnchain, имитируя вывод токенов с биржи, возвращает True, если вывод прошел успешно, иначе False.
У Exchange должен быть закрытый метод _check_token, который запускается в методе withdraw и проверяет, есть ли токен на бирже,
если токена нет, то завершает работу метода withdraw.

Создайте дочерние классы Binance, Okx, Bybit, которые наследуются от класса Exchange, которые наследуют атрибуты и методы класса Exchange.

Напишите скрипт, который:
- берет список из 9 токенов, которые есть на биржах
- создает объект AccountOnchain
- создает список объектов Binance, Okx, Bybit передавая в качестве аргумента объект AccountOnchain
- перемешивает список токенов, чтобы порядок был случайным
- запускает вывод каждого токена с каждой биржи, передавая в качестве аргументов название токена и количество токенов
- если биржа не поддерживает токен, то выбирать следующую биржу
- если вывод прошел успешно, то выбирать следующий токен
- скрипт должен сделать вывод всех токенов с соответствующих бирж.

Все методы должны быть реализованы в классe Exchange, а не в дочерних классах.
"""


import random

class Exchange:
    tokens = ['USDT', 'BTC', 'ETH', 'USDC', 'ZRO', 'ZK', 'DAI', 'LINK', 'UNI']

    def __init__(self, account):
        self.account = account

    def withdraw(self, token: str, amount: int) -> bool:
        """
        Вывод токена с биржи, если токен есть на бирже
        :param token: название токена
        :param amount: количество токенов
        :return: True, если вывод прошел успешно, иначе False
        """
        if self._check_token(token):
            print(f'Withdraw {amount} {token} from {self.__class__.__name__}')
            return True
        return False

    def _check_token(self, token):
        """
        Проверка наличия токена на бирже
        :param token: название токена
        :return: True, если токен есть на бирже, иначе False
        """
        if token in self.tokens:
            return True
        return False

class Binance(Exchange):
    tokens = ['USDT', 'BTC', 'ETH']

class Okx(Exchange):
    tokens = ['USDC', 'ZRO', 'ZK']

class Bybit(Exchange):
    tokens = ['DAI', 'LINK', 'UNI']

account = AccountOnchain(1, '0x1234567890')

exchanges = [Binance(account), Okx(account), Bybit(account)]

random.shuffle(Exchange.tokens)

for token in Exchange.tokens:
    for exchange in exchanges:
        if exchange.withdraw(token, 10):
            break



