# Сформировать из введенного числа обратное по порядку входящих в него
# цифр и вывести на экран
class NewEx(Exception):
    pass


def revers_num(number, temp_n=''):
    if number == 0:
        print(temp_n)
    else:
        temp_n += str(number % 10)
        number //= 10
        return revers_num(number, temp_n)


try:
    number = int(input('Введите число: '))
    if number <= 9:
        raise NewEx()
except NewEx:
    print('Число отрицательное или введена цифра.')
except ValueError:
    print('Введено не число.')
else:
    revers_num(number)
