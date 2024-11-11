'''
Посмотрите функцию random.choices(), используйте в генерации кошельков.
- создайте список из 100 кошельков одной строчкой кода с помощью генератора списков.
- создайте список из 100 рандомных балансов кошельков одной строчкой кода с помощью генератора списков.
- создайте список из 100 рандомных счетчиков транзакций 1 строчкой.
- перечислите все значения списков в терминале при помощи цикла for и zip(), в формате: "кошелек: баланс, транзакции"

'''

import random

wallets = ['0x' + ''.join(random.choices('0123456789abcdef', k=40)) for _ in range(100)]
balances = [random.randint(1, 10) for _ in range(100)]
tx_count = [random.randint(1, 3) for _ in range(100)]

for wallet, balance, tx in zip(wallets, balances, tx_count):
    print(f'{wallet}: {balance}, {tx}')
