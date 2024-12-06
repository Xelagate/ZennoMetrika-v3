'''## Задача 1 - light

1. Создайте класс Account, который имеет атрибуты:
- номер профиля
- адрес кошелька
- адрес суб аккаунта
- balance - баланс аккаунта (изначально 1000)
2. Создайте методы:
- init для инициализации атрибутов
- get_balance - возвращает баланс аккаунта, при запуске печатает "Баланс аккаунта {номер профиля}, {адрес кошелька} равен {баланс}"
- send_tx - принимает параметры: адрес кошелька и сумму, уменьшает баланс в атрибуте на сумму отправки, печатает в терминале
  "Транзакция на сумму {сумма} успешно отправлена на адрес {адрес кошелька}, баланс аккаунта {номер профиля}, {адрес кошелька} равен {баланс}"
'''
from __future__ import annotations


class Account:
    """ Модель аккаунта """

    def __init__(self, profile_number: int, wallet_address: str, sub_account_address: str):
        """

        :param profile_number: номер профиля
        :param wallet_address: адрес кошелька
        :param sub_account_address: адрес суб аккаунта на бирже
        """
        self.profile_number = profile_number
        self.wallet_address = wallet_address
        self.sub_account_address = sub_account_address
        self.balance = 1000

    def get_balance(self) -> float | int:
        """
        Получение баланса аккаунта
        :return: баланс аккаунта
        """
        print(f"Баланс аккаунта {self.profile_number}, {self.wallet_address} равен {self.balance}")
        return self.balance

    def send_tx(self, wallet_address: str, amount: float) -> None:
        """
        Отправка транзакции на указанный адрес кошелька, уменьшение баланса аккаунта на сумму транзакции
        :param wallet_address: адрес получателя
        :param amount: сумма транзакции
        :return: None
        """
        self.balance -= amount
        print(
            f"Транзакция на сумму {amount} успешно отправлена на адрес {wallet_address}, баланс аккаунта {self.profile_number}, {self.wallet_address} равен {self.balance}")
