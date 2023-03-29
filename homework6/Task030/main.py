# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии:
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

firstElement = int(input('Введите первый элемент списка: '))
difference = int(input('Введите разность: '))
elementsCount = int(input('Введите количество элементов списка: '))
print('----------------------------------------')

myList1 = [firstElement + (i - 1) * difference for i in range(1, elementsCount + 1)]
myList2 = [firstElement + i * difference for i in range(elementsCount)]

# myList1 = []
# for i in range(1, elementsCount + 1):
#     myList1.append(firstElement + (i - 1) * difference)

print(myList1)
print(myList2)
