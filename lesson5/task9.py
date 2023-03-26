# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых
# неотрицательных чисел. Из всех арифметических операций допускаются только
# +1 и -1. Также нельзя использовать циклы.

class NewEx(Exception):
    pass


def sum_numbers(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return sum_numbers(a + 1, b - 1)


try:
    num_a = int(input('Введите число А: '))
    num_b = int(input('Введите число B: '))
    if num_a < 0 or num_b < 0:
        raise NewEx()
except NewEx:
    print('Введенно отрицательное число.')
except ValueError:
    print('Некорректные данные.')
else:
    print(sum_numbers(num_a, num_b))
