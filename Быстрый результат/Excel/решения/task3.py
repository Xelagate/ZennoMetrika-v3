from utils.utils import get_multiplayer, get_price_tokenutils.py


def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """

    # получаем цену токена
    eth_price = get_price_token('ETH')

    # получаем баланс всех профилей
    balances = bot.excel.get_counters('Баланс')
    # получаем баланс текущего профиля
    balance = bot.onchain.get_balance()

    # получаем средний баланс
    average_balance = sum(balances) / len(balances)

    # генерируем балансы по рангам
    rank_balances = {
        'Мейн': [average_balance * 1.5, 1000],
        'Мидл': [average_balance * 0.9, average_balance * 1.1],
        'Бомж': [10, average_balance * 0.5]
    }

    # получаем ранг текущего профиля
    rank = bot.excel.get_cell('Ранг')

    # переменная для хранения суммы перевода
    amount = 0

    # считаем баланс в usd
    usd_balance = balance.ether_float * eth_price

    # если баланс меньше минимального по рангу
    if usd_balance < rank_balances[rank][0]:
        # считаем сумму вывода с биржи
        amount = (rank_balances[rank][0] - usd_balance) / eth_price * get_multiplayer()
        # выводим с биржи
        bot.okx.withdraw(token='ETH', amount=amount, chain=bot.chain)
    # если баланс больше максимального по рангу
    elif usd_balance > rank_balances[rank][1]:
        # считаем сумму перевода на суб адрес
        amount = (usd_balance - rank_balances[rank][1]) / eth_price * get_multiplayer()
        # получаем суб адрес
        sub_address = bot.excel.get_cell('Sub Address')
        # переводим на суб адрес
        bot.onchain.send_token(amount=amount, to_address=sub_address)

    # если был проведен перевод, обновляем баланс
    if amount:
        balance = bot.onchain.get_balance()

    # записываем баланс в таблицу
    bot.excel.set_cell('Баланс', balance.ether_float)


9
