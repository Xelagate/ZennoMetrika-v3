def activity(bot: Bot):
    """
    Функция для работы с ботом, описываем логику активности бота.
    :param bot: бот
    :return: None
    """
    # Переходим на страницу метамаска
    bot.metamask.open_metamask()
    # ставим галочку в чекбокс
    bot.ads.page.get_by_test_id('onboarding-terms-checkbox').click()
    # нажимаем кнопку создать кошелек
    bot.ads.page.get_by_test_id('onboarding-create-wallet').click()
    # нажимаем кнопку "не сейчас"
    bot.ads.page.get_by_test_id('metametrics-no-thanks').click()

    # генерируем пароль и вводим в 2 поля
    if not bot.account.password:
        bot.account.password = generate_password()
    # вводим пароль
    bot.ads.page.get_by_test_id('create-password-new').fill(bot.account.password)
    # подтверждаем пароль
    bot.ads.page.get_by_test_id('create-password-confirm').fill(bot.account.password)
    # ставим галочку в чекбокс
    bot.ads.page.get_by_test_id('create-password-terms').click()
    # нажимаем кнопку "создать кошелек"
    bot.ads.page.get_by_test_id('create-password-wallet').click()
    # нажимаем кнопку защитить кошелек
    bot.ads.page.get_by_test_id('secure-wallet-recommended').click()
    # нажимаем показать фразу восстановления
    bot.ads.page.get_by_test_id('recovery-phrase-reveal').click()

    # создаем пустой список для сид фразы
    seed = []
    # проходим по 12 словам и добавляем их в список
    for i in range(12):
        # генерируем айдишник для слова
        test_id = f"recovery-phrase-chip-{i}"
        # получаем слово и добавляем его в список
        word = bot.ads.page.get_by_test_id(test_id).inner_text()
        seed.append(word)

    # переходим на следующую страницу
    bot.ads.page.get_by_test_id('recovery-phrase-next').click()
    # вводим сид фразу
    for i in range(12):
        # если в поле можно ввести текст
        if bot.ads.page.get_by_test_id(f'recovery-phrase-input-{i}').count():
            # вводим слово
            bot.ads.page.get_by_test_id(f'recovery-phrase-input-{i}').fill(seed[i])
    # нажимаем кнопку "далее"
    bot.ads.page.get_by_test_id('recovery-phrase-confirm').click()
    random_sleep(3, 5)
    # нажимаем кнопку "далее"
    bot.ads.page.get_by_test_id('onboarding-complete-done').click()
    bot.ads.page.get_by_test_id('pin-extension-next').click()
    random_sleep(3, 3)

    seed_str = " ".join(seed)

    # записываем данные в эксель
    bot.excel.set_cell('Password', bot.account.password)
    bot.excel.set_cell('Seed', seed_str)
