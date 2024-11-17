import random

# генерируем случайный газ от 15 до 25 (включительно)
gas_price = random.randint(15, 25)

# генерируем случайный баланс от 0 до 2 (включительно)
balance = random.randint(0, 2)

# генерируем случайное количество транзакций в кошельке от 0 до 3 (включительно)
tx_counter = random.randint(0, 3)

print(f'Стартовые параметры:\n'
      f'Баланс: {balance}, Количество транзакций: {tx_counter}\n')

bridge_price = 2  # цена за Bridge
swap_price = 1  # цена за Swap

if not balance:
    print('Баланс нулевой')
    withdrawal = random.randint(1, 2)
    print(f"делаем вывод с биржи: {withdrawal}")
    balance += withdrawal

# 1 транзакция

# определяем активность
activity = 'Bridge' if gas_price <= 20 else 'Swap'
# определяем цену активности
activity_price = bridge_price if activity == 'Bridge' else swap_price

# если баланса не хватает на активность, делаем вывод с биржи
if balance < activity_price:
    print('Баланса не хватает')
    withdrawal = random.randint(1, 2)
    print(f"делаем вывод с биржи: {withdrawal}")
    balance += withdrawal

tx_counter += 1  # увеличиваем счетчик транзакций
balance -= activity_price  # вычитаем цену активности из баланса
print(f'Мы сделали {activity}, баланс: {balance}', f'Количество транзакций: {tx_counter}\n')

# 2 транзакция
if tx_counter < 5:

    gas_price = random.randint(15, 25)

    # определяем активность
    activity = 'Bridge' if gas_price <= 20 else 'Swap'

    # определяем цену активности
    activity_price = bridge_price if activity == 'Bridge' else swap_price

    # если баланса не хватает на активность, делаем вывод с биржи
    if balance < activity_price:
        print('Баланса не хватает')
        withdrawal = random.randint(2, 3)
        print(f"делаем вывод с биржи: {withdrawal}")
        balance += withdrawal

    tx_counter += 1
    balance -= activity_price
    print(f'Мы сделали {activity}, баланс: {balance}', f'Количество транзакций: {tx_counter}\n')

    # 3 транзакция
    if tx_counter < 5:
        gas_price = random.randint(15, 25)

        # определяем активность
        activity = 'Bridge' if gas_price <= 20 else 'Swap'

        # определяем цену активности
        activity_price = bridge_price if activity == 'Bridge' else swap_price

        # если баланса не хватает на активность, делаем вывод с биржи
        if balance < activity_price:
            print('Баланса не хватает')
            withdrawal = random.randint(2, 3)
            print(f"делаем вывод с биржи: {withdrawal}")
            balance += withdrawal

        tx_counter += 1
        balance -= activity_price
        print(f'Мы сделали {activity}, баланс: {balance}', f'Количество транзакций: {tx_counter}\n')

        # 4 транзакция
        if tx_counter < 5:
            gas_price = random.randint(15, 25)

            # определяем активность
            activity = 'Bridge' if gas_price <= 20 else 'Swap'

            # определяем цену активности
            activity_price = bridge_price if activity == 'Bridge' else swap_price

            # если баланса не хватает на активность, делаем вывод с биржи
            if balance < activity_price:
                print('Баланса не хватает')
                withdrawal = random.randint(2, 3)
                print(f"делаем вывод с биржи: {withdrawal}")
                balance += withdrawal

            tx_counter += 1
            balance -= activity_price
            print(f'Мы сделали {activity}, баланс: {balance}', f'Количество транзакций: {tx_counter} \n')

            # 5 транзакция
            if tx_counter < 5:
                gas_price = random.randint(15, 25)

                # определяем активность
                activity = 'Bridge' if gas_price <= 20 else 'Swap'

                # определяем цену активности
                activity_price = bridge_price if activity == 'Bridge' else swap_price

                # если баланса не хватает на активность, делаем вывод с биржи
                if balance < activity_price:
                    print('Баланса не хватает')
                    withdrawal = random.randint(2, 3)
                    print(f"делаем вывод с биржи: {withdrawal}")
                    balance += withdrawal

                tx_counter += 1
                balance -= activity_price
                print(f'Мы сделали {activity}, баланс: {balance}', f'Количество транзакций: {tx_counter}')
