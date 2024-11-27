def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    # получаем баланс всех профилей
    balances = bot.excel.get_counters('Баланс')
    # получаем баланс текущего профиля
    balance = bot.onchain.get_balance()
    # получаем баланс текущего профиля
    bot.excel.get_counter('Баланс')
    # получаем средний баланс
    average_balance = sum(balances) / len(balances)
    # переменная для хранения суммы перевода
    amount = 0

    # если баланс меньше среднего более чем на 10%
    if balance.ether_float < average_balance * 0.9:
        # считаем сумму перевода
        amount = (average_balance - balance.ether_float) * get_multiplayer()
        # выводим недостающую сумму
        bot.okx.withdraw(token='ETH', amount=amount, chain=bot.chain)
    # если баланс больше среднего более чем на 30%
    elif balance.ether_float > average_balance * 1.3:
        # считаем сумму перевода
        amount = (balance.ether_float - average_balance) * get_multiplayer()
        # получаем адрес субаккаунта  для перевода
        sub_address = bot.excel.get_cell('Sub Address')
        # выводим лишнее с баланса на биржу
        bot.onchain.send_token(amount=amount, to_address=sub_address)

    # если был проведен перевод, обновляем баланс
    if amount:
        balance = bot.onchain.get_balance()

    # записываем баланс в таблицу
    bot.excel.set_cell('Баланс', balance.ether_float)