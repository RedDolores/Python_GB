"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


def sort_en(word):
    temp_lst = []
    try:
        for el in word:
            temp_lst.append(ord(el))
        print(bytes(temp_lst))
        temp_lst = []
    except ValueError:
        print(
            'Слово нельзя записать в байтовом типе с помощью маркировки b\'\'')


list_word = ['attribute', 'класс', 'функция', 'type']

for word in list_word:
    sort_en(word)
