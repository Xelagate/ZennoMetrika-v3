import random

# конфигурация
is_numbers = True
is_uppercase = True
is_lowercase = True
is_special = True

# создаем переменные с наборами символов
numbers = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
special = '!@#$%^&*()_+'

password = ''

# добавляем в пароль случайный символ из каждого набора, если пользователь хочет включить его в пароль
if is_numbers:
    password += random.choice(numbers)
if is_uppercase:
    password += random.choice(uppercase)
if is_lowercase:
    password += random.choice(lowercase)
if is_special:
    password += random.choice(special)

print(password)

