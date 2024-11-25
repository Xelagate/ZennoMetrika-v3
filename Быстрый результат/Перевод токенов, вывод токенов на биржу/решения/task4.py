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
    bot.metamask.select_chain(Chains.ARBITRUM_ONE)

    # создаем экземпляр класса Onchain в сети оптимизм и замеряем баланс usdt
    op_chain_instance = Onchain(account=bot.account, chain=Chains.OP)
    balance_usdt_old = op_chain_instance.get_balance(Tokens.USDT_OP)

    # проверяем баланс и считаем его в $
    balance = bot.onchain.get_balance()
    logger.info(f'{bot.account.profile_number} Баланс в сети {balance.ether_float} {balance.symbol}')
    price = get_price_token(bot.chain.native_token)
    balance_usd = balance.ether_float * price

    # если баланс меньше 10$, выводим токены с биржи
    if balance_usd < 10:
        amount = random.randint(10, 20)
        bot.okx.withdraw(token=bot.chain.native_token, amount=amount, chain=bot.chain)
        logger.info(f'{bot.account.profile_number} Баланс {balance.ether_float} {balance.symbol} в сети {bot.chain.name} вывели с биржи')

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
    # выбираем  токен
    token = 'USDT'

    logger.info(f'{bot.account.profile_number} выбрали токен {token}')

    # кликаем по токену
    bot.ads.page.locator('div.dialog:visible').get_by_text(token).click()
    # открываем список сетей
    bot.ads.page.locator('.to-area').locator('.bottomItem').locator('.left').click()
    # выбираем вкладку Ethereum & L2
    bot.ads.page.locator('.selectChainTab:visible').get_by_text('Ethereum & L2').click()
    # получаем локатор сетей
    chains_locator = bot.ads.page.locator('.list-content-box:visible').locator('.contentItemChain')

    # выбираем  сеть
    chain = 'Optimism'

    logger.info(f'{bot.account.profile_number} выбрали сеть {chain}')

    # кликаем по сети
    chains_locator.get_by_text(chain).click()
    # генерируем рандомное количество токенов
    random_amount = random.randint(10, 30)
    logger.info(f'{bot.account.profile_number} отправляем {random_amount} токенов')

    # проверяем баланс токенов, если не хватает выводим с биржи
    balance_usdt = bot.onchain.get_balance(Tokens.USDT_ARBITRUM_ONE)
    if balance_usdt.ether_float < random_amount:
        logger.error(f'{bot.account.profile_number} Недостаточно токенов на балансе')
        bot.okx.withdraw(token='USDT', amount=random_amount*1.1, chain=Chains.ARBITRUM_ONE)

    # ждем поступления токенов на баланс в стартовой сети
    for _ in range(100):
        balance_usdt = bot.onchain.get_balance(Tokens.USDT_ARBITRUM_ONE)
        if balance_usdt.ether_float >= random_amount:
            break
        random_sleep(10, 20)
    else:
        logger.error(f'{bot.account.profile_number} проблема с балансом')
        return

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

    # ждем поступления токенов в сеть OP
    for _ in range(100):
        balance_usdt_new = bot.onchain.get_balance(Tokens.USDT_OP)
        if balance_usdt_new.ether_float > balance_usdt_old.ether_float:
            break
        random_sleep(30, 60)
    else:
        logger.error(f'{bot.account.profile_number} не дождались поступления USDT в сеть OP')
        return

    logger.info(f'{bot.account.profile_number} завершили активность')

