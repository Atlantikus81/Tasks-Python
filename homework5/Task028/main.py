# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4
#

firstNumber = int(input('Введите первое число: '))
secondNumber = int(input('Введите второе число: '))
print('----------------------------')


def summ(a, b):
    if a >= 0:
        if a == 0:
            return b
        else:
            return summ(a - 1, b + 1)
    else:
        if b == 0:
            return a
        else:
            return summ(a + 1, b - 1)


result = summ(firstNumber, secondNumber)
print(f'{firstNumber} + {secondNumber} = {result}')
