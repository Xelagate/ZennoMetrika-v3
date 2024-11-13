'''## Задача 1 - light
### Условие:
- В конфиге указывается сколько кошельков нужно создать
- Программа создает список кошельков по введенному количеству (реализуйте одной строчкой кода).
- Программа создает список балансов кошельков, где баланс это случайное число от 1 до 1000 (реализуйте одной строчкой кода).
- Должно получиться 2 списка.
- Объедините 2 списка в словарь, где ключ это кошелек, а значение это баланс.
- Сделайте программу, которая будет умножать на 2 все четные значения балансов.
- Выведите конечный результат в формате "Кошелек {адрес}: баланс {баланс}", каждый элемент с новой строки.'''


import random

wallet_count = 100
wallets = ['0x' + ''.join(random.choices('0123456789abcdef', k=40)) for _ in range(wallet_count)]
balances = [random.randint(1, 1000) for _ in range(len(wallets))]
wallets_balances = dict(zip(wallets, balances))

for wallet, balance in wallets_balances.items():
    if balance % 2 == 0:
        wallets_balances[wallet] = balance * 2
    print(f'Кошелек {wallet}: баланс {wallets_balances[wallet]}')