# Для списка реализовать обмен значений соседних элементов/
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_input = input("Введите словосочетание: ")

exchange_list = list(user_input)
index_range = len(exchange_list) - 1
n = 0


while n < index_range:
    exchange_list[n], exchange_list[n+1] = exchange_list[n+1], exchange_list[n]
    n += 2

print(exchange_list)


