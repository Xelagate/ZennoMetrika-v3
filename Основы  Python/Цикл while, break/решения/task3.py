import random

profile_number = 0

# работаем пока profile_number больше 0
while profile_number < 100:
    print(f'Открыт профиль: {profile_number}')
    # условный оператор с шансом 50%
    if random.randint(0, 1):
        # генерируем случайное число от 10 до 100
        withdraw_amount = random.randint(10, 100)
        # выводим сумму снятия
        print(f'Снятие средств: {withdraw_amount}')

    profile_number += 1
