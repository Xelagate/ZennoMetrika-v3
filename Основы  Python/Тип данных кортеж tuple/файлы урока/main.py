# tuple - кортеж, неизменяемый список

# Создание кортежа
tuple
numbers = (1, 2, 3, 4, 5)
print(f'numbers: {numbers}, type: {type(numbers)}')
numbers2 = 1, 2, 3, 4, 5
print(f'numbers2: {numbers2}, type: {type(numbers2)}')

empty_tuple = ()
empty_tuple2 = tuple()
print(f'empty_tuple: {empty_tuple}, type: {type(empty_tuple)}')
print(f'empty_tuple2: {empty_tuple2}, type: {type(empty_tuple2)}')

convert_list = tuple([1, 2, 3, 4, 5])
print(f'convert_list: {convert_list}, type: {type(convert_list)}')
convert_string = tuple('hello')
print(f'convert_string: {convert_string}, type: {type(convert_string)}')

# создание кортежа с одним элементом
one_element_tuple = (1,)
one_element_tuple2 = 1,
print(f'one_element_tuple: {one_element_tuple}, type: {type(one_element_tuple)}')
print(f'one_element_tuple2: {one_element_tuple2}, type: {type(one_element_tuple2)}')

# Извлечение элементов кортежа
print(f'numbers[0]: {numbers[0]}')
print(f'numbers[-1]: {numbers[-1]}')
# извлечение среза
print(f'numbers[1:3]: {numbers[1:3]}')
print(f'numbers[:3]: {numbers[:3]}')

# изменение кортежа, нельзя изменить элемент кортежа
# numbers[0] = 10
# print(f'numbers: {numbers}')

my_list = [1, 2, 3, 4, 5]

def process_list(init_list: list) -> list:
    res_list = init_list.copy()
    res_list.append(6)
    return res_list


my_list2 = process_list(my_list)
print(f'my_list: {my_list}')
print(f'my_list2: {my_list2}')


tokens = ('ETH', 'BTC')

def process_list(init_tuple: tuple) -> tuple:
    res_list = list(init_tuple)
    res_list.append('SOL')
    return tuple(res_list)


tokens_2 = process_list(tokens)
print(f'my_list: {tokens}')
print(f'my_list2: {tokens_2}')


def get_stat() -> tuple[int, int, int]:
    print('get_stat')
    return 1, 2, 3

stat = get_stat()
print(f'stat: {stat}, type: {type(stat)}')
one_stat, two_stat, three_stat = stat
print(f'one_stat: {one_stat}, two_stat: {two_stat}, three_stat: {three_stat}')

# распаковка кортежа
one, two, three = (1, 2, 3)
print(f'one: {one}, two: {two}, three: {three}')

name, surname, age = 'John', 'Doe', 30
name, surname, age = age, name, surname

# конкатенация кортежей и умножение кортежа на число
numbers = (1, 2, 3)
numbers2 = (4, 5, 6)
numbers3 = numbers + numbers2
print(f'numbers3: {numbers3}')

numbers4 = numbers * 3
print(f'numbers4: {numbers4}')

# методы кортежей
numbers = (1, 2, 3, 4, 5)
print(f'numbers: {numbers}')
print(f'numbers.count(2): {numbers.count(2)}')

print(f'numbers.index(3): {numbers.index(3)}')
print(f'numbers.index(3, 2): {numbers.index(3, 2)}')
print(f'numbers.index(3, 2, 4): {numbers.index(3, 2, 4)}')

# проверка наличия элемента в кортеже
print(f'2 in numbers: {2 in numbers}')

print(len(numbers))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# сортировка кортежа
numbers = (3, 1, 5, 2, 4)
numbers = tuple(sorted(numbers))
print(f'numbers: {numbers}')

# преобразование кортежа в строку
numbers = 1, 2, 3, 4, 5
numbers_str = str(numbers)
print(f'numbers_str: {numbers_str}, type: {type(numbers_str)}')

numbers_str = ' '.join(map(str, numbers))
print(f'numbers_str: {numbers_str}, type: {type(numbers_str)}')

# преобразование строки в кортеж
numbers_str = '1 2 3 4 5'
numbers = tuple(numbers_str.split())
print(f'numbers: {numbers}, type: {type(numbers)}')

# изменение кортежа через преобразование
numbers = (1, 2, 3, 4, 5)
numbers = list(numbers)
numbers.pop(2)
numbers = tuple(numbers)
print(f'numbers: {numbers}')

# переменные и кортежи
a = 1
b = 2
c = 3
numbers = a, b, c
a = 5
print(f'numbers: {numbers}')

# кортежи и функции
def get_data():
    return 1, 2, 3







