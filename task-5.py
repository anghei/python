income_rate = int(input("Введите размер выручки компании: "))
expensive_rate = int(input("Введите размер издержек компании: "))
print("=================================")

profit = income_rate - expensive_rate
lesion = expensive_rate - income_rate
if profit > 0:
  print("Прибыль компании составила: " + str(profit))
  print("Рентабельность составила: " + str(round((profit / income_rate)*100)) + "%")
  print("=============================")
  employees = int(input("Введите количество сотрудников в компании: "))
  profit_per_employee = profit / employees
  print("Прибыль компании в расчете на одного сотрудника составила: " + str(round(profit_per_employee, 2)))
else:
  print("Убыток компании составил: -" + str(lesion))

