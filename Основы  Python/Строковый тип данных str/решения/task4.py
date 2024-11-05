user_input = input("Введите адрес кошелька, пароль и количество повторений пароля через пробел: ")
address, password, repeat_count = user_input.split()
repeat_count = int(repeat_count)
password = password * repeat_count

print(f'Адрес кошелька: {address}')
print(f'Пароль: {password}')