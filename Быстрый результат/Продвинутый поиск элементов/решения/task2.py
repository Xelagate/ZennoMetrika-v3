
import random

def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    words = ['playwright', 'python', 'java', 'c++', 'c#', 'javascript', 'typescript', 'html', 'css', 'php']

    bot.ads.open_url('https://www.wikipedia.org/')
    bot.ads.page.get_by_label('searchInput')
    bot.ads.page.get_by_label('Search Wikipedia').fill(random.choice(words))
    # клик по первому заголовку из результатов поиска
    bot.ads.page.get_by_role('heading', level=3).nth(0).click()
