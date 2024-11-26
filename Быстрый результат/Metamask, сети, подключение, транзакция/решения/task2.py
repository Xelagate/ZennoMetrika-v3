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
    connect_wallet = bot.ads.page.get_by_role('button', name='Connect Wallet').filter(has=bot.ads.page.locator('svg'))
    if connect_wallet.count():
        connect_wallet.click()
        metamask_button = bot.ads.page.get_by_role('button', name='MetaMask')
        bot.metamask.connect(metamask_button)
