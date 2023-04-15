"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def encode_word(lst):
    temp_lst = []
    for word in lst:
        temp_lst.append(word.encode('utf-8'))
    return temp_lst


def decode_word(lst):
    temp_lst = []
    for word in lst:
        temp_lst.append(word.decode('utf-8'))
    return temp_lst


list_word = ['разработка', 'администрирование', 'protocol', 'standard']
a = encode_word(list_word)
print(*a, sep='\n')
print()
b = decode_word(a)
print(*b, sep='\n')
