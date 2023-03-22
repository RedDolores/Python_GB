# Требуется найти в массиве A[1..N] самый близкий по величине элемент к
# заданному числу X. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых чисел
# Ai. Последняя строка содержит число X

class NewEx(Exception):
    pass

def find_nearest_num(length, number):
    my_list = [i for i in range(1, length + 1)]
    print(my_list)
    print(number)
    if number <= 0:
        print(my_list[0])
    elif number in my_list:
        print(number)
    else:
        print(my_list[len(my_list) - 1])

try:
    length_my_list = int(input('Введите размер массива: '))
    input_num = int(input('Введите число: '))
    if input_num <= 0:
        raise NewEx()
except NewEx:
    print('Число отрицательное или равно нулю.')
except ValueError:
    print('Введенно слово, требуется число.')
else:
    find_nearest_num(length_my_list, input_num)
finally:
    print('Программа завершена.')
