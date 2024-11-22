'''
## Задача 4 - medium
### Условие:
- создайте список из 10 токенов.
- создайте список из 100 кошельков
- посмотрите функцию random.shuffle() и примените ее к списку кошельков.
- сделайте цикл который перебирает в рандомном порядке 100 кошельков и имитирует вывод с биржи по 3 рандомных токена для каждого кошелька.
- итерация по списку должна быть без использования индексации.

'''

import random

tokens = ['BTC', 'ETH', 'BNB', 'ADA', 'SOL', 'DOT', 'DOGE', 'LUNA', 'AVAX', 'UNI']
wallets = ['0x' + ''.join(random.choices('0123456789abcdef', k=40)) for _ in range(100)]
random.shuffle(wallets)

for wallet in wallets:
    for _ in range(3):
        token = random.choice(tokens)
        print(f'{wallet}: вывели {token}')