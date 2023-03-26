# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.

from random import randint

random_num = randint(0, 100)


def guess_number(random_num, count=10):
    try:
        number = int(input('Введите число: '))
    except ValueError:
        print('Число введено некорректно.')
    else:
        if count == 1:
            print(f'Попытки закончились. Загаданное число: {random_num}')
        else:
            if number == random_num:
                print('Угадали!')
            elif number < random_num:
                print('Загаданное число больше.')
                count -= 1
                guess_number(random_num, count)
            else:
                print('Загаданное число меньше.')
                count -= 1
                guess_number(random_num, count)


guess_number(random_num)
