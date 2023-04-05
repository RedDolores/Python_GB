# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру
# строки и столбца. Аргументы num_rows и num_columns указывают число строк и
# столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов
# идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией
# называется любая операция, у которой ровно два аргумента, как, например, у
# операции умножения.

class Table:

    def print_operation_table(self, operation, num_rows=6, num_columns=6):
        res = [[operation(i, j) for j in range(1, num_columns + 1)]
               for i in range(1, num_rows + 1)]
        arr = '\n'.join(['\t'.join([str(j) for j in i]) for i in res])
        return arr


res = Table()
print(res.print_operation_table(lambda x, y: x * y))
