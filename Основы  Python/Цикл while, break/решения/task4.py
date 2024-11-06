import random

profile_number = 100

# работаем пока profile_number больше 0
while profile_number > 0:
    print(f'Открыт профиль: {profile_number}')
    # генерируем случайное количество транзакций
    tx_limit = random.randint(5, 10)
    # счетчик транзакций
    tx_counter = 0
    # повторяем пока tx_counter меньше tx_limit
    while tx_counter < tx_limit:
        tx_counter += 1
        print(f'Профиль: {profile_number} - сделана транзакция Swap #{tx_counter}')

    profile_number -= 1
