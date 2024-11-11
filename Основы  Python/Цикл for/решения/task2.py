import random
'''
- Создайте список из 100 адресов кошельков.
- Создайте список в котором будут храниться рандомныe балансы кошельков.
- Скрипт должен проитерировать список при помощи цикла for и вывести каждый кошелек и его баланс в терминал.
- Используйте индексацию и переменную i.

'''
wallets = ['0x' + ''.join(random.choices('0123456789abcdef', k=40)) for _ in range(100)]
balances = [random.randint(1, 10) for _ in range(100)]

for i in range(len(wallets)):
    print(wallets[i], balances[i])
