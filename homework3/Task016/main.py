# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
# в массиве A[1...N]. Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

elementsCount = int(input('Введите количество элементов списка: '))
number = int(input('Введите число, которое требуется найти: '))

numberCount = 0

myList = []
for i in range(elementsCount):
    myList.append(randint(0, 9))
    if myList[i] == number:
        numberCount += 1
print(myList)
print(f'Число {number} встречается {numberCount} раз(а)')

# newList = [randint(0, 9) for i in range(elementsCount)]
# print(newList)
