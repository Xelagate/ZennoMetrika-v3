
'''

## Задача 3 - medium
1. Создайте класс контейнер Chains, в котором будут храниться объекты класса Chain.

2. Создайте класс модель Chain, который принимает:
- название сети
- url адрес rpc ноды
- id блокчейна
- имя сети для добавления в метамаск (необязательный аргумент) - если не указан используется название сети
- тикер нативного токена - по умолчанию 'ETH'

3. Заполните контейнер Chains объектами класса Chain, для сетей Ethereum, BSC, Arbitrum, zkSync

Заполните документацию к классам и методам инициализации.

'''
from typing import Optional



class Chain:
    """
    Класс для хранения информации о сети. Информацию о сети можно искать тут https://chainid.network/chains.json
    """

    def __init__(
            self,
            name: str,
            rpc: str,
            chain_id: int,
            metamask_name: Optional[str] = None,
            native_token: str = 'ETH',
    ):
        """
        :param name: наименование сети
        :param rpc: адрес провайдера в формате https://1rpc.io/eth, можно взять на https://chainlist.org/
        :param chain_id: id сети, например 1 для Ethereum, можно искать тут https://chainid.network/chains.json
        :param metamask_name: название сети в metamask, по умолчанию берется из параметра name
        :param native_token: тикер нативного токена сети, по умолчанию 'ETH'
        """
        self.name = name
        self.rpc = rpc
        self.chain_id = chain_id
        self.metamask_name = metamask_name if metamask_name else name
        self.native_token = native_token

class Chains:
    """
    Класс для хранения информации о сетях.
    """
    ethereum = Chain(
        name='ethereum',
        rpc='https://1rpc.io/eth',
        chain_id=1,
        metamask_name='Ethereum'
    )

    bsc = Chain(
        name='bsc',
        rpc='https://1rpc.io/bsc',
        chain_id=56,
        metamask_name='Binance Smart Chain',
        native_token='BNB'
    )

    arbitrum = Chain(
        name='arbitrum',
        rpc='https://1rpc.io/arb',
        chain_id=42161,
        metamask_name='Arbitrum One'
    )

    zksync = Chain(
        name='zksync',
        rpc='https://1rpc.io/zksync2-era',
        chain_id=324,
        metamask_name='zkSync'
    )

def test():
    chains = Chains()
    assert chains.ethereum.name == 'ethereum'
    assert chains.ethereum.rpc == 'https://1rpc.io/eth'
    assert chains.ethereum.chain_id == 1
    assert chains.ethereum.metamask_name == 'Ethereum'
    assert chains.ethereum.native_token == 'ETH'

    assert chains.bsc.name == 'bsc'
    assert chains.bsc.rpc == 'https://1rpc.io/bsc'
    assert chains.bsc.chain_id == 56
    assert chains.bsc.metamask_name == 'Binance Smart Chain'
    assert chains.bsc.native_token == 'BNB'

    assert chains.arbitrum.name == 'arbitrum'
    assert chains.arbitrum.rpc == 'https://1rpc.io/arb'
    assert chains.arbitrum.chain_id == 42161
    assert chains.arbitrum.metamask_name == 'Arbitrum One'
    assert chains.arbitrum.native_token == 'ETH'

    assert chains.zksync.name == 'zksync'
    assert chains.zksync.rpc == 'https://1rpc.io/zksync2-era'
    assert chains.zksync.chain_id == 324
    assert chains.zksync.metamask_name == 'zkSync'
    assert chains.zksync.native_token == 'ETH'