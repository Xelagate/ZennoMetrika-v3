import random

# Генерируем случайное значение баланса в эфирах (ETH) в диапазоне от 0.02 до 0.03
balance_eth = random.uniform(0.02, 0.03)

# Генерируем случайную стоимость одного эфира (ETH) в долларах в диапазоне от 2300 до 2700
price_eth = random.uniform(2300, 2700)

# Вычисляем баланс в долларах, умножая баланс в ETH на текущую стоимость ETH
balance_usd = balance_eth * price_eth

# Вычисляем минимальное количество эфира, эквивалентное 100 долларам (+1% запас)
min_balance_eth = 100 / price_eth * 1.01

# Выводим текущий баланс в ETH
print(f'Баланс кошелька: {balance_eth} ETH')

# Выводим текущую стоимость одного ETH в долларах
print(f'Стоимость 1 ETH: {price_eth} $')

# Выводим текущий баланс в долларах
print(f'Баланс в долларах: {balance_usd} $')

# Вычисляем недостающую сумму в ETH, чтобы достичь минимального баланса
insufficient_amount = min_balance_eth - balance_eth

# Выводим недостающую сумму в ETH
print(f'Недостающая сумма: {insufficient_amount} ETH')

# Округляем недостающую сумму до 4 знаков после запятой для вывода
withdrawal_amount = round(insufficient_amount, 4)

# Выводим сумму для вывода
print(f'Сумма для вывода: {withdrawal_amount} ETH')

# Вычисляем новый баланс в ETH после вывода
balance = balance_eth + withdrawal_amount

# Вычисляем новый баланс в долларах после вывода
balance_usd = balance * price_eth

# Выводим новый баланс в ETH после вывода
print(f'Баланс после вывода: {balance} ETH')

# Выводим новый баланс в долларах после вывода
print(f'Баланс в долларах после вывода: {balance_usd} $')
