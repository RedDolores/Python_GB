# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем
# слова. Будем считать, что на вход подается только одно слово, которое
# содержит либо только английские, либо только русские буквы.

class NewEx(Exception):
    pass

eng_abc = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
           2: ['D', 'G'], 3: ['B', 'C', 'M', 'P'],
           4: ['F', 'H', 'V', 'W', 'Y'], 5: ['K'], 8: ['J', 'X'],
           10: ['Q', 'Z']}
rus_abc = {1: ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'],
           2: ['Д', 'К', 'Л', 'М', 'П', 'У'], 3: ['Б', 'Г', 'Ё', 'Ь', 'Я'],
           4: ['Й', 'Ы'], 5: ['Ж', 'З', 'Х', 'Ц', 'Ч'], 8: ['Ш', 'Э', 'Ю'],
           10: ['Ф', 'Щ', 'Ъ']}

def sum_eng (word):
    sum_w = 0
    for el in word:
        for k in eng_abc.keys():
            if el in eng_abc.get(k):
                sum_w += k
    return sum_w

def sum_rus(word):
    sum_w = 0
    for el in word:
        for k in rus_abc.keys():
            if el in rus_abc.get(k):
                 sum_w += k
    return sum_w

try:
    word = input('Введите слово: ').upper()
    flag_en = True
    flag_ru = True
    for el in word:
        if flag_en == True:
            # проверяем входит ли символ слова в диапозон английских букв
            # таблицы ASCII
            if 122 >= ord(el) >= 65 and not 91 <= ord(el) <= 96 \
                    and not 1040 <= ord(el) <= 1103:
                sum_word = sum_eng(word)
            else:
                flag_en = False
    for el in word:
        if flag_ru == True and flag_en == False:
            # проверяем входит ли символ слова в диапозон русских букв
            # таблицы ASCII
            if 1040 <= ord(el) <= 1103 and not 122 >= ord(el) >= 65:
                sum_word = sum_rus(word)
            else:
                flag_ru = False
                raise NewEx
except NewEx:
    print('В слове присутствуют разные раскладки или другие символы.')
else:
    print(sum_word)







