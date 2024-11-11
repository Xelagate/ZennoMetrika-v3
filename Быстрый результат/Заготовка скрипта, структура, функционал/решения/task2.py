'''Возьмите заготовку скрипта: https://github.com/MaxZarev/The-Template
Доработайте функцию activity, чтобы скрипт:
1. Открывал страницу метамаска.
2. Осуществлял авторизацию в метамаске
3. Ждал от 5 до 10 секунд
4. Писал в терминале при помощи logger "Metamask is opened"

- Для решения задачи используйте только функционал который есть у бота.
- Присылайте в домашнем задании только код функции activity().

'''

def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    bot.metamask.open_metamask()
    bot.metamask.auth_metamask()
    random_sleep(5, 10)
    logger.info("Metamask is opened")
