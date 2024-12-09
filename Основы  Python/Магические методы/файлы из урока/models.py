import random


class Account:
    """
    Класс для создания объекта аккаунта
    """

    def __init__(self, profile_number: int, password: str, private_key: str, address: str):
        """
        Конструктор класса
        :param profile_number: номер профиля
        :param password: пароль
        """
        self.profile_number = profile_number
        self.password = password
        self.private_key = private_key
        self.address = address
        self.transactions = ['1', '2', '3']
        self.balance = 0
        self.data = {'name': 'John', 'age': 30}
        self.file = open('data.txt', 'w')

    def send_transaction(self, token: str, amount: float):
        """
        Метод для отправки транзакции
        :param token: токен
        :param amount: количество
        """
        self.transactions.append({'token': token, 'amount': amount})
        print(f'Отправлена транзакция на сумму {amount} {token}')

    def add_balance(self, amount: float):
        self.balance += amount
        print(f'Баланс увеличен на {amount} и составляет {self.balance}')

    def __str__(self):
        return f'Аккаунт {self.profile_number}, адрес: {self.address}'

    def __repr__(self):
        return f'Account(profile_number={self.profile_number}, password={self.password}, private_key={self.private_key}, address={self.address})'

    def __len__(self):
        return len(self.transactions)

    def __add__(self, other):
        return self.balance + other

    def __sub__(self, other):
        return self.balance - other

    def __mul__(self, other):
        return self.balance * other

    def __truediv__(self, other):
        return self.balance / other

    def __floordiv__(self, other):
        return self.balance // other

    def __mod__(self, other):
        return self.balance % other

    def __pow__(self, other):
        return self.balance ** other

    def __radd__(self, other):
        return self.balance + other

    def __rsub__(self, other):
        return self.balance - other

    def __rmul__(self, other):
        return self.balance * other

    def __rtruediv__(self, other):
        return self.balance / other

    def __rfloordiv__(self, other):
        return self.balance // other

    def __rmod__(self, other):
        return self.balance % other

    def __rpow__(self, other):
        return self.balance ** other

    def __iadd__(self, other):
        self.balance += other
        return self

    def __eq__(self, other) -> bool:
        """
        Метод для сравнения объектов аккаунтов оператором ==.
        :param other: объект для сравнения
        :return: результат сравнения
        """
        if isinstance(other, Account):
            return self.profile_number == other.profile_number and self.password == other.password and self.private_key == other.private_key and self.address == other.address
        elif isinstance(other, int):
            return self.profile_number == other
        elif isinstance(other, str):
            return self.address == other

        return False

    def __ne__(self, other) -> bool:
        """
        Метод для сравнения объектов аккаунтов оператором !=.
        :param other: объект для сравнения
        :return: результат сравнения
        """
        return not self.__eq__(other)

    def __lt__(self, other) -> bool:
        """
        Метод для сравнения объектов аккаунтов оператором <.
        :param other: объект для сравнения
        :return: результат сравнения
        """
        if isinstance(other, Account):
            return self.profile_number < other.profile_number
        elif isinstance(other, int):
            return self.profile_number < other
        return False

    def __gt__(self, other):
        """
        Метод для сравнения объектов аккаунтов оператором >.
        :param other: объект для сравнения
        :return: результат сравнения
        """
        if isinstance(other, Account):
            return self.profile_number > other.profile_number
        elif isinstance(other, int):
            return self.profile_number > other
        return False

    def __le__(self, other):
        """
        Метод для сравнения объектов аккаунтов оператором <=.
        :param other: объект для сравнения
        :return: результат сравнения
        """
        if isinstance(other, Account):
            return self.profile_number <= other.profile_number
        elif isinstance(other, int):
            return self.profile_number <= other
        return False

    def __ge__(self, other):
        """
        Метод для сравнения объектов аккаунтов оператором >=.
        :param other: объект для сравнения
        :return: результат сравнения
        """
        if isinstance(other, Account):
            return self.profile_number >= other.profile_number
        elif isinstance(other, int):
            return self.profile_number >= other
        return False

    def __int__(self):
        return int(self.balance)

    def __float__(self):
        return float(self.balance)

    #
    # def __getitem__(self, key):
    #
    #     if isinstance(key, int):
    #         args_list = [self.profile_number, self.password, self.private_key, self.address]
    #         return args_list[key]
    #
    #     if key == 'balance':
    #         print(f'Баланс аккаунта: {self.balance}')
    #         return self.balance
    #
    #     elif key == 'profile_number':
    #         return self.profile_number
    #
    #
    #     if key in self.data:
    #         return self.data[key]
    #
    #     return None

    def __setitem__(self, key, value):
        if isinstance(key, int):
            args_list = [self.profile_number, self.password, self.private_key, self.address]
            args_list[key] = value

        if key == 'balance':
            self.balance = value
        elif key == 'profile_number':
            self.profile_number = value
        elif key == 'password':
            self.password = value


    def __iter__(self):
        self._index = 0
        self._args = [self.profile_number, self.password, self.private_key, self.address]
        return self


    def __next__(self):
        if self._index < len(self._args):
            value = self._args[self._index]
            self._index += 1
            return value
        else:
            raise StopIteration


    def __contains__(self, item) -> bool:
        args_list = [self.profile_number, self.password, self.private_key, self.address]
        return item in args_list

    def __enter__(self):
        print('Аккаунт создан', self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print('Файл закрыт')
        return True




account = Account(950, 'qwerty', '1234567890', '0x1234567890')
account2 = Account(950, 'qwerty', '1234567890', '0x1234567890')

print(f'Запустили в работу {account}')

print(repr(account))

account.send_transaction('USDT', 100)
account.send_transaction('USDT', 100)
account.send_transaction('USDT', 100)
account.send_transaction('USDT', 100)
account.send_transaction('USDT', 100)
account.send_transaction('USDT', 100)
account.send_transaction('USDT', 100)
account.send_transaction('USDT', 100)
account.send_transaction('USDT', 100)
print(f'len(account) - {len(account)}')

account.balance = 1000
account2.balance = 2000

print(account + 1)
print(account - 10)
print(account * 10)
print(account / 10)
print(account // 10)
print(account % 10)
print(account ** 10)

print(10 + account)
print(10 - account)
print(10 * account)
print(10 / account)
print(10 // account)
print(10 % account)
print(10 ** account)

print(account + account2)

account += 100
print(account.balance)

account_3 = Account(951, 'qwerty', '1234567890', '0x1234567890')
account_4 = Account(951, 'qwerty', '1234567890', '0x1234567890')

print(account_3 == '0x1234567890')

print(int(account))
print(float(account))

# print(account[1])

account['password'] = 'sjnsdjfs'

print('*' * 50)
print()



for value in account:
    print(value)


tx_hash = '0x1234567ff890'

print(tx_hash in account)


with Account(950, 'qwerty', '1234567890', '0x1234567890') as account:
    print(account, 'в работе')




















