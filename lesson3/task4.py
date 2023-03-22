# Требуется вычислить, сколько раз встречается некоторое число X в
# массиве A[1..N]. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих  строках записаны N целых
# чисел Ai. Последняя строка содержит число X

class NewEx(Exception):
    pass

try:
    length_array = int(input('Введите размер массива: '))
    find_num = int(input('Введите искомое число: '))
    if length_array <= 0:
        raise NewEx()
    if find_num <= 0:
        raise NewEx()
except NewEx:
    print('Число отрицательное или равно нулю.')
except ValueError:
    print('Некорректное значение.')
else:
    new_array = [i for i in range(1, length_array)]
    print(new_array.count(find_num) if new_array.count(find_num) == True
          else print(0))

