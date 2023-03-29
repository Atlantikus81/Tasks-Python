# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

elementsCount = int(input('Введите количество элементов списка: '))
minValue = int(input('Введите нижнее значение диапазона: '))
maxValue = int(input('Введите верхнее значение диапазона: '))

myList = [randint(0, 100) for i in range(elementsCount)]
print(myList)
print('------------------------------------------------------------')

indexList = [i for i in range(len(myList)) if minValue <= myList[i] <= maxValue]

# indexList = []
# for i in range(len(myList)):
#     if minValue <= myList[i] <= maxValue:
#         indexList.append(i)

print(f'Индексы элементов из заданного диапазона: {indexList}')
