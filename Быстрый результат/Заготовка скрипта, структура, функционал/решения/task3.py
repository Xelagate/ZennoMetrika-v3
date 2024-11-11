'''Возьмите заготовку скрипта: https://github.com/MaxZarev/The-Template
Доработайте функцию activity, чтобы скрипт:
1. Открывал страницу https://www.google.com/
2. Писал в терминале "Google is opened"
3. Записывал в excel таблицу в столбец google дату и время открытия страницы, в строке с номером открытого аккаунта.
4. Ждал рандомную паузу от 5 до 10 секунд
5. Переходил на страницу https://www.youtube.com/
6. Писал в терминале "Youtube is opened"
7. Записывал в excel таблицу в столбец youtube дату и время открытия страницы, в строке с номером открытого аккаунта.
8. Ждал рандомную паузу от 5 до 10 секунд
9. Завершал работу над аккаунтом

- Для решения задачи используйте только функционал который есть у бота.
- Присылайте в домашнем задании только код функции activity().

'''

def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    bot.ads.open_url('https://www.google.com/')
    logger.info("Google is opened")
    bot.excel.set_date('google')
    random_sleep(5, 10)
    bot.ads.open_url('https://www.youtube.com/')
    logger.info("Youtube is opened")
    bot.excel.set_date('youtube')
    random_sleep(5, 10)
