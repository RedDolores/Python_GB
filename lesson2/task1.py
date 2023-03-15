# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
# гербом. Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите
# минимальное количество монет, которые нужно перевернуть

from random import randint

count_coins = int(input('Введите количество монеток: '))
sum_zeros, sum_ones = 0, 0
array_coins = [randint(0, 1) for i in range(count_coins)]

for el in array_coins:
    print(el, end=' ')

print()

for el in array_coins:
    if el == 0:
        sum_zeros += 1
    else:
        sum_ones += 1

print(sum_zeros if sum_zeros < sum_ones else sum_ones)