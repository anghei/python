class ZeroDivErr(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    numerator = input('Введите числитель: ')
    denominator = input('Введите знаменатель: ')
    if denominator == "0":
        raise ZeroDivErr('Деление на ноль запрещено!')
    division = int(numerator) / int(denominator)
except (ZeroDivisionError, ZeroDivErr) as Error:
    print(Error)
else:
    print(round(division, 2))