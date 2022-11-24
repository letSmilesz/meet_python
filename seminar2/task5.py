# 5) Решить следующую задачу, которая вычисляет наибольший общий делитель двух целых чисел
num1 = int(input('Write the first number: '))
num2 = int(input('Write the second number: '))

if num1 > num2:
    num1, num2 = num2, num1

while num2 % num1 != 0:
    help = num1
    num1 = num2 % num1
    num2 = help

print(num1)