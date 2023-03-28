# Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

while True:
    try:
        n=int(input("Введите длинну массива : "))
        a=int(input("Введите низ диапазона : "))
        b=int(input("Введите верх диапазона : "))
        break
    except:
        print("Неверный ввод,попробуйте ещё")
random_list=[random.randint(-10, 10) for i in range(10)]
print(random_list)
find_list=list()
for i in range(len(random_list)):
    if random_list[i]>=a and random_list[i]<=b:
        find_list.append(i)
print(find_list)

  
