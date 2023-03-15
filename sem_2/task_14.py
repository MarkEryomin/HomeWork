# Требуется вывести все целые степени двойки (т.е. числа вида 2k)
# , не превосходящие числа N.

while True:
    try:
        N=int(input("Введите число: "))
        pov=1
        while pov<=N:
            print(pov,end=' ')
            pov*=2
        break
    except:
        print("Неверный ввод!!! Повторите ввод")
