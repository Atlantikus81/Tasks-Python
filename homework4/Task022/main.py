# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

elementsCount1 = int(input('Введите количество элементов первого множества: '))
elementsCount2 = int(input('Введите количество элементов второго множества: '))
minValue = int(input('Введите минимальное значение элемента: '))
maxValue = int(input('Введите максимальное значение элемента: '))

myList1 = [randint(minValue, maxValue) for i in range(elementsCount1)]
print(myList1)
myList2 = [randint(minValue, maxValue) for i in range(elementsCount2)]
print(myList2)
print('-------------------------------------')

newList = []
for i in range(len(myList1)):
    for j in range(len(myList2)):
        if myList1[i] == myList2[j]:
            newList.append(myList1[i])
print(newList)

uniqueElementsList = list(set(newList))
print(uniqueElementsList)
resultList = sorted(uniqueElementsList)
print(resultList)
