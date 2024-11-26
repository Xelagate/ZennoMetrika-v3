def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    bot.metamask.auth_metamask()
    bot.metamask.select_chain(Chains.ARBITRUM_ONE)
    bot.ads.open_url('https://stargate.finance/bridge')
    random_sleep(5, 7)

    # перебираем страницы и закрываем всплывающее окно метамаска
    for page in bot.ads.context.pages:
        if 'notification' in page.url:
            page.close()
            break

    connect_wallet = bot.ads.page.get_by_role('button', name='Connect Wallet').filter(
        has=bot.ads.page.locator('svg'))
    if connect_wallet.count():
        connect_wallet.click()
        metamask_button = bot.ads.page.get_by_role('button', name='MetaMask')
        bot.metamask.connect(metamask_button)

    # выбираем первый токен
    bot.ads.page.get_by_role('button', name='Token').first.click()
    bot.ads.page.get_by_placeholder('Search by name or token symbol').first.fill('ETH')
    bot.ads.page.locator('div', has_text='Select token').get_by_role('button', name='ETH Arbitrum').click()

    # выбираем сеть назначения
    bot.ads.page.get_by_role('button', name='To').filter(has_not_text='Token').first.click()
    # выбираем сеть оптимизм
    bot.ads.page.get_by_role('button', name='Optimism').first.click()
    # выбираем второй токен
    bot.ads.page.get_by_role('button', name='Token').nth(1).click()
    # вводим название второго токена
    bot.ads.page.get_by_placeholder('Search by name or token symbol').nth(1).fill('ETH')
    # выбираем токен ETH Optimism
    bot.ads.page.locator('div', has_text='Select token').get_by_role('button', name='ETH Optimism').click()

    # вводим сумму
    amount = random.uniform(0.0001, 0.001)
    bot.ads.page.get_by_placeholder('0').fill(str(round(amount, 5)))

    # нажимаем кнопку transfer и отправляем транзакцию
    transfer_button = bot.ads.page.get_by_role('button', name='Transfer').click()
    bot.metamask.send_tx(transfer_button)