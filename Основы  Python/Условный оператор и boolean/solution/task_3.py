# Начальный баланс в ETH и USDT
balance_eth = 1.35165161
balance_usdt = 505
# Текущая цена ETH в USDT
price_eth = 3000

# Проверяем, если баланс USDT равен 0
if balance_usdt == 0:
    # Рассчитываем комиссию в 5% от текущего баланса ETH
    commission = balance_eth * 0.05  
    # Рассчитываем количество ETH для обмена, вычитая комиссию
    eth_amount_in = balance_eth - commission  
    # Рассчитываем количество USDT, получаемое от обмена ETH
    usdt_amount_out = eth_amount_in * price_eth 
    # Выводим информацию об обмене
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    # Обновляем баланс USDT после обмена
    balance_usdt += usdt_amount_out
    # Обновляем баланс ETH после обмена
    balance_eth -= eth_amount_in
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    # Рассчитываем количество ETH, которое можно купить на текущий баланс USDT
    eth_amount_in = balance_usdt / price_eth
    # Выводим информацию об обмене
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    # Обновляем баланс ETH после обмена
    balance_eth += eth_amount_in
    # Устанавливаем баланс USDT в 0 после обмена
    balance_usdt = 0
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()  # Пустая строка для разделения выводов

# Повторяем тот же процесс обмена для демонстрации
if balance_usdt == 0:
    # Рассчитываем комиссию в 5% от текущего баланса ETH
    commission = balance_eth * 0.05
    # Рассчитываем количество ETH для обмена, вычитая комиссию
    eth_amount_in = balance_eth - commission
    # Рассчитываем количество USDT, получаемое от обмена ETH
    usdt_amount_out = eth_amount_in * price_eth
    # Выводим информацию об обмене
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    # Обновляем баланс USDT после обмена
    balance_usdt += usdt_amount_out
    # Обновляем баланс ETH после обмена
    balance_eth -= eth_amount_in
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    # Рассчитываем количество ETH, которое можно купить на текущий баланс USDT
    eth_amount_in = balance_usdt / price_eth
    # Выводим информацию об обмене
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    # Обновляем баланс ETH после обмена
    balance_eth += eth_amount_in
    # Устанавливаем баланс USDT в 0 после обмена
    balance_usdt = 0
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()  # Пустая строка для разделения выводов

if balance_usdt == 0:
    # Рассчитываем комиссию в 5% от текущего баланса ETH
    commission = balance_eth * 0.05
    # Рассчитываем количество ETH для обмена, вычитая комиссию
    eth_amount_in = balance_eth - commission
    # Рассчитываем количество USDT, получаемое от обмена ETH
    usdt_amount_out = eth_amount_in * price_eth
    # Выводим информацию об обмене
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    # Обновляем баланс USDT после обмена
    balance_usdt += usdt_amount_out
    # Обновляем баланс ETH после обмена
    balance_eth -= eth_amount_in
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    # Рассчитываем количество ETH, которое можно купить на текущий баланс USDT
    eth_amount_in = balance_usdt / price_eth
    # Выводим информацию об обмене
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    # Обновляем баланс ETH после обмена
    balance_eth += eth_amount_in
    # Устанавливаем баланс USDT в 0 после обмена
    balance_usdt = 0
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()  # Пустая строка для разделения выводов

if balance_usdt == 0:
    # Рассчитываем комиссию в 5% от текущего баланса ETH
    commission = balance_eth * 0.05
    # Рассчитываем количество ETH для обмена, вычитая комиссию
    eth_amount_in = balance_eth - commission
    # Рассчитываем количество USDT, получаемое от обмена ETH
    usdt_amount_out = eth_amount_in * price_eth
    # Выводим информацию об обмене
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    # Обновляем баланс USDT после обмена
    balance_usdt += usdt_amount_out
    # Обновляем баланс ETH после обмена
    balance_eth -= eth_amount_in
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    # Рассчитываем количество ETH, которое можно купить на текущий баланс USDT
    eth_amount_in = balance_usdt / price_eth
    # Выводим информацию об обмене
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    # Обновляем баланс ETH после обмена
    balance_eth += eth_amount_in
    # Устанавливаем баланс USDT в 0 после обмена
    balance_usdt = 0
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()  # Пустая строка для разделения выводов

if balance_usdt == 0:
    # Рассчитываем комиссию в 5% от текущего баланса ETH
    commission = balance_eth * 0.05
    # Рассчитываем количество ETH для обмена, вычитая комиссию
    eth_amount_in = balance_eth - commission
    # Рассчитываем количество USDT, получаемое от обмена ETH
    usdt_amount_out = eth_amount_in * price_eth
    # Выводим информацию об обмене
    print(f'Обмен {balance_eth} ETH на {usdt_amount_out} USDT')
    # Обновляем баланс USDT после обмена
    balance_usdt += usdt_amount_out
    # Обновляем баланс ETH после обмена
    balance_eth -= eth_amount_in
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')
else:
    # Рассчитываем количество ETH, которое можно купить на текущий баланс USDT
    eth_amount_in = balance_usdt / price_eth
    # Выводим информацию об обмене
    print(f'Обмен {balance_usdt} USDT на {eth_amount_in} ETH')
    # Обновляем баланс ETH после обмена
    balance_eth += eth_amount_in
    # Устанавливаем баланс USDT в 0 после обмена
    balance_usdt = 0
    # Выводим обновленные балансы
    print(f'Баланс ETH: {balance_eth} ETH после обмена')
    print(f'Баланс USDT: {balance_usdt} USDT после обмена')

print()  # Пустая строка для разделения выводов
