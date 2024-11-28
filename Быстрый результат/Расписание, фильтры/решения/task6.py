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

    # перебираем аккаунты
    for account in accounts:

        # подключаем аккаунт к таблице
        excel.connect_account(account)
        # получаем счетчик транзакций
        counter = excel.get_counter('Transactions')
        # если счетчик транзакций меньше 100, то добавляем аккаунт в список для работы
        if counter <= 30:
            # если меньше 30, то добавляем аккаунт 5 раз
            accounts_for_work.extend([account] * 5)
        elif 30 < counter <= 50:
            # если меньше 50, то добавляем аккаунт 3 раза
            accounts_for_work.extend([account] * 3)
        elif 50 < counter < 100:
            # если меньше 100, то добавляем аккаунт 1 раз
            accounts_for_work.append(account)

    logger.info(f"Выбрано {len(accounts_for_work)} аккаунтов для работы")

    # возвращаем список аккаунтов для работы
    return accounts_for_work