from functions.withdraw import withdraw_binance, withdraw_bybit, withdraw_okx


def main():
    withdraw_binance()
    withdraw_okx()
    withdraw_bybit()

if __name__ == '__main__':
    main()