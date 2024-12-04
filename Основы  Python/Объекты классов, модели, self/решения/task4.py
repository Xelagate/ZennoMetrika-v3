
'''

## Задача 4 - hard

### Условие:
1. Создайте класс контейнер, который хранит типы токенов: ERC20, NATIVE, STABLE, в виде атрибутов со значениями 'erc20', 'native', 'stable'.
2. Создайте класс контейнер Tokens, в котором будут храниться объекты класса Token.
3. Создайте модель Token, который принимает:
- символ токена, в атрибуте должен быть записан в верхнем регистре
- адрес смарт контракта, в атрибуте должен быть записан в нижнем регистре
- сеть токена (указывается как объект класса Chain, например Chains.Ethereum)
- decimals (количество знаков после запятой, можно посмотреть в эксплорере блокчейна), в атрибуте должен быть записан в формате int, по умолчанию 18
- тип токена (указывается как объект класса TokenTypes, например TokenTypes.ERC20), по умолчанию 'erc20'
4. Заполните контейнер Tokens объектами класса Token с реальынми данными, для токенов:
- USDT в сети Ethereum
- USDC в сети BSC
- USDC в сети zkSync


Заполните документацию к классам и методам инициализации.



'''
from typing import Optional
from task3 import Chains, Chain


class TokenTypes:
    """
    Класс для хранения типов токенов
    """
    ERC20 = 'erc20'
    NATIVE = 'native'
    STABLE = 'stable'


class Token:
    """
    Класс для хранения информации о токене.
    """
    def __init__(
            self,
            symbol: str,
            address: str,
            chain: Chain,
            decimals: int = 18,
            type_token: str = TokenTypes.ERC20,
    ):
        self.symbol = symbol
        self.address = address
        self.chain = chain
        self.decimals = decimals if isinstance(decimals, int) else int(decimals)
        self.type_token = type_token

class Tokens:
    """
    Класс для хранения объектов класса Token.
    """
    USDT_ETHEREUM = Token(
        symbol='USDT',
        address='0xdac17f958d2ee523a2206206994597c13d831ec7',
        chain=Chains.ethereum,
        type_token=TokenTypes.STABLE,
        decimals=6
    )


    USDC_BSC = Token(
        symbol='USDC',
        address='0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d',
        chain=Chains.bsc,
        type_token=TokenTypes.STABLE,
        decimals=6
    )

    USDC_ZKSYNC = Token(
        symbol='USDC',
        address='0x1d17CBcF0D6D143135aE902365D2E5e2A16538D4',
        chain=Chains.zksync,
        type_token=TokenTypes.STABLE,
        decimals=6
    )

def test():
    assert Tokens.USDT_ETHEREUM.symbol == 'USDT'
    assert Tokens.USDT_ETHEREUM.address == '0xdac17f958d2ee523a2206206994597c13d831ec7'
    assert Tokens.USDT_ETHEREUM.chain == Chains.ethereum
    assert Tokens.USDT_ETHEREUM.decimals == 6
    assert Tokens.USDT_ETHEREUM.type_token == TokenTypes.STABLE

    assert Tokens.USDC_BSC.symbol == 'USDC'
    assert Tokens.USDC_BSC.address == '0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d'
    assert Tokens.USDC_BSC.chain == Chains.bsc
    assert Tokens.USDC_BSC.decimals == 6
    assert Tokens.USDC_BSC.type_token == TokenTypes.STABLE

    assert Tokens.USDC_ZKSYNC.symbol == 'USDC'
    assert Tokens.USDC_ZKSYNC.address == '0x1d17CBcF0D6D143135aE902365D2E5e2A16538D4'
    assert Tokens.USDC_ZKSYNC.chain == Chains.zksync
    assert Tokens.USDC_ZKSYNC.decimals == 6
    assert Tokens.USDC_ZKSYNC.type_token == TokenTypes.STABLE

    assert isinstance(Tokens.USDT_ETHEREUM.decimals, int)

    weth = Token(
        symbol='WETH',
        address='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
        chain=Chains.ethereum,
        type_token=TokenTypes.ERC20,
        decimals='18'
    )
    assert weth.symbol == 'WETH'
    assert weth.address == '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'
    assert weth.chain == Chains.ethereum
    assert weth.decimals == 18
    assert weth.type_token == TokenTypes.ERC20
    assert isinstance(weth.decimals, int)
