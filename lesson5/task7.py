# Напишите программу, доказывающую или проверяющую, что для множества
# натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.

class NewEx(Exception):
    pass


def sum_num(number):
    if number == 1:
        return 1
    else:
        return number + sum_num(number - 1)


try:
    number = int(input('Введите натуральное число: '))
    if number < 1:
        raise NewEx()
except NewEx:
    print('Число введено некорректно.')
except ValueError:
    print('Введено не число.')
else:
    sum_number = sum_num(number)
    if sum_number == number * (number + 1) / 2:
        print(f'для n = {number}')
        list_num = [i for i in range(1, number + 1)]
        print(*list_num, sep='+', end=' ')
        print(f'= {number}*({number}+1)/2')
