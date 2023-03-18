class NewEx(Exception):
    pass


my_list = [7, 5, 4, 2, 2]


def rating(number):
    # если число есть в списке ставим после равных
    if input_num in my_list:
        my_list.insert(my_list.index(input_num) + my_list.count(input_num),
                       input_num)
    elif input_num not in my_list:
        for i in range(len(my_list)):
            # проверяем пары с начала списка
            if input_num > my_list[i - len(my_list)] and \
                    input_num > my_list[i + 1 - len(my_list)]:
                my_list.insert(i, input_num)
                break
            # проверяем пары с конца списка
            elif input_num < my_list[len(my_list) - (len(my_list) + i)] and \
                    input_num < my_list[
                len(my_list) - (len(my_list) + i + 1)]:
                my_list.insert(len(my_list) + i + 1, input_num)
                break
    print(my_list)

try:
    input_num = int(input('Введите число: '))
    if input_num <= 0:
        raise NewEx()
except NewEx:
    print('Число отрицательное или равно нулю.')
except ValueError:
    print('Введенно слово, требуется число.')
else:
    rating(input_num)
finally:
    print('Программа завершена.')
