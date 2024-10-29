
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