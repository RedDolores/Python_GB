"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import os
import csv


def filter_array(array, first_index):
    t_arr = [array[i].split(': ') for i in range(first_index, len(array), 4)]
    tt_arr = [el[j] for el in t_arr for j in range(1, len(el))]
    return tt_arr


def fill_array(*args):
    temp_arr = [el for el in args]
    n_arr = [['' for i in range(len(temp_arr) + 1)] for j in
             range(len(temp_arr[0]))]
    for i in range(len(temp_arr)):
        for j in range(len(temp_arr[i])):
            n_arr[j][0] = j + 1
            n_arr[j][i + 1] = temp_arr[i][j]
    return n_arr


def get_data(directory):
    list_name = ['Изготовитель системы', 'Название ОС', 'Код продукта',
                 'Тип системы']
    temp_list, main_data = [], []
    main_data.append(list_name)
    for entry in os.scandir(directory):
        if entry.is_file() and entry.name.endswith('.txt'):
            with open(entry.path, 'r') as t_file:
                for line in t_file:
                    content = ' '.join(line.split())
                    for el in list_name:
                        if content.startswith(el):
                            temp_list.append(content)

    os_name_list = filter_array(temp_list, 0)
    os_code_list = filter_array(temp_list, 1)
    os_prod_list = filter_array(temp_list, 2)
    os_type_list = filter_array(temp_list, 3)
    main_data.extend(
        fill_array(os_prod_list, os_name_list, os_code_list, os_type_list))
    return main_data


def write_to_csv(path):
    data = get_data(directory)
    with open(path, 'w', encoding='utf-8') as c_file:
        c_file_writer = csv.writer(c_file)
        for row in data:
            c_file_writer.writerow(row)
    with open(path, encoding='utf-8') as c_file:
        print(c_file.read())


directory = 'D:/GB/Python/lessons/venv/Python_GB/lesson8/task1'
write_to_csv('data_report1.csv')

""" Внизу уже было """
# os_prod_reg = re.compile(r'Изготовитель системы:\s*\S*')
# os_prod_list.append(os_prod_reg.findall(data)[0].split()[2])
