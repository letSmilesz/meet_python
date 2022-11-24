#1) Вводим с клавиатуры целое число X и У.
#Выводим на экран количество чисел между Х и У, которые делятся на 2 и 3

num1 = int(input('Write the first number: '))
num2 = int(input('Write the second number: '))
answer = 0
while num1 < num2:
    if num1 % 2 == 0 and num1 % 3 == 0:
        answer += 1
    num1 += 1

print(f'Only {answer} numbers are divisible by 2 and 3')