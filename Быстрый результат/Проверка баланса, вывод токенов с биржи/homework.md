## Задача 1 - light
### Условие:
Создайте сети в Chains с полностью заполненными данными, для сетей:
- Ethereum Mainnet
- Binance Smart Chain
- Polygon
- Avalanche
- zkSync
- Arbitrum One
- Optimism

Отправляйте только файл chains.


## Задача 2 - light
### Условие:
Создайте токены в Tokens, с полностью заполненными данными, для токенов:
- USDT для сетей: Ethereum Mainnet, Binance Smart Chain, Polygon, Avalanche, zkSync, Arbitrum One, Optimism
- USDC для сетей: Ethereum Mainnet, Binance Smart Chain, Polygon, Avalanche, zkSync, Arbitrum One, Optimism

Отправляйте только файл tokens.

## Задача 3 - medium
### Условие:
Напишите скрипт, который:
- запускает все профили по очереди
- проверяет баланс токена USDT на сети Arbitrum One
- записывает баланс в Excel в столбец "USDT-Arbitrum One"

Отправляйте файл run.py и settings.py


## Задача 4 - medium
### Условие:
Напишите скрипт, который:
- запускает все профили по очереди
- проверяет баланс нативных токенов в сетях Ethereum Mainnet, Binance Smart Chain, Polygon, Avalanche, zkSync, Arbitrum One, Optimism
- записывает баланс в Excel в столбцы {название сети}-{название токена}

Отправляйте файл run.py и settings.py

## Задача 5 - hard
### Условие:
Напишите скрипт, который:
- запускает все профили рандомно
- проверяет баланс токена USDT и USDC в сетях Ethereum Mainnet, Binance Smart Chain, Polygon, Avalanche, zkSync, Arbitrum One, Optimism
- сети берет в рандомном порядке
- если суммарный баланс  обоих токенов в сети меньше 100$, то выводит тот токен, которого меньше на балансе, чтобы суммарный баланс был больше 100$
- если был сделан вывод, встает на паузу на 10 минут
- записывает сумму вывода в Excel в столбец "Вывод {название сети}-{название токена}"
- выводит сообщение в консоль: "Вывод {название сети}-{название токена} на сумму {сумма} успешно выполнен"
- скрипт должен работать бесконечно, с паузой между профилями 10-20 минут


Отправляйте файл run.py и settings.py