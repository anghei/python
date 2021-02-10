# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».

# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

## TODO: доработать функцию для распознавания даты введенной на русском языке
class Data():
    """
    Функция преобразования даты вида "день-месяц-год"
    """

    def __init__(self, v):
        self.v = v

    # def convert(self):
    #   converted_date = self.v.split('-')
    #   day = converted_date[0]
    #   month = converted_date[1]
    #   year = converted_date[2]
    #   return f'Сегодня {day}.{month}.{year} года'

    @classmethod
    def convert(cls, v):
        converted_date = v.split('-')
        # print(converted_date)
        day = converted_date[0]
        month = converted_date[1]
        year = converted_date[2]
        return f'Указана дата: {int(day):02d}.{int(month):02d}.{int(year)} г.'

    @staticmethod
    def check(self):
        converted_date = self.split('-')
        day = converted_date[0]
        month = converted_date[1]
        year = converted_date[2]
        if int(month) in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] and int(year) in range(2000, 2050):
            return f'Дата введена корректно!'
        else:
            return f'Неверный формат даты\nМесяц должен быть указан в диапазоне от 1 до 12\nГод - от 2000 до 2050'


print(Data.check('06-13-2021'))
print(Data.convert('06-02-2021'))