# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно 
# два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
# число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь 
# перед некоторым кустом заданной во входном файле грядки

import random

while(True):
    beds_number = input("Введите количество грядок: ")
    if(beds_number.isdigit() == False or int(beds_number) < 3):
        print("Введите ЧИСЛО от трех")
    else:
        break

beds_array = [random.randint(1, 100) for _ in range(int(beds_number))]
print(beds_array)

last_element = beds_array[-2]
last_element_index = -2
next_element = beds_array[0]
next_element_index = 0
temp = beds_array[-2] + beds_array[-1] + beds_array[0]
result = temp
result_position = -1
for i in range(-2, len(beds_array) - 3):
    next_element = beds_array[next_element_index + 1]
    next_element_index += 1
    temp += next_element - last_element
    last_element = beds_array[last_element_index + 1]
    last_element_index += 1
    if result < temp:
        result = temp
        result_position = next_element_index
    if result_position==-1:
        result_position=beds_number
print("Максимальное количество ягод: " + str(result) + "\nНужно начинать с куста под номером: " + str(result_position))