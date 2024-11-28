import datetime
import random
import time

from loguru import logger

from config import config, Chains, Tokens
from core.bot import Bot
from core.onchain import Onchain
from core.excel import Excel
from models.account import Account
from utils.logging import init_logger
from utils.utils import random_sleep, get_accounts, generate_password, get_price_token, shuffle_account, \
    get_multiplayer


def main():
    """ Основная функция """
    # Инициализация консоли и логгера
    init_logger()
    # Получаем список аккаунтов из файлов
    accounts = get_accounts()

    # перебираем профили в цикле
    for i in range(config.cycle):

        # получаем список аккаунтов для работы
        accounts_for_work = schedule_and_filter(accounts)
        # перемешиваем аккаунты если включен режим случайного выбора
        shuffle_account(accounts_for_work)

        # Перебираем аккаунты
        for account in accounts_for_work:
            # передаем аккаунт в функцию worker
            worker(account)
            # Пауза между профилями
            random_sleep(*config.pause_between_profile)

        logger.success(f'Цикл {i + 1} завершен, обработано {len(accounts_for_work)} аккаунтов')
        logger.info(f'Ожидание перед следующим циклом ~{config.pause_between_cycle[1]} секунд')

        # Пауза между циклами
        random_sleep(*config.pause_between_cycle)


def worker(account: Account) -> None:
    """
    Функция Воркера, который создает бота, передает ему аккаунт и вызывает функции активностей передавая туда бота.
    :param account: аккаунт
    :return: None
    """
    # Создаем бота, если в конфиге включен is_browser_run, то будет запущен браузер
    with Bot(account) as bot:
        # Вызываем функцию activity и передаем в нее бота
        activity(bot)
        # сюда по необходимости добавляем другие функции с активностями


def schedule_and_filter(accounts: list[Account]) -> list[Account]:
    """
    Функция для фильтрации аккаунтов по времени и дополнительной логике,
    чтобы пропускать те аккаунты, которые не нужно запускать.
    Перебирает аккаунты через фильтры и возвращает новый список аккаунтов для работы.
    :param accounts: список аккаунтов
    :return: список аккаунтов для работы
    """
    # если фильтрация аккаунтов не включена, возвращаем все аккаунты
    if not config.is_schedule:
        return accounts

    # список аккаунтов для работы
    accounts_for_work = []

    # подключение к таблице со статистикой, без аккаунта
    excel = Excel()

    date_limit = datetime.datetime.now() - datetime.timedelta(minutes=5)

    # перебираем аккаунты
    for account in accounts:

        # подключаем аккаунт к таблице
        excel.connect_account(account)

        # проверяем дату из таблицы
        last_date = excel.get_date('Дата последнего запуска')
        # если дата была после лимита, пропускаем аккаунт
        if last_date > date_limit:
            continue

        # add account in list for work
        accounts_for_work.append(account)


    logger.info(f"Выбрано {len(accounts_for_work)} аккаунтов для работы")

    # возвращаем список аккаунтов для работы
    return accounts_for_work



def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """

    chains = [Chains.BSC, Chains.ETHEREUM, Chains.ARBITRUM_ONE]

    for chain in chains:
        # создаем объект для работы с ончейном
        onchain = Onchain(bot.account, chain)
        # получаем баланс нативной валюты
        new_balance = onchain.get_balance()
        # получаем старый баланс из таблицы
        old_balance = bot.excel.get_counter(f'Balance {chain.name}')
        # если баланс уменьшился в два раза и более, то отправляем уведомление
        if new_balance.ether_float < old_balance / 2:
            message = f'‼️‼️‼️‼️‼ {bot.account} - {bot.account.address}️ Balance {chain.name} is less than half ‼️‼️‼️‼️‼️'
            logger.critical(message)
        # записываем новый баланс в таблицу
        bot.excel.set_cell(f'Balance {chain.name}', new_balance.ether_float)
        # записываем дату последнего запуска
        bot.excel.set_date('Дата последнего запуска')

if __name__ == '__main__':
    main()
