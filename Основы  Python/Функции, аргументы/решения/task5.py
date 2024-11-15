
wallets = []
generate_wallet_list(10)  # генерируем список кошельков
for wallet in wallets:
    print(f"Кошелек: {wallet}")  # печатаем название кошелька
    password_generator(10, True, True, True)  # генерируем пароль
    wait_work_gas(30)  # ждем когда газ будет меньше 30
    withdraw_from_exchange(wallet, 1000)  # проверяем баланс и делаем вывод если надо