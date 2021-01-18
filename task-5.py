# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

raiting_list = [8, 6, 5, 2, 2]
user_input = int(input("Введите рейтинг: "))
user_list = [user_input]


range_of_raiting = range(raiting_list[-1], raiting_list[0])
# index_by_user_input = raiting_list.index(user_input)

if user_input in raiting_list:
    # print('In List')
    index_by_user_input = raiting_list.index(user_input)
    print(index_by_user_input)
    raiting_list.insert(index_by_user_input, user_input)
    print("Ваш текущий рейтинг: " + str(raiting_list))
    # if index_by_user_input == 0:
    #     index_by_user_input += 1
    #     raiting_list.insert(index_by_user_input, user_input)
    #     print(raiting_list)
else:
    # print('Not in list')
    raiting_list = raiting_list + user_list
    print("Ваш текущий рейтинг: " + str(sorted(raiting_list, reverse=True)))
