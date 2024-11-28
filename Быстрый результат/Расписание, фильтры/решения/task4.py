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

    # название столбцов в таблице
    activities = ['activity 1', 'activity 2', 'activity 3', 'activity 4', 'activity 5']

    minimum = 100
    is_zero = False

    # перебираем аккаунты
    for account in accounts:

        # подключаем аккаунт к таблице
        excel.connect_account(account)

        # получаем список счетчиков активностей
        counters = [excel.get_counter(activity) for activity in activities]

        # если есть хоть один счетчик равный 0
        if min(counters) == 0:
            # если нашли первый 0, обнуляем список аккаунтов для работы
            if not is_zero:
                accounts_for_work = []
            # добавляем аккаунт в список для работы
            accounts_for_work.append(account)
            # включаем флаг, чтобы искать только аккаунты с 0
            is_zero = True

        # пропускаем аккаунты, если есть аккаунты с 0
        if is_zero:
            continue

        # определяем сумму всех счетчиков
        total_counter = sum(counters)

        # если сумма счетчиков равна минимальному, то добавляем аккаунт в список для работы
        if total_counter == minimum:
            # добавляем аккаунт в список для работы и переходим к следующему аккаунту
            accounts_for_work.append(account)
            continue
        # иначе если сумма счетчиков меньше минимальной
        elif total_counter < minimum:
            # обновляем минимальную сумму
            minimum = total_counter
            # обнуляем список аккаунтов для работы и добавляем текущий аккаунт
            accounts_for_work = [account]

    logger.info(f"Выбрано {len(accounts_for_work)} аккаунтов для работы")

    # возвращаем список аккаунтов для работы
    return accounts_for_work

