""""""

"""
Задача 1 - light

Создайте класс Token, который будет содержать следующие атрибуты:
- address: str
- decimals: int
- symbol: str

- реализуйте магический метод сравнения у класса токен, который будет сравнивать объекты 
токенов по адресу токена
"""

class Token:

    def __init__(self, address: str, decimals: int, symbol: str):
        self.address = address
        self.decimals = decimals
        self.symbol = symbol

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.address == other.address
        return False


"""
Задача 2 - medium

Создайте класс Chain, который будет содержать следующие атрибуты:
- name: str
- rpc: str
- chain_id: int

Создайте магический метод сравнения у класса Chain, который будет сравнивать объекты 
сетей по идентификатору цепочки

Добавьте в класс Token созданный выше атрибуты:
- chain: Chain

Переделайте магический метод сравнения у класса токен, который будет сравнивать
объекты токенов по всем 4 атрибутам одновременно.

"""

class Chain:

        def __init__(self, name: str, rpc: str, chain_id: int):
            self.name = name
            self.rpc = rpc
            self.chain_id = chain_id

        def __eq__(self, other):
            if isinstance(other, Chain):
                return self.chain_id == other.chain_id
            return False

class Token:

        def __init__(self, address: str, decimals: int, symbol: str, chain: Chain):
            self.address = address
            self.decimals = decimals
            self.symbol = symbol
            self.chain = chain

        def __eq__(self, other):
            if isinstance(other, Token):
                return self.address == other.address and self.decimals == other.decimals and self.symbol == other.symbol and self.chain == other.chain
            return False

"""
Задача 3 - hard

Создайте класс Logger, который будет содержать следующие атрибуты, передаваемые при инициализации:
- account: Account - аккаунт, который будет использоваться для логирования, должен содержать
номер профиля и адрес кошелька
- file - файл, в который будут записываться логи
- file_name - имя файла, в который будут записываться логи

Создайте магический метод __enter__ и __exit__ у класса Logger, который будет открывать и закрывать файл
Реализуйте метод log у класса Logger, который будет записывать в файл переданный текст.

Напишите пример использования создания объекта класса Logger и записи в файл логов.
Записи в лог должны записываться следующим образом:
log.log('Open browser')

В файле должно быть записано:
Аккаунт: 1, Адрес: 0x1234567890abcdef - Open browser
"""

class Account:
    def __init__(self, profile_number: int, address: str):
        self.profile_number = profile_number
        self.address = address


class Logger:

    def __init__(self, account: Account, file_name: str):
        self.account = account
        self.file_name = file_name
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return True

    def log(self, text):
        self.file.write(f'Аккаунт: {self.account.profile_number}, Адрес: {self.account.address} - {text}\n')


account = Account(1, '0x1234567890abcdef')
with Logger(account, 'log.txt') as log:
    log.log('Open browser')

