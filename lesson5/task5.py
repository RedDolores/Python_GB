# Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной
# форме: по десять пар "код-символ" в каждой строке.


def print_ascii(count, temp_count):
    if count == 128:
        return
    else:
        if count < temp_count:
            n = str(chr(count))
            print(f' {count} - {n}', end=' ')
            count += 1
            print_ascii(count, temp_count)
        else:
            print()
            print_ascii(count, temp_count + 10)


print_ascii(32, 42)
