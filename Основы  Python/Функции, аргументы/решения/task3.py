wallets = []
def generate_wallet_list(wallet_amount):
    """
    Функция генерирует список кошельков в формате "0x" + 40 случайных символов из набора "abcdef0123456789" и сохраняет в глобальную переменную wallets

    :param wallet_amount: количество кошельков которое нужно сгенерировать
    :return: None
    """
    global wallets  # обращаемся к глобальной переменной
    while len(wallets) < wallet_amount:  # пока в списке не будет нужное количество кошельков
        wallet = "0x"  # начало кошелька

        # добавляем случайные символы в кошелек пока он не станет длиной 42 символа
        while len(wallet) < 42:
            wallet += random.choice("abcdef0123456789")  # добавляем случайный символ

        # проверяем что кошелек уникален
        if wallet not in wallets:
            wallets.append(wallet)  # добавляем кошелек в список
