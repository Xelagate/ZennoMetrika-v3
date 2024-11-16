import datetime
import time

from eth_account import Account
from loguru import logger

from config import config, Chains
from core.bot import Bot
from core.excel import Excel
from utils.logging import init_logger
from utils.utils import random_sleep, get_accounts, generate_password


def main():
    """ Основная функция """
    # Инициализация консоли и логгера
    init_logger()
    # Получаем список аккаунтов из файлов
    accounts = get_accounts()

    for i in range(config.cycle):
        # Перебираем аккаунты
        for account in accounts:
            # передаем аккаунт в функцию worker
            # здесь можно добавить логику получения данных из Excel и пропуска профиля, если он уже был обработан
            worker(account)

    logger.success("Все аккаунты обработаны")


def worker(account: Account) -> None:
    """
    Функция для работы с аккаунтом, создает бота и передает его в функцию activity
    :param account: аккаунт
    :return: None
    """

    # if not schedule(account):
    #     return

    # Создаем бота
    with Bot(account, Chains.LINEA) as bot:
        # Вызываем функцию activity и передаем в нее бота
        activity(bot)

    random_sleep(*config.pause_between_profile)


def schedule(account: Account) -> bool:
    """
    Функция для работы с аккаунтом, создает бота и передает его в функцию activity
    :param account: аккаунт
    :return: None
    """
    excel = Excel(account)
    date = excel.get_date('Активность 1')
    if date < datetime.datetime.now() - datetime.timedelta(days=5):
        return True
    return False


def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    import random

    # авторизуемся в метамаске
    bot.metamask.auth_metamask()

    # выбираем сеть
    bot.metamask.select_chain(Chains.ETHEREUM)

    # открываем сайт
    bot.ads.open_url('https://www.orbiter.finance')

    logger.info(f'{bot.account.profile_number} Открыли сайт, orbiter.finance')

    # получаем кнопку connect wallet
    connect_wallet = bot.ads.page.locator('.top-nav').get_by_text('Connect wallet')

    # если кнопка есть, то кликаем и подключаем метамаск
    if connect_wallet.count():
        connect_wallet.click()
        bot.metamask.connect(bot.ads.page.get_by_text('MetaMask'))

    logger.info(f'{bot.account.profile_number} Подключили метамаск')

    # открываем список токенов
    bot.ads.page.locator('.ob-select-box').first.click()
    # получаем список всех токенов
    tokens = bot.ads.page.locator('div.dialog:visible').locator('.select-item').all_inner_texts()
    # выбираем рандомный токен
    token = random.choice(tokens)

    logger.info(f'{bot.account.profile_number} выбрали токен {token}')

    # кликаем по токену
    bot.ads.page.locator('div.dialog:visible').get_by_text(token).click()
    # открываем список сетей
    bot.ads.page.locator('.to-area').locator('.bottomItem').locator('.left').click()
    # выбираем вкладку Ethereum & L2
    bot.ads.page.locator('.selectChainTab:visible').get_by_text('Ethereum & L2').click()
    # получаем локатор сетей
    chains_locator = bot.ads.page.locator('.list-content-box:visible').locator('.contentItemChain')
    # получаем список сетей
    chains = chains_locator.all_inner_texts()
    # выбираем рандомную сеть
    chain = random.choice(chains)

    logger.info(f'{bot.account.profile_number} выбрали сеть {chain}')

    # кликаем по сети
    chains_locator.get_by_text(chain).click()
    # генерируем рандомное количество токенов
    random_amount = random.uniform(0.1, 1)

    logger.info(f'{bot.account.profile_number} отправляем {random_amount} токенов')
    # вводим количество токенов
    bot.ads.page.get_by_placeholder('at least').fill(str(random_amount))
    # кликаем на кнопку send
    bot.ads.page.get_by_text('SEND', exact=True).click()
    # ждем загрузки страницы
    bot.ads.page.wait_for_load_state('load')
    # передаем кнопку отправки транзакции в метод отправки транзакции
    bot.metamask.send_tx(bot.ads.page.get_by_text('CONFIRM AND SEND'))

    logger.info(f'{bot.account.profile_number} отправили транзакцию')

    # записываем дату и увеличиваем счетчик транзакций в целевую сеть в Excel
    bot.excel.set_date('date')
    bot.excel.increase_counter(f'bridge_{chain}')

    logger.info(f'{bot.account.profile_number} завершили активность')




if __name__ == '__main__':
    main()
