"""
У вас есть 2 переменные с балансами кошелька в токене ETH и USDT.
Еще одна переменная описывает стоимость ETH в USDT.

Напишите программу, которая будет делать обмен из ETH в USDT если баланс USDT нулевой, при этом оставляя 5% токенов ETH на комиссии.

Если баланс USDT не нулевой, то программа должна делать обмен всех токенов USDT в ETH.

Во время обмена должно печататься в терминале какой токен меняется на какой и какая сумма обмена.
По результату обмена программа балансы должны меняться.

Продублируйте логику, чтобы программа делала 5 обменов из ETH в USDT и обратно, сама выбирая когда и какой обмен делать.

В конце работы программа должна выводить сообщение актуальный баланс токенов ETH и USDC.

"""

balance_eth = 1.35165161
balance_usdt = 505
price_eth = 3000

if balance_usdt == 0:
    commission = balance_eth * 0.05  # 5% на будущие комиссии
    eth_amount_in = balance_eth - commission  # сумма обмена ETH
    usdt_amount_out = eth_amount_in * price_eth # сумма обмена USDT
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    balance_usdt += usdt_amount_out
    balance_eth -= eth_amount_in
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    eth_amount_in = balance_usdt / price_eth
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    balance_eth += eth_amount_in
    balance_usdt = 0
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()

if balance_usdt == 0:
    commission = balance_eth * 0.05  # 5% на будущие комиссии
    eth_amount_in = balance_eth - commission  # сумма обмена ETH
    usdt_amount_out = eth_amount_in * price_eth # сумма обмена USDT
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    balance_usdt += usdt_amount_out
    balance_eth -= eth_amount_in
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    eth_amount_in = balance_usdt / price_eth
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    balance_eth += eth_amount_in
    balance_usdt = 0
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()
if balance_usdt == 0:
    commission = balance_eth * 0.05  # 5% на будущие комиссии
    eth_amount_in = balance_eth - commission  # сумма обмена ETH
    usdt_amount_out = eth_amount_in * price_eth # сумма обмена USDT
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    balance_usdt += usdt_amount_out
    balance_eth -= eth_amount_in
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    eth_amount_in = balance_usdt / price_eth
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    balance_eth += eth_amount_in
    balance_usdt = 0
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()
if balance_usdt == 0:
    commission = balance_eth * 0.05  # 5% на будущие комиссии
    eth_amount_in = balance_eth - commission  # сумма обмена ETH
    usdt_amount_out = eth_amount_in * price_eth # сумма обмена USDT
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    balance_usdt += usdt_amount_out
    balance_eth -= eth_amount_in
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    eth_amount_in = balance_usdt / price_eth
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    balance_eth += eth_amount_in
    balance_usdt = 0
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()
if balance_usdt == 0:
    commission = balance_eth * 0.05  # 5% на будущие комиссии
    eth_amount_in = balance_eth - commission  # сумма обмена ETH
    usdt_amount_out = eth_amount_in * price_eth # сумма обмена USDT
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    balance_usdt += usdt_amount_out
    balance_eth -= eth_amount_in
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    eth_amount_in = balance_usdt / price_eth
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    balance_eth += eth_amount_in
    balance_usdt = 0
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()
