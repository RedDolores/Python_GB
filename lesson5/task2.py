# Подсчитать четные и нечетные цифры введенного натурального числа.

class NewEx(Exception):
    pass


def find_even_odd(number, even_count=0, odd_count=0):
    if number == 0:
        print(f'Количество четных: {even_count}, '
              f'количество нечетных: {odd_count}')
    else:
        temp_num = number % 10
        number //= 10
        if temp_num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
        return find_even_odd(number, even_count, odd_count)


try:
    number = int(input('Введите число: '))
    if number < 0:
        raise NewEx()
except NewEx:
    print('Введенное число отрицательное.')
except ValueError:
    print('Число введено некорректно.')
else:
    find_even_odd(number)
