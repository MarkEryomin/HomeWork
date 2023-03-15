# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали 
# билет с номером. Счастливым билетом называют такой
# билет с шестизначным номером, где сумма первых трех
# цифр равна сумме последних трех. Т.е. билет с 
# номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет 
# счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

flag=True
while flag:
    Num=input('Введите номер билета : ')
    if len(Num)!=6:
        print('Неверный номер билета')
    else :
        flag=False
         
Left=int(Num[0])+int(Num[1])+int(Num[2])
SumLeft=int(Left)
Right=int(Num[3])+int(Num[4])+int(Num[5])
SumRight=int(Right)
print("Сумма левой части {}={} и правой {}={}".format(Num[:3],SumLeft,Num[3:],SumRight))
if SumRight==SumLeft:
    print('Ура!!! Счастливый билет!!!')
else :
    print('Попробуйте ещё ')






# flag=True
# while flag:
#     Num=input('Введите номер билета : ')
#     if len(Num)!=6:
#         print('Неверный номер билета')
#     else:
#         i=0
#         while i <len(Num):

#         print('Неверный номер билета!!!!')
#     else :
#         flag=False
#         # if i.isdigit() == False or j.isdigit() == False: