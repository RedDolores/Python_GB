# Напишите программу, которая на вход принимает два числа A и B, и
# возводит число А в целую степень B с помощью рекурсии.


def degree_positive(a, b):
    if b == 0:
        return 1
    return a * degree_positive(a, b - 1)


def degree_negative(a, b):
    if b == 0:
        return 1
    return 1 / a * degree_negative(a, b + 1)


try:
    num_a = int(input('Введите число А: '))
    num_b = int(input('Введите степень B: '))
except ValueError:
    print('Некорректные данные.')
else:
    if num_b >= 0:
        print(degree_positive(num_a, num_b))
    else:
        print(degree_negative(num_a, num_b))
