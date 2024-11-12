def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    bot.ads.open_url('pancakeswap.finance', wait_until='load')  # переходим на страницу по url

    links = ['Tokenomics',
             'CAKE Emission Projection',
             'Blog',
             'Careers',
             'Terms Of Service']

    # перебираем ссылки и кликаем по ним
    for link in links:
        bot.ads.page.get_by_role('link', name=link).click()

    # перебираем страницы
    for page in bot.ads.context.pages:
        # активируем страницу
        page.bring_to_front()
        logger.info(f'Активирована страница {page.title()}')

    # закрыть все вкладки кроме последней
    pages_to_close = bot.ads.context.pages[:-1]
    for page in pages_to_close:
        logger.info(f'Закрыта страница {page.title()}')
        page.close()