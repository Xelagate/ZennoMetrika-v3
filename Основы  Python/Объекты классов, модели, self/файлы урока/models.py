class Account:
    """
    Класс для создания объекта аккаунта
    """

    def __init__(self, profile_number: int, password: str, private_key: str):
        """
        Конструктор класса
        :param profile_number: номер профиля
        :param password: пароль
        :param private_key: приватный ключ
        """
        self.profile_number = profile_number
        self.password = password
        self.private_key = private_key


class Token:
    """
    Класс для создания объекта токена
    """
    def __init__(self, address: str, decimals: int, symbol: str):
        """
        Конструктор класса
        :param address: адрес токена
        :param decimals: количество знаков после запятой
        :param symbol: символ токена
        """
        self.address = address
        self.decimals = decimals
        self.symbol = symbol


class Tokens:

    usdt = Token('0xdac17f958d2ee523a2206206994597c13d831ec7', 6, 'USDT')
    usdc = Token('0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d', 6, 'USDC')




class Chain:
    def __init__(arbitrum, name: str, rpc: str, chain_id: int):
        arbitrum.name = name
        arbitrum.rpc = rpc
        arbitrum.chain_id = chain_id


class Chains:
    ethereum = Chain('Ethereum', 'https://mainnet.infura.io/v3/your_infura_id', 1)
    arbitrum = Chain('Arbitrum', 'https://arb1.arbitrum.io/rpc', 42161)







# class Account:
#     """
#     Статичный класс для хранения данных об аккаунте
#
#     Аргументы:
#
#     - profile_number (int) - номер профиля
#     - password (str) - пароль
#     - private_key (str) - приватный ключ
#     - seed (str) - мнемоническая фраза
#     - proxy (str) - прокси
#
#     """
#     profile_number: int = 949
#     password: str = 'qwerty'
#     private_key: str = '1234567890'
#     seed: str = 'one two three four five six seven eight nine ten eleven twelve'
#     proxy: str = 'https://proxy.com:8080'
