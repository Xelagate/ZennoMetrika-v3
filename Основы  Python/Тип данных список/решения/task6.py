'''

## Задача 6 - hard
### Условие:
Дан список с 10 токенами.
Выведите в терминале токены, каждый с новой строчки в обратном порядке.
```python
tokens = ['USDT', 'ETH', 'BTC', 'BNB', 'ADA', 'XRP', 'SOL', 'DOT', 'DOGE', 'LTC']
'''

tokens = ['USDT', 'ETH', 'BTC', 'BNB', 'ADA', 'XRP', 'SOL', 'DOT', 'DOGE', 'LTC']
index = 10

while index >= 0:
    index -= 1
    print(tokens[index])
