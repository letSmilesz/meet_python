import math
# task1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

day = int(input('Write number of day of week to check, is it workday:'))
if 0 < day < 6:
    print('no')
elif 5 < day < 8:
    print('yes')
else:
    print('write correct number')

# task2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('Write values to this statement: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for i in range (2):
    x = False
    if i == 1:
        x = True
    for j in range (2):
        y = False
        if j == 1:
            y = True
        for l in range (2):
            z = False
            if l == 1:
                z = True
            print(f'X = {x}, Y = {y}, Z = {z}, answer = {not(x or y or z) == (not x and not y and not z)}')

# task3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('write coordinate x:'))
y = int(input('write coordinate y:'))

if x > 0:
    if y > 0:
        print('the first quarter')
    else:
        print('the fourth quarter')
else:
    if y > 0:
        print('the second quarter')
    else:
        print('the third quarter')

# task4. Напишите программу, которая по заданному номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

quarter = int(input('write the number of quarter'))
if quarter == 1:
    print('x = (0, +infinity), y = (0, +infinity)')
elif quarter == 2:
    print('x = (-infinity, 0), y = (0, +infinity)')
elif quarter == 3:
    print('x = (-infinity, 0), y = (-infinity, 0)')
elif quarter == 4:
    print('x = (0, +infinity), y = (-infinity, 0)')
else:
    print('write correct number')

# task5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

x1 = int(input('write coordinate x1:'))
y1 = int(input('write coordinate y1:'))
x2 = int(input('write coordinate x2:'))
y2 = int(input('write coordinate y2:'))

distance = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
print(f'distance = {round(distance, 3)}')
