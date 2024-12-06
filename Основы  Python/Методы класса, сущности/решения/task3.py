'''
## Задача 3 - hard

1. Создайте класс Account, который имеет:
- атрибут номер профиля
- атрибут адрес кошелька
- атрибут адрес суб аккаунта
- атрибут баланс аккаунта (изначально 0)
- метод init для инициализации атрибутов
- метод get_balance для возврата баланса аккаунта из атрибута баланс
- метод send_token для отправки токена, принимает параметры: адрес кошелька и сумму, уменьшает баланс аккаунта на сумму транзакции
- метод withdraw_to_sub для отправки транзакции на указанную сумму на адрес суб аккаунта, для отправки внутри метода используйте метод send_token

2. Создайте класс Exchange, который имеет атрибуты:
- account - объект класса Account
- main_balance - баланс биржи (изначально 10000)
- sub_balance - баланс суб аккаунтов (изначально 0)
3. Создайте методы:
- init для инициализации атрибутов
- withdraw - метод для вывода токена с баланса биржи, принимает сумму вывода, уменьшает баланс биржи на сумму вывода, увеличивает баланс аккаунта на сумму вывода
- popup_sub_balance - метод для пополнения баланса суб аккаунта после вывода токена с кошелька, увеличивает балаанс суб аккаунта на сумму пополнения
- collect_from_sub_to_main - метод для сбора токенов с суб аккаунтов на главный аккаунт, уменьшает баланс суб аккаунтов на сумму сбора, увеличивает баланс биржи на сумму сбора

4. Напишите скрипт, который будет:
- извлекать из 3 текстовых файлов данные с номером профиля, адресом кошелька, адресом суб аккаунта
- создавать список объектов класса Account
- в цикле берет аккаунт из списка, создает объект класса Exchange и передает в него аккаунт
- делает вывод ~90% доступного баланса биржи на баланс аккаунта
- при выводе минусуйте с баланса биржи комиссию 0.1% от суммы вывода
- ждет 2-3 секунды
- делает вывод с кошелька всей суммы с кошелька на суб аккаунт, оставляя на балансе 5-10 токенов
- пополните баланс суб аккаунта на отправленную сумму
- делает сбор с суб аккаунта на баланс биржи
- запускает следующий цикл

- Задача прогнать объем токенов через все аккаунты, оставив на балансе аккаунтов по 5-10 токенов.
- Каждая операция с балансами должна уменьшать и увеличивать соответствующие балансы на указанные суммы.
- В конце необходимо будет посчитать сколько суммарно осталось токенов на балансах аккаунтов запрашивая баланс через метод get_balance
- В конце необходимо будет вывести оставшийся баланс на бирже и суб аккаунте
'''

from __future__ import annotations

import random
import time


class Account:

    def __init__(self, profile_number: int, wallet_address: str, sub_account_address: str):
        """
        Инициализация атрибутов, так же устанавливает баланс аккаунта в 0
        :param profile_number:  номер профиля
        :param wallet_address: адрес кошелька
        :param sub_account_address: адрес суб аккаунта
        """
        self.profile_number = profile_number
        self.wallet_address = wallet_address
        self.sub_account_address = sub_account_address
        self.balance = 0

    def get_balance(self) -> float | int:
        """
        Получение баланса аккаунта из атрибута
        :return: баланс аккаунта
        """
        print(f"Баланс аккаунта {self.profile_number}, {self.wallet_address} равен {self.balance}")
        return self.balance

    def send_token(self, wallet_address: str, amount: float) -> None:
        """
        Отправка токена на указанный адрес, уменьшение баланса аккаунта на сумму транзакции
        :param wallet_address: адрес кошелька
        :param amount: сумма транзакции
        :return: None
        """
        self.balance -= amount
        print(
            f"Транзакция на сумму {amount} успешно отправлена на адрес {wallet_address}, баланс аккаунта {self.profile_number}, {self.wallet_address} равен {self.balance}")

    def withdraw_to_sub(self, amount: float) -> None:
        """
        Отправка транзакции на указанный адрес суб аккаунта, уменьшение баланса аккаунта на сумму транзакции
        :param amount: сумма транзакции
        :return: None
        """
        print(f"Отправка транзакции на сумму {amount} на адрес субаккаунт {self.sub_account_address}")
        self.send_token(self.sub_account_address, amount)


class Exchange:

    def __init__(self, account: Account):
        """
        Инициализация атрибутов, принимает объект класса Account
        :param account: объект класса Account
        """
        self.account = account
        self.main_balance = 10000
        self.sub_balance = 0

    def withdraw(self, amount: float) -> None:
        """
        Вывод токена с баланса биржи, уменьшение баланса биржи на сумму вывода, увеличение баланса аккаунта на сумму вывода
        :param amount: сумма вывода
        :return: None
        """
        commission = amount * 0.001
        if self.main_balance < amount + commission:
            print("Недостаточно средств на балансе биржи, выводим 90% баланса за вычетом комиссии")
            amount = self.main_balance * 0.9
            commission = amount * 0.001

        self.main_balance -= amount + commission
        self.account.balance += amount
        print(f"Вывод на сумму {amount} успешно прошел, комиссия составила {commission}")

    def popup_sub_balance(self, amount: float) -> None:
        """
        Пополнение баланса суб аккаунта, увеличение баланса суб аккаунта на сумму транзакции
        :param amount: сумма транзакции
        :return: None
        """
        self.sub_balance += amount
        print(f"Пополнение суб аккаунта на сумму {amount} прошло успешно")

    def collect_from_sub_to_main(self) -> None:
        """
        Перевод токенов с суб аккаунтов на главный аккаунт, уменьшение баланса суб аккаунтов, увеличение баланса биржи
        :return: None
        """
        if self.sub_balance > 0:
            self.main_balance += self.sub_balance
            self.sub_balance = 0
            print(f"Сбор с суб аккаунта на главный аккаунт прошел успешно")


def get_list_from_file(file_name: str) -> list:
    """
    Получение списка из файла, где каждая строка это элемент списка
    :param file_name: имя файла
    :return: список строк
    """
    with open(file_name) as f:
        return f.read().splitlines()
def main():
    profiles = []
    profile_numbers = get_list_from_file("profile_numbers.txt")
    wallet_addresses = get_list_from_file("wallet_addresses.txt")
    sub_account_addresses = get_list_from_file("sub_account_addresses.txt")

    for profile_number, wallet_address, sub_account_address in zip(profile_numbers, wallet_addresses, sub_account_addresses):
        profiles.append(Account(profile_number, wallet_address, sub_account_address))

    for profile in profiles:
        # Создаем объект класса Exchange и передаем в него аккаунт
        exchange = Exchange(profile)
        # Выводим 90% доступного баланса биржи на баланс аккаунта
        amount_from_cex = exchange.main_balance * 0.9
        # Выводим токены с баланса биржи на баланс аккаунта
        exchange.withdraw(amount_from_cex)
        # Ждем 2-3 секунды
        time.sleep(random.randint(2, 3))
        # получаем баланс аккаунта
        balance = profile.get_balance()
        # Оставляем на балансе 5-10 токенов и отправляем остальные на суб аккаунт
        amount_to_sub = balance - random.randint(5, 10)
        # Отправляем токены на суб аккаунт
        profile.withdraw_to_sub(amount_to_sub)
        # Пополняем баланс суб аккаунта на отправленную сумму
        exchange.popup_sub_balance(amount_to_sub)
        # Собираем токены с суб аккаунта на главный аккаунт
        exchange.collect_from_sub_to_main()
