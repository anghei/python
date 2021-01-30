import random

with open('task-5.txt', 'w+', encoding='utf-8') as numbers:
    x = [random.randint(1, 100) for i in range(1, 17)]
    print(x)
    count = 0
    for number in x:
        # print(number)
        count += number
    print(f'Sum of numbers in a row: {count}')
