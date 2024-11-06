import random

# конфигурация
password_length = 10
is_numbers = True
is_uppercase = True
is_lowercase = True
is_special = True

# если введено число вне диапазона, то программа должна выбрать случайное число из этого диапазона
if password_length < 4 or password_length > 8:
    password_length = random.randint(4, 8)

print('Выбранная длина пароля:', password_length)

# создаем переменные с наборами символов
numbers = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
special = '!@#$%^&*()_+'

password = ''
# переменная, в которую добавляем все символы, которые пользователь хочет включить в пароль
all_symbols = ''

# добавляем в пароль случайный символ из каждого набора, если пользователь хочет включить его в пароль
if is_numbers:
    password += random.choice(numbers)
    all_symbols += numbers
if is_uppercase:
    password += random.choice(uppercase)
    all_symbols += uppercase
if is_lowercase:
    password += random.choice(lowercase)
    all_symbols += lowercase
if is_special:
    password += random.choice(special)
    all_symbols += special

# мы не проходили циклы, поэтому пока делаем так, добавляем случайный символ,
# пока длина пароля не станет равной password_length
if len(password) < password_length:
    password += random.choice(all_symbols)
    if len(password) < password_length:
        password += random.choice(all_symbols)
        if len(password) < password_length:
            password += random.choice(all_symbols)
            if len(password) < password_length:
                password += random.choice(all_symbols)
                if len(password) < password_length:
                    password += random.choice(all_symbols)
                    if len(password) < password_length:
                        password += random.choice(all_symbols)
                        if len(password) < password_length:
                            password += random.choice(all_symbols)

print(password, len(password))
