# Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна
# запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь
# вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции.

class NewEx(Exception):
    pass


def operations_a_b():
    op_list = ['0', '+', '-', '*', '/']
    try:
        operator = input('op: ')
        if operator not in op_list:
            raise NewEx()
    except NewEx:
        print('Оператор введен неверно. Введите +, -, *, / '
              'или 0 для выхода')
        operations_a_b()
    else:
        if operator == '0':
            return
        try:
            num_a = int(input('Введите первое число: '))
            num_b = int(input('Введите второе число: '))
            if num_b == 0:
                raise NewEx()
        except ValueError:
            print('Введено не число. Введите +, -, *, / или 0 для выхода')
            operations_a_b()
        except NewEx:
            print('Деление на ноль невозможно. Введите +, -, *, / '
                  'или 0 для выхода')
            operations_a_b()
        else:
            if operator == '+':
                print(num_a + num_b)
            elif operator == '-':
                print(num_a - num_b)
            elif operator == '*':
                print(num_a * num_b)
            elif operator == '/':
                print(num_a / num_b)
            operations_a_b()


operations_a_b()
