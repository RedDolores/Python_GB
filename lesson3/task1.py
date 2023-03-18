class NewEx(Exception):
    pass

winter = [12 , 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

def find_season(number):
    if input_num in winter:
        print('Зима')
    elif input_num in spring:
        print('Весна')
    elif input_num in summer:
        print('Лето')
    else:
        print('Осень')

try:
    input_num = int(input('Введите номер месяца: '))
    if input_num <= 0 or input_num > 12:
        raise NewEx()
except NewEx:
    print('Месяца с таким номером не существует.')
except ValueError:
    print('Введенно слово, требуется число.')
else:
    find_season(input_num)
finally:
    print('Программа завершена.')

