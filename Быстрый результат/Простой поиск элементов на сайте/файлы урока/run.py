def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    bot.ads.open_url('pancakeswap.finance', wait_until='load')  # переходим на страницу по url

    button = bot.ads.page.get_by_role()  # ищем элемент по роли
    bot.ads.page.get_by_test_id()  # ищем элемент по тегу test_id
    bot.ads.page.get_by_text()  # ищем элемент по тексту
    bot.ads.page.get_by_label()  # ищем элемент по лейблу
    bot.ads.page.get_by_placeholder()  # ищем элемент по placeholder
    bot.ads.page.get_by_title()  # ищем элемент по title
    bot.ads.page.get_by_alt_text()  # ищем элемент по alt тексту

    button.click()