import random

counter = 0

# работаем пока счетчик меньше 100
while counter < 100:
    # генерируем случайное число от 1 до 1000
    profile_number = random.randint(1, 1000)
    print(f'Открыт профиль: {profile_number}')

    counter += 1  # увеличиваем счетчик на 1
