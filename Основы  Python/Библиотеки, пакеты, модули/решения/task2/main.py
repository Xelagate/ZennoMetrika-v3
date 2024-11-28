from functions.withdraw import withdraw_binance as binance
from functions.withdraw import withdraw_bybit as bybit
from functions.withdraw import withdraw_okx as okx

def main():
    binance()
    okx()
    bybit()

if __name__ == '__main__':
    main()