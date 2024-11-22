import datetime
import random
import time

from eth_account import Account
from loguru import logger

from config import config, Chains, Tokens
from core.bot import Bot
from core.onchain import Onchain
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
    with Bot(account) as bot:
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
    chains = [Chains.ETHEREUM, Chains.BSC, Chains.POLYGON, Chains.AVALANCHE, Chains.ZKSYNC, Chains.ARBITRUM_ONE, Chains.OP]
    # перемешиваем сети
    random.shuffle(chains)

    for chain in chains:
        # находим токены
        usdt = Tokens.get_token_by_symbol('USDT', chain)
        usdc = Tokens.get_token_by_symbol('USDC', chain)

        # создаем объект Onchain с нужной сетью
        onchain = Onchain(bot.account, chain)

        # получаем балансы токенов в нужной сети
        balance_usdt = onchain.get_balance(usdt)
        balance_usdc = onchain.get_balance(usdc)
        logger.info(f"{bot.account.profile_number} Баланс USDT {chain.name}: {balance_usdt}, Баланс USDC {chain.name}: {balance_usdc}")

        total_balance = balance_usdt.ether_float + balance_usdc.ether_float

        # если сумма балансов меньше 100, то делаем вывод
        if total_balance < 100:
            # выбираем токен для вывода, у которого баланс меньше
            withdraw_token = usdt if balance_usdt.ether_float < balance_usdc.ether_float else usdc
            # рандомный мультипликатор для вывода
            random_mult = random.uniform(1.05, 1.1)
            # считаем сумму вывода
            amount = round((100 - total_balance) * random_mult, 2)
            # выводим токен передавая токен, сумму и сеть
            bot.okx.withdraw(withdraw_token, amount, chain)
            # ждем 10-11 минут
            random_sleep(600, 660)

            bot.excel.set_cell(f'{chain.name}-{withdraw_token.symbol}', amount)
            logger.success(f"Вывод {chain.name}-{withdraw_token.symbol} на сумму {amount} успешно выполнен")

















if __name__ == '__main__':
    main()
