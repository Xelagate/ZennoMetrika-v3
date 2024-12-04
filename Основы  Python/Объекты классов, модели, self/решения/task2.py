
'''

## Задача 2 - lite
### Условие:
Создайте класс 'Balance', который принимает:
- баланс в float
- название токена в str
- стоимость токена в $ в float

У объектов созданных по данному классу должны быть атрибуты:
- баланс в токене
- баланс в токене округленный до 2 знаков после запятой
- название токена
- стоимость токена в $
- баланс в $

Баланс токена в $ должен вычисляться в момент инициализации объекта.

Заполните документацию к классу и методу инициализации.
'''
from typing import Optional

class Balance:
    """Класс для создания объектов для хранения информации о балансе токена.

    Атрибуты объекта:
    balance - баланс в токенах
    balance_round - баланс в токенах округленный до 2 знаков после запятой
    token_name - название токена
    token_price - стоимость токена в $
    balance_in_usd - баланс в $, вычисляется в момент инициализации объекта на основе balance и token_price
    """

    def __init__(self, balance: float, token_name: str, token_price: float) -> None:
        """
        Инициализация объекта класса Balance.

        :param balance: баланс в токенах
        :param token_name: название токена
        :param token_price: стоимость токена в $
        """
        self.balance = balance
        self.balance_round = round(balance, 2)
        self.token_name = token_name
        self.token_price = token_price
        self.balance_in_usd = round(balance * token_price, 2)


def test():

    eth_balance = Balance(1.5515615, 'ETH', 3500)
    assert eth_balance.balance == 1.5515615
    assert eth_balance.balance_round == 1.55
    assert eth_balance.token_name == 'ETH'
    assert eth_balance.token_price == 3500
    assert eth_balance.balance_in_usd == round(1.5515615 * 3500, 2)

