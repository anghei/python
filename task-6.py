import re

dict_subject = {}
with open('task-6.txt', encoding='utf-8') as schedule:
    for line in schedule.readlines():
        dict_subject[re.findall(r'^\w+', line)[0]] = sum(map(int, (re.findall(r'\d+', line))))
    print(dict_subject)