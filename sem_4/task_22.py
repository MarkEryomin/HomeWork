# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются 
# в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств

# Эталон

# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')

n=int(input("Введите количество элементов первого набора : "))
m=int(input("Введите количество элементов второго набора : "))

def completion(list,num):
    for i in range(num):
        list.append(int(input(f"Введите {i+1} элемент : ")))
    print(list)
    return list

list1=list()
list2=list()
completion(list1,n)
completion(list2,m)
setlist1=set(list1)
setlist2=set(list2)
print(setlist1)
print(setlist2)
list_res=list()
list1=list(setlist1)
list2=list(setlist2)
print(list1)
print(list2)


if len(list1)>len(list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                list_res.append(list1[i])
else :
    for i in range(len(list2)):
        for j in range(len(list1)):
            if list2[i]==list1[j]:
                list_res.append(list2[i])
print (list_res)

temp=0
for i in range(len(list_res)):
    for j in range(len(list_res)-1,-1):
        if list_res[i]>list_res[j]:
            temp=list_res[i]
            list_res[i]=list_res[j]
            list_res[j]=temp

print (list_res)
