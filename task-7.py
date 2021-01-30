import json

with open('task-7.json', 'w+', encoding='utf-8') as json_f:
  with open('task-7.txt', 'r', encoding='utf-8') as firm:
    income = {name.split()[0]: int(name.split()[2]) - int(name.split()[3]) for name in firm}
    # print(income)
    avg_income = {
      "Средняя прибыль": sum([int(x) for x in filter(lambda x: x > 0, income.values())]) / len([int(x) for x in filter(lambda x: x > 0, income.values())])
    }

    final = [income, avg_income]

  json.dump(final, json_f, ensure_ascii=False, indent=4)