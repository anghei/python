# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# from timeit import timeit as t
various_types = []

# <------------- Numbers ---------------->
various_types.append(12)

# <------------- Float ---------------->
various_types.append(5.5)

# <------------- Complex ---------------->
various_types.append(complex(1, 3))

# <------------- String ---------------->
various_types.append('fruit')

# <------------- List ---------------->
various_types.append(['apple', 'banana'])

# <------------- Tuple ---------------->
various_types.append(tuple('Earth'))

# <------------- Set ---------------->
various_types.append(set('Winter'))

# <------------- Bool ---------------->
various_types.append(False)

# <------------- Dict ---------------->
various_types.append({'name': 'Timur', 'age': 36})

# <------------- None ---------------->
various_types.append(None)

for item in various_types:
    print(type(item))
    # print(round(t(type(item)), 3))
