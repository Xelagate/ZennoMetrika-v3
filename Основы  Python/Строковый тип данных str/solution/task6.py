password = 'qwerty123'  # записываем пароль в переменную
user_input = input("Введите пароль: ")  # запрашиваем у пользователя пароль в терминале

is_valid = user_input == password  # сравниваем введенный пользователем пароль с записанным в переменной

print('Пароль корректный?', is_valid)  # выводим результат проверки на экран
