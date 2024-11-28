from functions import withdraw_binance, withdraw_bybit, withdraw_okx


def main():
    withdraw_binance()
    withdraw_okx()
    withdraw_bybit()

if __name__ == '__main__':
    main()

"""
Файл __init__.py в пакете позволяет объединить несколько модулей в один пакет.
В данном случае, в файле __init__.py импортируются функции из модулей balance, onchain и withdraw.
Таким образом, в файле main.py можно импортировать функции из пакета functions, а не из каждого модуля по отдельности.
"""