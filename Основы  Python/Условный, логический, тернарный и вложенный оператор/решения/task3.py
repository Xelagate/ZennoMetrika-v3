import random

# Генерация случайного числа от 0 до 4
activity_index = random.randint(0, 4)

# ветвление на основе числа в переменной activity_index
if activity_index == 0:
    print('swap')
elif activity_index == 1:
    print('bridge')
elif activity_index == 2:
    print('mint')
elif activity_index == 3:
    print('farm')
else:
    print('stake')