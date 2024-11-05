import random  # необходимо, чтобы робот из своих справочников достал нужную функцию

balance = random.randint(100, 500)
count_transactions = random.randint(1, 10)
volume = random.randint(1000, 2000)
average_volume_transaction = volume / count_transactions

min_balance = 200
min_volume = 1500
min_count_transactions = 5
min_average_volume_transaction = min_volume / min_count_transactions

is_eligible_balance = balance >= min_balance  # проверка на баланс
is_eligible_volume = volume >= min_volume  # проверка на объем
is_eligible_count_transactions = count_transactions >= min_count_transactions  # проверка на количество транзакций
is_eligible_average_volume_transaction = volume / count_transactions >= min_average_volume_transaction  # проверка на среднюю сумму транзакции
is_eligible = is_eligible_balance and is_eligible_volume and is_eligible_count_transactions and is_eligible_average_volume_transaction  # проверка на все условия

print(f"Минимальные критерии дропа:")
print(f"Баланс: {min_balance}")
print(f"Объем: {min_volume}")
print(f"Количество транзакций: {min_count_transactions}")
print(f"Средняя сумма транзакции: {min_average_volume_transaction}")
print()
print(f"Показатели кошелька:")
print(f"Баланс: {balance} Eligible? {is_eligible_balance}")
print(f"Количество транзакций: {count_transactions} Eligible? {is_eligible_count_transactions}")
print(f"Объем транзакций: {volume} Eligible? {is_eligible_volume}")
print(f"Средняя сумма транзакции: {average_volume_transaction} Eligible? {is_eligible_average_volume_transaction}")
print(f"Кошелек Eligible для дропа? {is_eligible}")
