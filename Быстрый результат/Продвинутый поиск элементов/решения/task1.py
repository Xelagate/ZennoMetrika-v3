def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    bot.ads.open_url('https://www.wikipedia.org/')
    bot.ads.page.get_by_label('searchInput')
    bot.ads.page.get_by_label('Search Wikipedia').fill('playwright')
    bot.ads.page.get_by_text('Playwright (software)').click()