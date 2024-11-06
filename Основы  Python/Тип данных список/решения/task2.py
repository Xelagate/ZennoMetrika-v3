'''
`
## Задача 2 - light
### Условие
Сделайте скрипт, который генерирует список из 10 случайных чисел.
Скрипт должен перебрать список (взять по очереди каждый элемент списка) и все четные числа должны быть умножены на 2 и вставлены обратно в список.
Используйте цикл и работу с индексами списка.

'''

import random

numbers = []
counter = 0

# генерация списка
while counter < 10:
    random_number = random.randint(1, 100)
    numbers.append(random_number)
    counter += 1

print(numbers)

index = 0
# перебор списка и умножение четных чисел на 2
while index < 10:
    number = numbers[index]
    if number % 2 == 0:
        numbers[index] = number * 2

    index += 1

print(numbers)
