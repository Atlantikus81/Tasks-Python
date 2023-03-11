# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой
# между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

length = int(input("Введите количество долек в длину шоколадки: "))
width = int(input("Введите количество долек в ширину шоколадки: "))
numberSlices = int(input("Введите количество долек, которое хотим отломить: "))
if numberSlices == length * width:
    print("Вы хотите взять целую шоколадку. Приятного аппетита!")
else:
    if numberSlices < length * width:
        if numberSlices % length == 0 or numberSlices % width == 0:
            print("Да, шоколадку можно разломить по прямой линии")
        else:
            print("Нет, по прямой линии разломить не получится")
    else:
        print("Ну у Вас и хотелки!!! В этой шоколадке нет такого количества долек!")