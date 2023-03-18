class NewEx(Exception):
    pass

analitics_dict = {'названия': [], 'цены': [],
                  'количества': [], 'ед.': []}
list_name, list_price, list_count, list_unit = [], [], [], []

try:
    count_position = int(input('Введите количестов позиций: '))
    if count_position <= 0:
        raise NewEx()
except NewEx:
    print('Число отрицательное или равно нулю.')
except ValueError:
    print('Введенно слово, требуется число.')
else:
    list_goods = [None for i in range(count_position)]

for i in range(count_position):
    try:
        name_product = input('Введите название: ')
        price_product = int(input('Введите цену: '))
        count_product = int(input('Введите количество: '))
        unit_product = input('Введите единицы измерения: ')
    except ValueError:
        print('Введенно слово, требуется число.')
    else:
        list_name.append(name_product)
        list_price.append(price_product)
        list_count.append(count_product)
        list_unit.append(unit_product)
        list_goods[i] = tuple([i + 1, {'название': name_product,
                                       'цена': price_product,
                                       'количество': count_product,
                                       'ед.': unit_product}])
        analitics_dict.update({'названия': list(set(list_name))})
        analitics_dict.update({'цены': list(set(list_price))})
        analitics_dict.update({'количества': list(set(list_count))})
        analitics_dict.update({'ед.': list(set(list_unit))})

for tuples in list_goods:
    print(tuples)
print()
for k, v in analitics_dict.items():
    print(k, v)



