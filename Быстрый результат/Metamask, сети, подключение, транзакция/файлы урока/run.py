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
    bot.metamask.select_chain(Chains.ARBITRUM_ONE)
    bot.ads.open_url('pancakeswap.finance')
    if bot.ads.page.get_by_role('button', name='Connect wallet').count():
        bot.ads.page.get_by_role('button', name='Connect wallet').first.click()
        metamask_button = bot.ads.page.get_by_text('Metamask')
        bot.metamask.connect(metamask_button)

    button_swap = bot.ads.page.locator('#confirm-swap-or-send')
    bot.metamask.send_tx(button_swap)




if __name__ == '__main__':
    main()
