import random
import string

def password_generator(len_password, is_lat_symbol, is_numbers, is_spec_symbol):
    """
    Функция генерирует пароль по заданным параметрам и печатает в терминале.
    :param len_password: длина пароля, минимум 3 символа
    :param is_lat_symbol: использовать ли латинские буквы
    :param is_numbers: использовать ли цифры
    :param is_spec_symbol: использовать ли спец символы
    :return: None
    """

    if not any([is_lat_symbol, is_numbers, is_spec_symbol]):
        print("Необходимо выбрать хотя бы один тип символов")
        return

    if len_password < 3:
        print("Длина пароля должна быть больше 2")
        return


    password = ""  # создаем переменную для пароля
    alphabet = string.ascii_letters  # латинские буквы (включая заглавные)
    number = string.digits  # цифры
    spec_symbol = "!@#$%^&*()_+-="  # спец символы

    active_symbols_list = []

    # Добавляем минимум по одному символу каждого типа если нужно и собираем выбранные символы в список
    if is_lat_symbol:
        password += random.choice(alphabet)
        active_symbols_list.append(alphabet)
    if is_numbers:
        password += random.choice(number)
        active_symbols_list.append(number)
    if is_spec_symbol:
        password += random.choice(spec_symbol)
        active_symbols_list.append(spec_symbol)

    # Добавляем остальные символы
    for _ in range(len_password - len(password)): # пока длина пароля не равна нужной
        random_symbols = random.choice(active_symbols_list) # выбираем случайный список символов
        password += random.choice(random_symbols) # добавляем случайный символ из выбранного списка

    password = ''.join(random.sample(password, len(password))) # перемешиваем пароль
    print(password)  # печатаем пароль
