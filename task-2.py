with open('task-2.txt', encoding='utf-8') as quotes:
    for index, line in enumerate(quotes):

        print(f'Строка {index + 1} содержит слов - {len(line.split())}')