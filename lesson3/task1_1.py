class NewEx(Exception):
    pass

seasons = {'Зима': [12 , 1, 2], 'Весна': [3, 4, 5],
            'Лето': [6, 7, 8], 'Осень': [9, 10, 11]
          }

def find_season(number):
    if input_num in seasons['Зима']:
        print('Зима')
    elif input_num in seasons['Весна']:
        print('Весна')
    elif input_num in seasons['Лето']:
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