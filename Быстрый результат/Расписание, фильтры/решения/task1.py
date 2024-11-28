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
    excel = Excel(file='report.xlsx')

    # перебираем аккаунты
    for account in accounts:
        # подключаем аккаунт к таблице
        excel.connect_account(account)

        # проверяем статус профиля в таблице
        status = excel.get_counter('Status')
        #  if status is not 'Working', skip this account
        if status != 'Working':
            continue

        # add account in list for work
        accounts_for_work.append(account)

    logger.info(f"Выбрано {len(accounts_for_work)} аккаунтов для работы")

    # возвращаем список аккаунтов для работы
    return accounts_for_work