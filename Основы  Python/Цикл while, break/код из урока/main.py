# import random
#
# password_length = 20
# alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
#
# password = ''
#
# if len(password) < password_length:
#     password += random.choice(alphabet_lower)
#     if len(password) < password_length:
#         password += random.choice(alphabet_upper)
#         if len(password) < password_length:
#             password += random.choice(digits)
#             if len(password) < password_length:
#                 password += random.choice(alphabet_lower)
#                 if len(password) < password_length:
#                     password += random.choice(alphabet_upper)
#                     if len(password) < password_length:
#                         password += random.choice(digits)
#                         if len(password) < password_length:
#                             password += random.choice(alphabet_lower)
#                             if len(password) < password_length:
#                                 password += random.choice(alphabet_upper)
#                                 if len(password) < password_length:
#                                     password += random.choice(digits)
#                                     if len(password) < password_length:
#                                         password += random.choice(alphabet_lower)
#                                         if len(password) < password_length:
#                                             password += random.choice(alphabet_upper)
#                                             if len(password) < password_length:
#                                                 password += random.choice(digits)
#                                                 if len(password) < password_length:
#                                                     password += random.choice(alphabet_lower)
#                                                     if len(password) < password_length:
#                                                         password += random.choice(alphabet_upper)
#                                                         if len(password) < password_length:
#                                                             password += random.choice(digits)
#                                                             if len(password) < password_length:
#                                                                 password += random.choice(alphabet_lower)
#                                                                 if len(password) < password_length:
#                                                                     password += random.choice(alphabet_upper)
#                                                                     if len(password) < password_length:
#                                                                         password += random.choice(digits)
#                                                                         if len(password) < password_length:
#                                                                             password += random.choice(alphabet_lower)
#                                                                             if len(password) < password_length:
#                                                                                 password += random.choice(alphabet_upper)
#                                                                                 if len(password) < password_length:
#                                                                                     password += random.choice(digits)
#                                                                                     if len(password) < password_length:
#                                                                                         password += random.choice(alphabet_lower)
#                                                                                         if len(password) < password_length:
#                                                                                             password += random.choice(alphabet_upper)
#                                                                                             if len(password) < password_length:
#                                                                                                 password += random.choice(digits)
#
# print(password)


import random
#
# alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# digits = '0123456789'
# print("Программа генерации пароля запущена")
# # while - пока условие верно, выполняется код внутри цикла
# password = ''
#
# password_length = 15
# flag = True
#
# while len(password) < password_length:
#     if random.randint(0, 1):
#         password += random.choice(alphabet_lower)
#         if len(password) == password_length:
#             continue
#
#     if random.randint(0, 1):
#         password += random.choice(alphabet_upper)
#         if len(password) == password_length:
#             continue
#
#     if random.randint(0, 1):
#         password += random.choice(digits)
#         if len(password) == password_length:
#             continue
#
# print(password, len(password))

# import random
# import time
#
# GAS_LIMIT = 12
# gas_price = random.randint(10, 100)
#
# while gas_price > GAS_LIMIT:
#     print(f'Цена газа {gas_price} высокая, ожидаем 1 сек...')
#     time.sleep(1)
#     if random.randint(0, 1):
#         break
#     gas_price = random.randint(10, 100)
# else:
#     print('Цена газа низкая, запускаем транзакцию')
#
#
# print('Send TX')
# print('еще какая-то логика')


# profile = 0
#
# while profile < 100:
#     profile += 1
#     print('Запустили профиль', profile)
    # tx_count = random.randint(0, 10)
    # if tx_count >= 10:
    #     print('Профиль', profile, 'уже сделал 10 транзакций')
    #     continue
    #
    # print('Swap')
    # print('Bridge')
    # print('Mint')


profile = 0

while profile < 100:
    profile += 1
    balance = random.randint(0, 1000)
    print('Запустили профиль', profile)

    if balance < 100:
        balance += 500

    tx_counter = 0
    while tx_counter < 10:
        tx_counter += 1
        print('Swap')
        print('Профиль', profile, 'сделал', tx_counter, 'транзакций')
