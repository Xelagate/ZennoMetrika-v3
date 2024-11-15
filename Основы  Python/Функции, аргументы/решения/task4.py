
def withdraw_from_exchange(wallet, min_balance):
    """
    Функция вывода с биржи, на вход должна получать адрес кошелька и минимальный баланс, внутри должен проходить псевдо запрос баланса (генерируем рандомно),
    :param wallet: адрес кошелька
    :param min_balance: минимальный баланс
    :return: None
    """
    balance = random.randint(0, 2000)  # генерируем случайный баланс
    print(f"Баланс кошелька {wallet}: {balance}")  # печатаем баланс
    if balance < min_balance:  # проверяем что баланс ниже минимальной суммы
        amount = random.randint(100, 1000)  # генерируем случайную сумму
        print(f"Вывод на кошелек {wallet} суммой {amount}")  # печатаем сообщение о выводе

