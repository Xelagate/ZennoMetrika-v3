def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    bot.onchain.send_token(amount=0.025, to_address='0xAC8ce8fbC80115a22a9a69e42F50713AAe9ef2F7')

