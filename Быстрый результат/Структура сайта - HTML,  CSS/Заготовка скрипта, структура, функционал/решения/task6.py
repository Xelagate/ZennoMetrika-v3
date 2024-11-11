'''

## Задача 5 - medium
### Условие:
Возьмите заготовку скрипта и напишите скрипт, который:
- будет открывать https://github.com/MaxZarev/ZennoMetrika-v3
- после чего будет кликать по ссылке “Основы Python".
- отправляйте только реализацию функции activity()
'''

def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    logger.info('Начинаем активность')

    bot.ads.open_url('https://github.com/MaxZarev/ZennoMetrika-v3')
    bot.ads.page.get_by_role("link", name='Основы Python').click()