'''

## Задача 3 - medium
### Условие:
Имеется кортеж с токенами:
```python
tokens = ('BTC', 'ETH', 'BNB', 'ADA', 'DOGE', 'XRP', 'DOT', 'UNI', 'LTC', 'LINK')
```
Напишите функцию, которая:
- принимает кортеж с токенами и строку с названием токена
- возвращает кортеж без указанного токена
- если токена нет в кортеже, то возвращает кортеж без изменений

'''

tokens = ('BTC', 'ETH', 'BNB', 'ADA', 'DOGE', 'XRP', 'DOT', 'UNI', 'LTC', 'LINK')


def remove_token(tokens: tuple, token: str) -> tuple:
    """
    Функция удаляет токен из кортежа, если он есть
    :param tokens: кортеж токенов
    :param token: токен, который нужно удалить
    :return: новый кортеж без указанного токена
    """
    if token in tokens:
        tokens = list(tokens)
        tokens.remove(token)
        return tuple(tokens)
    return tokens
