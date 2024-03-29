# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод init()), который должен принимать данные (список списков) для
# формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22
# 37 43
# 51 86
#
# 3 5 32
# 2 4 6
# -1 64 -8
#
# 3 5 8 3
# 8 3 7 1
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.
#


class Matrix:
    def __init__(self, array):
        temp_list = []
        for el in array:
            temp_list.append([i for i in el])
        self.matrix = temp_list

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


a = [[31, 32], [37, 43], [51, 86]]
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
