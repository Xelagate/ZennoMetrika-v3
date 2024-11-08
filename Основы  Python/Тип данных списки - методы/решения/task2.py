
'''

## Задача 2 - light
### Условие
Создайте список из 10 сгенерированных адресов кошельков.

Возьмите созданный список и напечайте в терминале адреса кошельков в рандомном порядке.

Адреса не должны повторяться. Каждый адрес должен быть напечатан только один раз.

'''

import random

# список символов для генерации адреса
symbols = '0123456789abcdef'
# пустой список для хранения адресов
wallets = []

# пока в списке адресов меньше 10
while len(wallets) < 10:
    # переменная для хранения адреса
    wallet = '0x'
    # посимвольно добавляем к адресу случайные символы из списка,
    # пока длина адреса не станет равной 42
    while len(wallet) < 42:
        # добавляем случайный символ из списка
        wallet += random.choice(symbols)
    # если адреса нет в списке
    if wallet not in wallets:
        # добавляем его в список адресов
        wallets.append(wallet)

print('Список адресов:')
print(wallets, '\n')


# пока в списке адресов есть элементы, [] - False
while len(wallets):
    # генерируем случайный индекс от 0 до длины списка адресов
    length = len(wallets)
    # делаем -1, чтобы не выйти за границу списка
    random_index = random.randint(0, length - 1)
    # удаляем адрес по случайному индексу и печатаем его
    wallet = wallets.pop(random_index)
    print(wallet)
