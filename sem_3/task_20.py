# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо 
# только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
word = input("Введите слово: ").upper()
count = 0
for i in word:
    if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        for j in points_en:
            if i in points_en[j]:
                count = count + j
    else:
        for j in points_en:
            if i in points_ru[j]:
                count = count + j
print(f"Стоимость слова: {count}")

# # Вариант 2
# dictionary = {
# 'a':1, 'e':1, 'i':1, 'l':1, 'n':1, 'o':1, 'r':1, 's':1, 't':1, 'u':1,
# 'd':2, 'g':2,
# 'b':3, 'c':3, 'm':3, 'p':3,
# 'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
# 'k':5,
# 'j':8, 'x':8,
# 'q':10, 'z':10,
# 'а':1, 'в':1, 'е':1, 'и':1, 'н':1, 'о':1, 'р':1, 'с':1, 'т':1,
# 'д':2, 'к':2, 'л':2, 'м':2, 'п':2, 'у':2,
# 'б':3, 'г':3, 'ё':3, 'ь':3, 'я':3,
# 'й':4, 'ы':4,
# 'ж':5, 'з':5, 'х':5, 'ц':5, 'ч':5,
# 'ш':8, 'э':8, 'ю':8,
# 'ф':10, 'щ':10, 'ъ':10
# }

# word = input('Введите слово -> ')
# word = word.lower()

# result = 0
# for i in word:
#     result += dictionary[i]

# print('Стоимость введенного вами слова:', result)