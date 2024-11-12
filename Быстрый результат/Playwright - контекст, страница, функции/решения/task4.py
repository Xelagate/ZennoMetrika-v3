def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    #  открываем страницу метамаск
    bot.metamask.open_metamask()
    # авторизуемся в метамаск
    bot.metamask.auth_metamask()

    # открываем страницу панкейксвап
    bot.ads.open_url('pancakeswap.finance', wait_until='load')

    # кликаем по кнопке Connect Wallet
    bot.ads.page.get_by_role('button', name='Connect Wallet').first.click()
    # находим кнопку Metamask и передаем в метод подключения кошелька
    metamask_button = bot.ads.page.get_by_text('Metamask')
    bot.metamask.connect(metamask_button)
    # ждем пока загрузится страница
    bot.ads.page.wait_for_load_state('load')