"""
Функция для работы с ботом, описываем логику активности бота.
:param bot: бот
:return: None
"""
bot.metamask.auth_metamask()
bot.metamask.select_chain(Chains.ARBITRUM_ONE)
bot.ads.open_url('https://app.uniswap.org/')
if bot.ads.page.get_by_test_id('navbar-connect-wallet').count():
    bot.ads.page.get_by_test_id('navbar-connect-wallet').first.click()
    metamask_button = bot.ads.page.get_by_role('button', name='MetaMask')
    bot.metamask.connect(metamask_button)
