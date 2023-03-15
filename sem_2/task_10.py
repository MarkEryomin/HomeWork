# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество
# монет, которые нужно перевернуть



import random

while True:
    try:
        coins=int(input("Введите общее количество монет: "))
        side=list()
        heads=0
        tails=0
        for i in range(coins):
            side.append(random.randint(0,1))
            if side[i]==0:
                heads+=1
            else:
                tails+=1
        print(side)
        if heads<tails:
            print(f"Необходимо перевернуть {heads} шт.")
        else :
            print(f"Необходимо перевернуть {tails} шт.")
        break
    except:
        print("Неверный ввод!!! Повторите ввод")
