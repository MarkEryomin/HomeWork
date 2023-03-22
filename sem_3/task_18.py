# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число,
# которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые
# равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6

import random




N=int(input("Введите длинну массива : "))
X=int(input("Введите искомое число : "))

default_list=[random.randint(1, N) for i in range(N)]
print(default_list)


diff_num = abs(X - default_list[0])
min_num=N
for i in range(len(default_list)):
    if default_list[i]!=X:
        if diff_num>=(abs(X - default_list[i])):
            diff_num = abs(X - default_list[i])
            min_num = default_list[i]
    print(f"{i},{diff_num}={X}-{default_list[i]}>>>{min_num}")
print(min_num)



# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)

# k = int(input())
# m = abs(k - list_1[0])  # модуль числа

# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)