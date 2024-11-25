def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    sub_address = bot.excel.get_cell('суб аккаунт')
    chains = [Chains.ARBITRUM_ONE, Chains.BSC, Chains.ETHEREUM]

    # пока в списке есть сети
    while chains:
        # перемешиваем список сетей
        random.shuffle(chains)
        # извлекаем сеть из списка и удаляем ее из списка
        chain = chains.pop()
        # создаем экземпляр класса Onchain
        chain_instance = Onchain(account=bot.account, chain=chain)
        # получаем баланс токена в сети
        balance = chain_instance.get_balance()
        # получаем цену нативного токена сети
        native_token = chain.native_token
        price = get_price_token(native_token)

        # считаем баланс в $
        balance_usd = balance.ether_float * price

        # если баланс меньше 10$,
        if balance_usd < 10:
            # генерируем рандомное количество токенов
            amount = random.randint(10, 30)
            # выводим токен с биржи
            bot.okx.withdraw(token=native_token, amount=amount, chain=chain)
            logger.info(f'Баланс {balance.ether_float} {native_token} в сети {chain.name} вывели с биржи')
        elif balance_usd > 100:
            # вычисляем сумму вывода на биржу, с рандомным коэффициентом
            amount = (balance_usd - 100) * random.uniform(1.1, 1.2)
            # отправляем баланс на суб аккаунт биржи
            bot.onchain.send_token(amount=amount, to_address=sub_address)
            logger.info(f'Баланс {balance.ether_float} {native_token} в сети {chain.name} отправлен на адрес {sub_address}')

        random_address = bot.onchain.w3.eth.account.create().address
        # отправляем баланс на рандомный адрес
        amount = 0.01 / price
        bot.onchain.send_token(amount=amount, to_address=random_address)
        logger.info(f'Баланс {amount} {native_token} в сети {chain.name} отправлен на рандомный адрес {random_address}')

