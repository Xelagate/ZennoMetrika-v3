# activity = 'withdraw_eth_from_cex'
# balance_eth = 1.35165161
# balance_usdt = 1543
# price_eth = 3000
#
# if activity == 'swap_from_eth_to_usdt':
#     eth_amount_out = 0.5  # Сколько ETH вы хотите обменять
#     usdt_amount_in = eth_amount_out * price_eth  # Сколько USDT вы получите за обмен
#     balance_eth -= eth_amount_out  # Обновляем баланс ETH
#     balance_usdt += usdt_amount_in  # Обновляем баланс USDT
#     print(f'Вы обменяли {eth_amount_out} ETH на {usdt_amount_in} USDT')
#     print(f'Баланс ETH: {balance_eth}')
#     print(f'Баланс USDT: {balance_usdt}')
# elif activity == 'swap_from_usdt_to_eth':
#     usdt_amount_out = 500  # Сколько USDT вы хотите обменять
#     eth_amount_in = usdt_amount_out / price_eth  # Сколько ETH вы получите за об
#     balance_eth += eth_amount_in  # Обновляем баланс ETH
#     balance_usdt -= usdt_amount_out  # Обновляем баланс USDT
#     print(f'Вы обменяли {usdt_amount_out} USDT на {eth_amount_in} ETH')
#     print(f'Баланс ETH: {balance_eth}')
#     print(f'Баланс USDT: {balance_usdt}')
# elif activity == 'withdraw_eth_from_cex':
#     if balance_eth < 0.5:
#         withdraw_eth = 0.5
#     else:
#         withdraw_eth = 0.1
#     balance_eth += withdraw_eth
#     print(f'Вы вывели {withdraw_eth} ETH')
#     print(f'Баланс ETH: {balance_eth}')
# else:  # если условие выше False
#     print('Неизвестная операция')
#
# print('Программа завершена')

var = 5818
if var:
    print('True')
else:
    print('False')
balance = 0


# 0 = False
# любое другое значение = True

# '' = False
# 'text' = True

# [] = False
# [1, 2, 3] = True

# {} = False
# {'key': 'value'} = True

