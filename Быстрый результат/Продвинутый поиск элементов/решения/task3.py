def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    # Открываем страницу
    bot.ads.open_url('https://www.wikipedia.org/')

    # ищем playwright
    bot.ads.page.get_by_label('searchInput')
    bot.ads.page.get_by_label('Search Wikipedia').fill('playwright')
    bot.ads.page.get_by_text('Playwright (software)').click()

    # проставляем радио кнопки
    bot.ads.page.get_by_role('radio', name='Small').click()
    bot.ads.page.get_by_role('radio', name='Wide').click()
    bot.ads.page.get_by_role('radio', name='Dark').click()

    # открываем меню
    bot.ads.page.locator('#vector-page-tools-dropdown').click()
    # открываем ссылку
    bot.ads.page.locator('#t-whatlinkshere').click()
    # открываем список
    bot.ads.page.locator('#mw-htmlform-whatlinkshere-ns').click()
    # выбираем статью
    bot.ads.page.locator('span', has_text='(Article)').click()
    # ставим чекбокс
    bot.ads.page.locator('span#mw-input-hidelinks').click()
    # нажимаем кнопку
    bot.ads.page.get_by_role('button', name='Go').click()