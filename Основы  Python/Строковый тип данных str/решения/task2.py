address = "0xac8ce8fbc80115a22a9a69e42f50713aae9ef2f7"
balance_eth = 1.35165161
price_eth = 3000

balance_usd = balance_eth * price_eth  # считаем баланс в USD
short_address = address[:4] + "..." + address[-3:]  # обрезаем адрес кошелька
balance_eth_rounded = round(balance_eth, 2)  # округляем баланс до 2 знаков после запятой
balance_usd_rounded = round(balance_usd, 3)  # округляем баланс в USD до 3 знаков после запятой

balance_eth_str = str(balance_eth_rounded).replace(".", ",")  # заменяем точку на запятую
balance_usd_str = str(balance_usd_rounded).replace(".", ",")  # заменяем точку на запятую

print(f'Адрес кошелька: {short_address}')
print(f'Баланс: {balance_eth_str} ETH')
print(f'Баланс в USD: {balance_usd_str} USD')
