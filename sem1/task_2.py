#  Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


flag=True
while flag:
    n=input('Введите трёхзначное число : ')
    if n.isdigit() == False :
        print('Ввели не число !!!')
        print('Попробуйте ещё !!!')
    else:
        n=int(n)
        if n<100 or n>1000:
            print('Ввели не трёхзначное число !!!')
            print('Попробуйте ещё !!!')
        else:
            flag=False

sum=0
while n>0:
    x=n%10
    sum=sum+x
    n=n//10
print(sum)





  