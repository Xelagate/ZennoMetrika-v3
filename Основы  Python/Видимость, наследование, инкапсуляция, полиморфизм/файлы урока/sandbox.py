import random


class Dex:
    contract_address = ''

    def swap(self, src_token: str, dst_token: str, amount: float) -> None:
        self._connect_contract()
        print(f'Swapping {amount} {src_token} for {dst_token}, contract: {self.contract_address}, dex: {self.__class__.__name__}')


    def _connect_contract(self):
        print('Connecting to contract', self.contract_address)


class Uniswap(Dex):
    contract_address = 'контракт унисвапа'

    def swap(self, src_token: str, dst_token: str, amount: float) -> None:
        print('особенная логика для унисвапа')
        self._connect_contract()
        print(
            f'Swapping {amount} {src_token} for {dst_token}, contract: {self.contract_address}, dex: {self.__class__.__name__}')


class PancakeSwap(Dex):
    contract_address = 'контракт панкейксвапа'


class SushiSwap(Dex):
    contract_address = 'контракт суши свапа'


dexes = [Uniswap(), PancakeSwap(), SushiSwap()]
random.shuffle(dexes)

for dex in dexes:
    dex.swap('ETH', 'USDT', 1.5)




