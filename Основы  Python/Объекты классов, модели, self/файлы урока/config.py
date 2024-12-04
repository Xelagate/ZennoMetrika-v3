import random


class Account:
    """
    Класс для хранения данных об аккаунте

    Аргументы:

    - profile_number (int) - номер профиля
    - password (str) - пароль
    - private_key (str) - приватный ключ
    - seed (str) - мнемоническая фраза
    - proxy (str) - прокси

    """
    profile_number: int = 949
    password: str = 'qwerty'
    private_key: str = '1234567890'
    seed: str = 'one two three four five six seven eight nine ten eleven twelve'
    proxy: str = 'https://proxy.com:8080'

    @staticmethod
    def balance_account(address: str) -> int:
        """
        Метод для получения баланса аккаунта

        Аргументы:

        - address (str) - адрес аккаунта

        Возвращает:

        - int - баланс аккаунта

        """
        print(f'Get balance for address: {address}')
        return random.randint(0, 1000)




class Config:
    """
    Класс для хранения данных о конфигурации

    Аргументы:

    - timeout (int) - время ожидания
    - is_random (bool) - случайное значение

    """

    timeout: int = 10
    is_random: bool = False

class Tokens:
    class Ethereum:
        usdt = {'address': '0xdac17f958d2ee523a2206206994597c13d831ec7', 'decimals': 6, 'symbol': 'USDT'}
        usdc = {'address': '0x1234567890', 'decimals': 6, 'symbol': 'USDC'}

    class BSC:
        usdt = {'address': '0x55d398326f99059ff775485246999027b3197955', 'decimals': 18, 'symbol': 'USDT'}
        usdc = {'address': '0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d', 'decimals': 18, 'symbol': 'USDC'}


class Contracts:
    uniswap_contract = '0x7a250d5630b4cf539739df2c5dacb4c659f2488d'
    sushiswap_contract = '0xc0aee478e3658e2610c5f7a4a2e1777ce9e4f2ac'
    curve_contract = '0x45f783cce6b7ff23b2ab2d70e416cdb7d6055f51'

class RPC:
    ethereum_rpc = 'https://mainnet.infura.io/v3/'
    bsc_rpc = 'https://bsc-dataseed.binance.org/'
    polygon_rpc = 'https://polygon-rpc.com/'
