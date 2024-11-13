'''

## Задача 2 - medium
### Условие
- В конфиге указывается сколько кошельков нужно создать
- Генерируется словарь, где ключ это кошелек, а значение словарь в котором:
  - баланс ETH (от 0.5 до 2.5)
  - баланс USDT (от 500 до 1500)
  - количество транзакций (от 5 до 25)
- необходимо сделать чтобы на каждом кошельке было минимум 30 транзакций
- сделайте так, чтобы после каждой транзакции брался другой кошелек, то есть не делать по несколько транзакций подряд на одном кошельке
- программа выбирает рандомный кошелек и делает свап ETH на USDT или наоборот
- при обменах должны меняться балансы токенов и количество транзакций
- когда все кошельки сделали минимум 30 транзакций программа завершается.
- сделайте чтобы программа писала в логе подробную информацию о работе
- стоимость эфира на момент транзакции должна быть от 2000 до 4000

'''

import random

# создаем кошельки
wallets_count = 100
wallets = ['0x' + ''.join(random.choices('0123456789abcdef', k=40)) for _ in range(wallets_count)]
wallets_data = dict()

# заполняем данными
for wallet in wallets:
    wallets_data[wallet] = {
        'ETH': random.uniform(0.5, 2.5),
        'USDT': random.randint(500, 1500),
        'txs': random.randint(5, 25)
    }
    print(wallet, wallets_data[wallet])


print('-------------------')
print('Запуск программы')
# пустой словарь для завершенных кошельков
complete_wallets = dict()

while wallets_data:
    # выбираем случайный кошелек
    wallet = random.choice(list(wallets_data.keys()))
    print(f'Выбран кошелек {wallet}')
    # выбираем из какого токена делать обмен
    from_token = random.choice(['ETH', 'USDT'])
    # генерируем случайную цену эфира
    eth_price = random.uniform(2000, 4000)
    # генерируем случайный процент для обмена
    random_percent = random.uniform(0.01, 0.10)
    print(f'Текущая цена эфира: {eth_price}')
    # делаем обмен в зависимости от выбранного токена и его наличия
    if from_token == 'ETH' and wallets_data[wallet]['ETH'] > 0.1:
        eth_amount = wallets_data[wallet]['ETH']
        eth_to_swap = eth_amount * random_percent
        usdt_amount = eth_to_swap * eth_price
        wallets_data[wallet]['ETH'] -= eth_to_swap
        wallets_data[wallet]['USDT'] += usdt_amount
        print(f'{wallet} Совершена транзакция: {eth_to_swap} ETH -> {usdt_amount} USDT')
    else:
        usdt_amount = wallets_data[wallet]['USDT']
        usdt_to_swap = usdt_amount * random_percent
        eth_amount = usdt_to_swap / eth_price
        wallets_data[wallet]['ETH'] += eth_amount
        wallets_data[wallet]['USDT'] -= usdt_to_swap
        print(f'{wallet} Совершена транзакция: {usdt_to_swap} USDT -> {eth_amount} ETH')

    # увеличиваем количество транзакций
    wallets_data[wallet]['txs'] += 1

    print(f'Баланс ETH: {wallets_data[wallet]["ETH"]}, Баланс USDT: {wallets_data[wallet]["USDT"]}')
    # если количество транзакций больше 30, то удаляем кошелек из словаря и добавляем в завершенные
    if wallets_data[wallet]['txs'] >= 30:
        print(f'Кошелек {wallet} завершил работу')
        complete_wallets[wallet] = wallets_data.pop(wallet)
    print('-------------------')

for wallet, data in complete_wallets.items():
    print(f'Кошелек {wallet} завершил работу с данными: {data}')
