"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    t_order_dict = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    order_dict = {'orders': [t_order_dict]}

    with open('orders1.json') as j_file:
        j_file_content = j_file.read()
        objs = json.loads(j_file_content)

    if objs == {}:  # проверяем, если файл пустой (т.е. только {})
        with open('orders1.json', 'w') as j_file:
            json.dump(order_dict, j_file, indent=4)
    else:
        for el in objs.values():
            el.append(t_order_dict)
        with open('orders1.json', 'w') as j_file:
            json.dump(objs, j_file, indent=4)


write_order_to_json('scaner', '1', '6000', 'Petrov', '06.06.2001')
write_order_to_json('computer', '2', '50000', 'Sidorov', '25.12.2005')
