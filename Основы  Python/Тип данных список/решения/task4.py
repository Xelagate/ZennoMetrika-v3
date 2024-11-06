import random

# Конфигурация для генератора паролей
password_count = 10  # Количество паролей, которые необходимо сгенерировать
password_length = 10  # Длина каждого пароля
is_numbers = True  # Включать ли цифры в пароль
is_uppercase = True  # Включать ли заглавные буквы в пароль
is_lowercase = True  # Включать ли строчные буквы в пароль
is_special = True  # Включать ли специальные символы в пароль

# Наборы символов для генерации паролей
numbers = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
special = '!@#$%^&*()_+'

# Список для хранения сгенерированных паролей
passwords = []

# Переменная для хранения всех символов, которые могут быть использованы в пароле
all_symbols = ''

# Добавляем в all_symbols символы в зависимости от настроек
if is_numbers:
    all_symbols += numbers
if is_uppercase:
    all_symbols += uppercase
if is_lowercase:
    all_symbols += lowercase
if is_special:
    all_symbols += special

# Генерация паролей
while password_count > 0:
    password = ''

    # Добавляем хотя бы один символ каждого типа, если они включены в конфигурации
    if is_numbers:
        password += random.choice(numbers)
    if is_uppercase:
        password += random.choice(uppercase)
    if is_lowercase:
        password += random.choice(lowercase)
    if is_special:
        password += random.choice(special)

    # Заполняем оставшуюся часть пароля случайными символами из all_symbols
    while len(password) < password_length:
        password += random.choice(all_symbols)

    # Добавляем сгенерированный пароль в список
    passwords.append(password)
    password_count -= 1

# Выводим список сгенерированных паролей
print(passwords)
