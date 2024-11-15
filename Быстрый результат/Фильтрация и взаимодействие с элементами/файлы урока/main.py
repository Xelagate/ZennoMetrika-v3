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
    bot.ads.open_url('pancakeswap.finance')
    button = bot.ads.page.locator('nav')
    button.locator('something')

    button.and_(bot.ads.page.locator('nav'))
    button.or_(bot.ads.page.locator('nav'))

    button.filter()

    bnb_chain_button = bot.ads.page.get_by_text('BNB Chain')
    connect_wallet = bot.ads.page.get_by_text('Connect Wallet')

    bot.ads.page.locator('div:visible').filter(has=bnb_chain_button, has_not=connect_wallet).count()

    bot.ads.page.get_by_role('link').filter(has_text='seme text').get_by_role('button').click()

    links = bot.ads.page.get_by_role('link').all()

    for link in links[:10]:
        link.hover()

    bot.ads.page.locator('button').wait_for('visible')

    bot.ads.page.locator('#swap-button').is_disabled()

    bot.ads.page.locator('#swap-button').first.click(force=True)
    bot.ads.page.locator('#swap-button').first.dblclick()
    bot.ads.page.locator('#swap-button').first.fill()
    bot.ads.page.locator('#swap-button').first.clear()
    bot.ads.page.locator('#swap-button').first.press('a')
    bot.ads.page.locator('#swap-button').first.press_sequentially()
    bot.ads.page.locator('#swap-button').first.check()


if __name__ == '__main__':
    main()
