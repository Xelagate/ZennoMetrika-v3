'''

## Задача 5 - Hard
### Условие:
Напишите функцию, которая принимает 2 списка и возвращает кортеж, в котором:
- каждый элемент - это кортеж из двух элементов:
  - первый элемент из первого списка и второй элемент из второго списка
- если списки разной длинны, то в кортеж должен быть ограничен длинной списка с меньшим количеством элементов

пример:
```python
wallets = ['wallet1', 'wallet2', 'wallet3', 'wallet4']
passwords = ['password1', 'password2', 'password3']

# result = (('wallet1', 'password1'), ('wallet2', 'password2'), ('wallet3', 'password3'))
'''

wallets = ['wallet1', 'wallet2', 'wallet3', 'wallet4']
passwords = ['password1', 'password2', 'password3']

def connect_data(wallets: list, passwords: list) -> tuple:
    """
    Функция соединяет два списка в кортеж, где каждый элемент - это кортеж из двух элементов из списков
    :param wallets: список кошельков
    :param passwords: список паролей
    :return: кортеж из кортежей
    """
    return tuple(zip(wallets, passwords))
