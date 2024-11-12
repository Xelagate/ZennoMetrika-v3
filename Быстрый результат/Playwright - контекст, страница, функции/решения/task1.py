def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    # переходим на страницу по url
    bot.ads.open_url('pancakeswap.finance', wait_until='load')

    # кликаем по ссылке и ловим новую страницу
    with bot.ads.context.expect_page() as page_catcher:
        # кликаем по ссылке
        bot.ads.page.get_by_role('link', name='Contributing').click()
    new_page = page_catcher.value
    # ждем загрузки страницы
    new_page.wait_for_load_state('load')
    # закрываем страницу
    bot.ads.context.pages[0].close()
    # логируем название новой страницы
    logger.info(new_page.title())
