from random import randint, randrange


class Matrix:
    """
    Функция для сложения матриц
    """

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return f'Матрица равна\n' + str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))

    def __add__(self, other):
        return Matrix(list(map(
            lambda x, y: list(map(lambda z, w: z + w, x, y)), self.matrix, other.matrix)))


a1 = [
    [randrange(1, 3) for num in range(3)],
    [randrange(1, 3) for num in range(3)]
]
a2 = [
    [randrange(1, 3) for num in range(3)],
    [randrange(1, 3) for num in range(3)]
]

matrix1 = Matrix(a1)
matrix2 = Matrix(a2)

matrix3 = matrix1 + matrix2
print(matrix3)

# a = Matrix([[1, 2, 3], [4, 5, 6]])
# b = Matrix([[1, 2, 3], [4, 5, 6]])
# c = a + b
#
# print(c)
