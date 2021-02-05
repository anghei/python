class Cell:
    """
    Супер-пупер метод молекулярной генетики и инженерии
    """
    def __init__(self, quantity):
        self.q = quantity

    def make_order(self, rows):
        return '\n'.join(['@ ' * rows for _ in range(self.q // rows)]) + '\n' + '@ ' * (self.q % rows)

    def __str__(self):
        return f"{self.q}"

    def __add__(self, other):
        if isinstance(other, Cell):
            return f'Сумма клеток - {self.q + other.q}'
        raise NotImplemented

    def __sub__(self, other):
        if isinstance(other, Cell):
            return f'Вычитание клеточной биомассы составило - {Cell(self.q - other.q)}' \
                if self.q - other.q > 0 \
                else f"Клеточной биомассы в первой клетке меньше чем во второй, вычитание невозможно!"

    def __mul__(self, other):
        if isinstance(other, Cell):
            return f'Процедура переумножения клеток вернуло результат - {Cell(self.q * other.q)}'

    def __floordiv__(self, other):
        if isinstance(other, Cell):
            return f'Процедура целочисленного деления клеток вернуло результат - {Cell(self.q // other.q)}'


a = Cell(5)
b = Cell(7)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(b.make_order(7))
