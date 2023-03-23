# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются
# в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого
# множества. m - кол-во элементов второго множества. Затем пользователь вводит
# сами элементы множеств.

size_n = int(input('n '))
size_m = int(input('m '))

arr_n = set([int(input(f'n el [{i}] ')) for i in range(size_n)])
arr_m = set([int(input(f'm el [{i}] ')) for i in range(size_m)])
arr_nm = set()

print(arr_n)
print(arr_m)

arr_nm = arr_n.intersection(arr_m)

print(arr_nm)