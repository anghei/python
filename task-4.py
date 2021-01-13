user_num = int(input("Введите число: "))

maxnum = 0

while user_num > 0:
  a = user_num % 10
  user_num = user_num // 10
  if a > maxnum:
    maxnum = a

print("Самая большая цифра в введенном числе: " + str(maxnum))
