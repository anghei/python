class Worker:
    __income = {
        'wage': 150000,
        'bonus': 220000
    }

    def __init__(self, name='John', surname='Smith', position='CEO'):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = Worker.__income
        self.full_name = name + surname
        self.total_income = Worker.__income['wage'] + Worker.__income['bonus']

    # def get_full_name(self):
    #     return self.name + ' ' + self.surname
    #
    # def get_total_income(self):
    #     return self.total_income


class Position(Worker):
    #
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.total_income


a = Position()

print(f'Employee is {a.get_full_name()}')
print(f'Total income of {a.get_full_name()} is ${a.get_total_income()}')
