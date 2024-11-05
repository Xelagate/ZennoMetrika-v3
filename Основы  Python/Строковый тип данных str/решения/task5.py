import random  # Импортируем модуль random для генерации случайных чисел

# Создаем строки с символами, которые будут использоваться для генерации пароля
alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Строка с буквами алфавита в нижнем регистре
alphabet_upper = alphabet.upper()  # Строка с буквами алфавита в верхнем регистре
numbers = '0123456789'  # Строка с цифрами
symbols = '!@#$%^&*'  # Строка с символами

# Вычисляем длины строк для дальнейшего использования в генерации случайных индексов
alphabet_length = len(alphabet)  # Длина алфавита в нижнем регистре
numbers_length = len(numbers)  # Длина строки с цифрами
symbols_length = len(symbols)  # Длина строки с символами

# Генерируем случайные индексы для выбора символов из каждой строки
low_char_index = random.randint(0, alphabet_length - 1)  # Случайный индекс для буквы в нижнем регистре
upper_char_index = random.randint(0, alphabet_length - 1)  # Случайный индекс для буквы в верхнем регистре
number_index = random.randint(0, numbers_length - 1)  # Случайный индекс для цифры
symbol_index = random.randint(0, symbols_length - 1)  # Случайный индекс для символа

# Формируем пароль, соединяя выбранные символы
password = (
    alphabet[low_char_index] +
    alphabet_upper[upper_char_index] +
    numbers[number_index] +
    symbols[symbol_index]
)

# Выводим сгенерированный пароль
print(password)
