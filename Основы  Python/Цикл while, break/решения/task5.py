import random

counter = 0  # счетчик
total_withdraw = 0  # общая сумма вывода
withdraw_counter = 0  # счетчик выводов

while counter < 100:  # пока счетчик меньше 100
    counter += 1  # увеличиваем счетчик на 1
    profile_number = random.randint(100, 500)  # генерируем случайное число от 100 до 500
    balance = random.randint(0, 1000)  # генерируем случайное число от 0 до 1000
    print(f"Профиль: {profile_number}, баланс: {balance}")  # выводим на экран профиль и баланс

    if profile_number % 2 == 0:  # если профиль делится на 2 без остатка
        print(f'Профиль {profile_number} пропускаем', end='\n\n')  # выводим на экран, что профиль пропускаем
        continue  # переходим к следующей итерации цикла

    if balance < 500:  # если баланс меньше 500
        amount_to_withdraw = random.randint(100, 500)  # генерируем случайное число от 100 до 500
        print(f'Профиль {profile_number} вывод: {amount_to_withdraw}',
              end='\n\n')  # выводим на экран, что профиль выводит
        total_withdraw += amount_to_withdraw  # увеличиваем общую сумму вывода на сумму вывода
        withdraw_counter += 1  # увеличиваем счетчик выводов на 1

print(f'Сделано выводов: {withdraw_counter}')  # выводим на экран количество выводов
print(f'Выведено: {total_withdraw}')  # выводим на экран общую сумму вывода
