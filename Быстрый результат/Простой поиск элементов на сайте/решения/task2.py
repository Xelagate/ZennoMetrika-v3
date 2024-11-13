
BSC = Chain(
    name='bsc',
    rpc='https://1rpc.io/bnb',
    chain_id=56,
    native_token='BNB'
)

def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    # авторизация в метамаске
    bot.metamask.auth_metamask()
    # выбор сети
    bot.metamask.select_chain(Chains.BSC)
    # переход на сайт
    bot.ads.open_url('https://pancakeswap.finance/', wait_until='load')
    # открываем меню подключения кошелька
    bot.ads.page.get_by_role('button', name='Connect Wallet').nth(0).click()
    # получаем кнопку Metamask
    metamask_button = bot.ads.page.get_by_text('Metamask')
    # подключаем кошелек
    bot.metamask.connect(metamask_button)
    # ждем прогрузки страницы
    bot.ads.page.wait_for_load_state('load')
    random_sleep(5, 10)