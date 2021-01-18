# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_input = int(input("Введите месяц в виде числа от 1 до 12: "))

season_dict = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
}

if user_input in [12, 1, 2] and user_input in season_dict.keys():
    print(f'Сейчас {season_dict.get(user_input)}')
elif user_input in [3, 4, 5] and user_input in season_dict.keys():
    print(f'Сейчас {season_dict.get(user_input)}')
elif user_input in [6, 7, 8] and user_input in season_dict.keys():
    print(f'Сейчас {season_dict.get(user_input)}')
elif user_input in [9, 10, 11] and user_input in season_dict.keys():
    print(f'Сейчас {season_dict.get(user_input)}')