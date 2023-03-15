# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

from random import randint
# x, y = 2, 5

x, y = randint(0, 1000), randint(0, 1000)
sum_x_y, product_x_y = x + y, x * y
print(f'Сумма чисел: {sum_x_y}, произведение чисел: {product_x_y}')

num1 = int(input('введите первое число: '))
num2 = int(input('введите второе число: '))
if (num1 + num2 == sum_x_y) and (num1 * num2 == product_x_y):
    print('yes')

while (num1 + num2 != sum_x_y) or (num1 * num2 != product_x_y):
    print('no')
    num1 = int(input('введите первое число: '))
    num2 = int(input('введите второе число: '))
    if (num1 + num2 == sum_x_y) and (num1 * num2 == product_x_y):
        print('yes')
