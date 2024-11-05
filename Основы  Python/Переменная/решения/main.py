
# 1

profile_number = 1
address = "0xC1a2eA4439753A319997D74084E5A26E5bd449A8"
balance_ETH = 0.5
price_ETH = 3100
balance_USD = balance_ETH * price_ETH
print(f'Запущен профиль: {profile_number}, кошелек: {address}')
print(f'баланс: {balance_ETH} ETH, баланс х: {balance_USD}')

# 2

surname = "Max"
name = "Zarev"
name, surname = surname, name
print(f"My name is {name}, my surname is {surname}")

# 3-1
surname = "Zarev"
name = "Max"
full_name = name + ' ' + surname
print(full_name)

# 3-2
surname = "Zarev"
name = "Max"
full_name = f'{name} {surname}'
print(full_name)

# 4

total = 0
total = total + 10
print(total)
total = total + 10
print(total)
total = total + 10
print(total)
total = total + 10
print(total)

# 5
# номер профиля - profile_number, profile_num, num_profile
# адрес кошелька - address, wallet, wallet_address
# баланс нативного токена - balance_ETH, balance_native_token, native_token_balance
# баланс токена в долларах - balance_USD, token_balance_usd, usd_token_balance
# цена газа - gas_price, price_gas, gas_cost
# баланс токена usdt - balance_USDT, usdt_balance, balance_usdt
# сумма для обмена - amount_to_exchange, exchange_amount, amount_exchange
# первый токен для обмена - token_1, first_token, from_token
# второй токен для обмена - token_2, second_token, to_token
# минимальный баланс Названия переменных должны быть в snake_case, на английском языке и отражать суть хранимых данных.