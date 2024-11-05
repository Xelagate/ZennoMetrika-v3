import random

# Генерируем случайную цену газа в диапазоне от 10 до 100
gas_price = random.randint(10, 100)

# Генерируем случайный баланс в диапазоне от 2000 до 10000
balance = random.randint(2000, 10000)

# Рассчитываем стоимость различных операций на основе цены газа
swap_price = gas_price * 40  # Стоимость свапа
bridge_price = gas_price * 75  # Стоимость моста
mint_price = gas_price * 100  # Стоимость минта

# Общая стоимость всех операций
total_price = swap_price + bridge_price + mint_price

# Проверяем, хватает ли баланса для выполнения всех операций
if balance < total_price:
    print('Недостаточно средств для выполнения операций')
    missing_sum = total_price - balance  # Сумма, которой не хватает
    print(f'Сумма вывода: {missing_sum}')
    balance += missing_sum  # Пополняем баланс на недостающую сумму

# Проверяем, подходит ли цена газа для выполнения операций
if gas_price <= 25:
    print('Мост Scroll запущен')
    balance -= bridge_price  # Списываем стоимость моста с баланса
    print(f'Списано {bridge_price} с баланса')
    if gas_price <= 15:
        print('Минт домена запущен')
        balance -= mint_price  # Списываем стоимость минта с баланса
        print(f'Списано {mint_price} с баланса')
elif 50 > gas_price > 25:
    print('Свап запущен')
    balance -= swap_price  # Списываем стоимость свапа с баланса
    print(f'Списано {swap_price} с баланса')
else:
    print('Рекомендуется поработать в другой раз')
