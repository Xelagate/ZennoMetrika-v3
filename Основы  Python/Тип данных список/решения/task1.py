'''
## Задача 1 - light
### Условие:
Сделайте скрипт, который генерирует список из 10 случайных чисел от 1 до 100.
Используйте цикл и метод append() для добавления чисел в список.

'''

import random

numbers = []
counter = 0
while counter < 10:
    # генерация случайного числа
    random_number = random.randint(1, 100)
    # добавление числа в список
    numbers.append(random_number)
    counter += 1
