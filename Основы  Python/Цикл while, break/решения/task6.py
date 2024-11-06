import random

#  Генерируем случайное число от 1 до 50
secret_number = random.randint(1, 50)
# Количество попыток
tries = 5
print('Угадайте число от 1 до 50. У вас 5 попыток.')
# Пока количество попыток не равно 0
while tries > 0:
    # Ввод числа от пользователя
    user_number = int(input('Введите число: '))
    # Если число пользователя равно секретному числу
    if user_number == secret_number:
        print(f'Поздравляю, вы угадали число! За {5 - tries + 1} попыток.')
        break
    elif user_number < secret_number:
        print('Число должно быть больше.')
    else:
        print('Число должно быть меньше.')
    tries -= 1
# Если цикл завершился без break, то это значит, что попытки закончились
else:
    print(f'Вы проиграли! Было загадано число: {secret_number}')
