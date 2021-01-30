with open('task-1.txt', 'w', encoding='utf-8') as f_obj:
    break_point = 'q'
    result_list = []
    while True:
        print('If you wanna quiet press Q')
        user_data = input('Input some data: ')
        if user_data.lower() == 'q':
            # result_list.pop()
            break
        f_obj.write(user_data + '\n')
        # user_data = ''.join(map(str, user_data))
        # result_list.append(user_data)
