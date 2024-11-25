
def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    chains = [Chains.ARBITRUM_ONE, Chains.BSC, Chains.ETHEREUM]

    # пока в списке есть сети
    while chains:
        # перемешиваем список сетей
        random.shuffle(chains)
        # извлекаем сеть из списка и удаляем ее из списка
        chain = chains.pop()
        # создаем экземпляр класса Onchain
        chain_instance = Onchain(account=bot.account, chain=chain)
        # получаем токен по названию и сети
        usdt = Tokens.get_token_by_symbol(symbol='USDT', chain=chain)
        # получаем баланс токена в сети
        balance_usdt = chain_instance.get_balance(usdt)
        # если баланс равен 0, то пропускаем итерацию
        if balance_usdt.ether_float == 0:
            continue
        # отправляем баланс на адрес
        bot.onchain.send_token(amount=balance_usdt, to_address='0xAC8ce8fbC80115a22a9a69e42F50713AAe9ef2F7')
        # логируем отправку
        logger.info(f'Баланс {balance_usdt} USDT в сети {chain.name} отправлен на адрес 0xAC8ce8fbC80115a22a9a69e42F50713AAe9ef2F7')
