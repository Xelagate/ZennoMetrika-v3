num_input = int(input('Введите число: '))
if num_input < 0:
    print('Трейдер')
elif num_input == 0:
    print('Начинающий')
elif 1 <= num_input <= 100:  # одновременно проверяет два условия
    print('Нормис')
elif 101 <= num_input <= 1000:  # одновременно проверяет два условия
    print('Деген')
elif 1001 <= num_input <= 10000:  # одновременно проверяет два условия
    print('Кит')
else:
    print('Илон Маск')
