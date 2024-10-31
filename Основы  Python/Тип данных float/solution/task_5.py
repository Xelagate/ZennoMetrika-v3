import random

balance_eth = random.uniform(0.02, 0.03)
price_eth = random.uniform(2300, 2700)
balance_usd = balance_eth * price_eth  # считаем баланс в долларах
min_balance_eth = 100 / price_eth * 1.01  # считаем минимальное количество эфира равное 100 долларам (+1% запас)

print(f'Баланс кошелька: {balance_eth} ETH')
print(f'Стоимость 1 ETH: {price_eth} $')
print(f'Баланс в долларах: {balance_usd} $')

insufficient_amount = min_balance_eth - balance_eth  # считаем недостающую сумму
print(f'Недостающая сумма: {insufficient_amount} ETH')

withdrawal_amount = round(insufficient_amount, 4)  # считаем сумму для вывода

print(f'Сумма для вывода: {withdrawal_amount} ETH')
balance = balance_eth + withdrawal_amount  # считаем баланс после вывода
balance_usd = balance * price_eth  # считаем баланс в долларах после вывода
print(f'Баланс после вывода: {balance} ETH')
print(f'Баланс в долларах после вывода: {balance_usd} $')
