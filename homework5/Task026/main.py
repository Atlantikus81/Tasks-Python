# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

number = int(input('Введите любое целое число: '))
exponentNum = int(input('Введите неотрицательный показатель степени: '))
print('-------------------------------')


def exponentiation(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * exponentiation(base, exponent - 1)


print(f'{number}^{exponentNum} = {exponentiation(number, exponentNum)}')
