def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """

    balance = bot.onchain.get_balance()
    bot.excel.set_cell('Баланс', balance.ether_float)