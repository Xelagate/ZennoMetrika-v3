def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    # переходим на страницу метамаска
    bot.ads.open_url(config.metamask_url)
    # ищем поле ввода пароля и вводим пароль
    bot.ads.page.get_by_test_id('unlock-password').fill(bot.account.password)
    # нажимаем на кнопку разблокировки
    bot.ads.page.get_by_test_id('unlock-submit').click()