# Задача 18: Требуется найти в массиве A[1...N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

elementsCount = int(input('Введите количество элементов списка: '))
number = int(input('Введите число, с которым требуется сравнивать элементы списка: '))

myList = []
for i in range(elementsCount):
    myList.append(randint(-9, 9))
print(myList)

difference = abs(number - myList[0])
element = myList[0]
for i in range(len(myList)):
    if abs(number - myList[i]) < difference:
        difference = abs(number - myList[i])
        element = myList[i]
print('-----------------------------------------------')
print(f'Элемент {element} самый близкий по величине к числу {number}')
