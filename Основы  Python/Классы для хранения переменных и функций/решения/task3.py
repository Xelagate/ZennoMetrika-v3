"""
Создайте класс Onchain, который содержит статические методы и переменные для работы с блокчейном:
- класс с перечислением токенов USDT и USDC в сети Arbitrum, Ethereum, Binance Smart Chain и их адреса смартконтрактов
- класс с перечислением сетей Arbitrum, Ethereum, Binance Smart Chain и RPC url адресами
- метод получение баланса, который принимает rpc url, адрес кошелька и адрес токена, возвращает баланс (рандомный)
- метод перевода баланса, который принимает rpc url, адрес кошелька получателя и адрес токена и сумму, печатает в терминале сообщение о переводе
- метод для получения цены газа, который принимает rpc url и возвращает цену газа (рандомную)

"""
import random


class Onchain:
    """
    Класс для хранения данных о блокчейне и работе с ним.

    """


    class Tokens:
        """
        Класс для хранения данных о токенах, разделенных по сетям.
        """
        class Ethereum:
            """
            Класс для хранения данных о токенах в сети Ethereum.
            """
            usdt = {'address': '0xdac17f958d', 'decimals': 6, 'symbol': 'USDT'}
            usdc = {'address': '0x1234567890', 'decimals': 6, 'symbol': 'USDC'}

        class Arbitrum:
            """
            Класс для хранения данных о токенах в сети Arbitrum.
            """
            usdt = {'address': '0xdac17f958d', 'decimals': 6, 'symbol': 'USDT'}
            usdc = {'address': '0x123456', 'decimals': 6, 'symbol': 'USDC'}

        class BinanceSmartChain:
            """
            Класс для хранения данных о токенах в сети Binance Smart Chain.
            """
            usdt = {'address': '0xdac17f958d', 'decimals': 6, 'symbol': 'USDT'}
            usdc = {'address': '0x123456', 'decimals': 6, 'symbol': 'USDC'}


    class Chains:
        """
        Класс для хранения данных о сетях и их RPC url адресах.
        """
        Ethereum = 'https://mainnet.infura.io/v3/1234567890'
        Arbitrum = 'https://arb1.arbitrum.io/rpc'
        BinanceSmartChain = 'https://bsc-dataseed.binance.org/'


    @staticmethod
    def balance_account(rpc_url: str, address: str, token_address: str) -> int:
        """
        Метод для получения баланса аккаунта.
        :param rpc_url: url адрес RPC
        :param address: адрес аккаунта
        :param token_address: адрес токена
        :return: баланс аккаунта
        """
        print(f'Get balance for address: {address}, token: {token_address}, rpc_url: {rpc_url}')
        return random.randint(0, 1000)

    @staticmethod
    def transfer_balance(rpc_url: str, recipient_address: str, token_address: str, amount: int) -> None:
        """
        Метод для перевода баланса.
        :param rpc_url: url адрес RPC
        :param recipient_address: адрес получателя
        :param token_address: адрес токена
        :param amount: сумма
        :return: None
        """
        print(f'Transfer {amount} tokens of {token_address} to address: {recipient_address}, rpc_url: {rpc_url}')

    @staticmethod
    def gas_price(rpc_url: str) -> int:
        """
        Метод для получения цены газа.
        :param rpc_url: url адрес RPC
        :return: цена газа
        """
        print(f'Get gas price, rpc_url: {rpc_url}')
        return random.randint(1, 100)