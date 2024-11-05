password = input("Enter your password: ")  # запрашиваем у пользователя пароль в терминале
password_length = len(password)  # вычисляем длину пароля
is_valid = password_length >= 8  # проверяем, что длина пароля больше или равна 8
print(is_valid)  # выводим результат проверки на экран
