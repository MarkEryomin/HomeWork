# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

def sum(a,b):
    if a==0:
        return b
    a=a-1
    return sum(a,b)+1

while True:
    try:
        flag=True
        while flag:
            a=int(input("Введите первое число : "))
            b=int(input("Введите второе число : "))
            if a<0 or b<0:
                flag=True
                print("Введите НЕ отрицательное число !!!")
            else:
                flag=False
        break
    except:
        print("Неверный ввод,попробуйте ещё")
if a>b:
    a,b=b,a
print(sum(a,b))