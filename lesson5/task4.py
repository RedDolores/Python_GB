# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


class NewEx(Exception):
    pass


def sum_numbers(number, a=1, b=-0.5, sum_num=0):
    if number == 0:
        print(sum_num)
    else:
        if number % 2 != 0:
            sum_num += a
            a /= 4
            number -= 1
            sum_numbers(number, a, b, sum_num)
        else:
            sum_num += b
            b /= 4
            number -= 1
            sum_numbers(number, a, b, sum_num)


try:
    number = int(input('Введите число: '))
    if number <= 0:
        raise NewEx()
except NewEx:
    print('Введено число меньше 1.')
except ValueError:
    print('Введено не число.')
else:
    sum_numbers(number)
