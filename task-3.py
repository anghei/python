with open('task-3.txt', encoding='utf-8') as employees:
    sum_salary = 0
    print('*'*41)
    for index, line in enumerate(employees):
        name = line.split(' ')[0]
        salary = float(line.split(' ')[1])
        sum_salary += salary
        if salary < 20000:
            print(f'Employee {name} have salary below $20000')
        # sum(salary)
    avg_salary = round(sum_salary / (index + 1), 2)
    print('*'*41)
    print(f'Average salary of employees is ${avg_salary}')
    print('*' * 41)