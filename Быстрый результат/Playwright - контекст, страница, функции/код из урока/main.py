def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    bot.ads.open_url('pancakeswap.finance', wait_until='load')  # переходим на страницу по url

    # получаем список вкладок
    bot.ads.context.pages

    # открываем новую вкладку
    bot.ads.context.new_page()

    # перебираем вкладки
    for page in bot.ads.context.pages:
        # активируем вкладки
        page.bring_to_front()
        # печатает название вкладки
        logger.info(f'Активирована страница {page.title()}')

    # обращение к вкладкам по индексу
    bot.ads.context.pages[0].reload()
    bot.ads.context.pages[0].close()

    # проверка закрыта ли вкладка
    bot.ads.page.is_closed()

    # получаем заголовок вкладки
    bot.ads.page.title()

    # получаем url вкладки
    bot.ads.page.url

    # открытие адреса с ожиданием загрузки и 3 попытками
    bot.ads.open_url('pancakeswap.finance/', wait_until='load', attempts=3)

    # встроенный метод для перехода на страницу
    bot.ads.page.goto('https://pancakeswap.finance/', wait_until='load')

    bot.ads.page.go_back()  # метод для возврата на предыдущую страницу
    bot.ads.page.go_forward()  # метод для перехода на следующую страницу
    bot.ads.page.reload()  # метод для перезагрузки страницы

    bot.ads.page.close()  # метод для закрытия страницы

    # запуск контекстного менеджера для ловли вкладки
    with bot.ads.context.expect_page() as page_catcher:
        # клик по элементу вызывающий открытие новой вкладки
        bot.ads.page.get_by_role('link', name='Get Help').click()

    # получение вкладки из контекста
    page_help = page_catcher.value

    bot.metamask.connect(bot.ads.page.get_by_role('button', name='metamask'))  # подключение метамаска
    bot.metamask.send_tx(bot.ads.page.get_by_role('button', name='swap'))  # подтверждение транзакции в метамаске

    # запуск генератора кода
    bot.ads.page.pause()