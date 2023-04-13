class CheckList:
    def __set_name__(self, owner, attr):
        self.attr = attr

    def __set__(self, instance, value):
        if type(value) is not list:
            raise ValueError(
                'Должен быть список, введен другой тип данных')
        instance.__dict__[self.attr] = value


class Matrix:
    matrix = CheckList()

    def __init__(self, array):
        self.matrix = array

    def __str__(self):
        self.arr = '\n'.join(['\t'.join([str(j) for j in i])
                              for i in self.matrix])
        return self.arr

    def __add__(self, other):
        temp_matrix = self.matrix.copy()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if len(self.matrix) == len(other.matrix) and \
                        len(self.matrix[i]) == len(other.matrix[i]):
                    temp_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                else:
                    return 'Матрицы разной размерности.'
        sum_matrix = Matrix(temp_matrix)
        return sum_matrix


a = [[1, 2], [3, 4], [5, 6]]
b = [[1, 2], [3, 4], [5, 6]]

aa = Matrix(a)
# print(aa.matrix)
print(aa)
print()
bb = Matrix(b)
# print(bb.matrix)
print(bb)
print()
cc = aa + bb
print(cc)