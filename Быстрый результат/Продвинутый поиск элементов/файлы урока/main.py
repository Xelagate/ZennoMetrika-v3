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

    # поиск по css селектору
    bot.ads.page.locator('button')
    bot.ads.page.locator('#pair')
    bot.ads.page.locator('.icon-up-down')


    bot.ads.page.locator('svg.icon-up-down')
    bot.ads.page.locator('div#pair')

    bot.ads.page.locator('div')

    bot.ads.page.locator('button[data-dd-action-name="Select currency"')
    bot.ads.page.locator('img[src="https://assets.pancakeswap.finance/web/wallets/metamask.png"]')

    bot.ads.page.locator('button')

    # xpath

    # /html/body/div[1]/div[1]/div[3]/div/div/div[1]/div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/label/div/div/button/div/div/div/div

    # //*[@id="pair"]

    bot.ads.page.locator('//button')
    bot.ads.page.locator('//div[@id="pair"]')
    bot.ads.page.locator('//button[@data-dd-action-name="Select currency"]')

    bot.ads.page.locator('//div[text()="Connect"]').highlight()
    bnb_chain_button = bot.ads.page.get_by_text('BNB Chain')
    connect_wallet = bot.ads.page.get_by_text('Connect Wallet')


    bot.ads.page.locator('div:visible', has=bnb_chain_button, has_not=connect_wallet).count()



    pass


if __name__ == '__main__':
    main()
