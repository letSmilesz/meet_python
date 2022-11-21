#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
    # *Примеры:* 
    
    # - 5, 25 -> да
    # - 4, 16 -> да
    # - 25, 5 -> да
    # - 8,9 -> нет

num1 = input('write the first number:')
num2 = input('write the second number:')
if num1 == pow(num2, 2) or num2 == pow(num1, 2):
    print('yes')
else:
    print('no')

#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
    # Примеры:
    
    # - 1, 4, 8, 7, 5 -> 8
    # - 78, 55, 36, 90, 2 -> 90

#Option 1
# num1 = input('write the first number:')
# num2 = input('write the second number:')
# num3 = input('write the third number:')
# num4 = input('write the fourth number:')
# num5 = input('write the fifth number:')

# max = num1
# if num2 > max:
#     max = num2
# if num3 > max:
#     max = num3
# if num4 > max:
#     max = num4
# if num5 > max:
#     max = num5

#Option 2
nums = []
max = None
for i in range(5):
    nums[i] = int(input(f'Write {i + 1} number: '))
    if i == 0:
        max = nums[i]
    elif nums[i] > max:
        max = nums[i]

print(f'Max number is {max}')



#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    
    # *Примеры:* 
    
    # - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

num = int(input('write number: '))
x = -num
if num < 0:
    while x != num - 1:
        print(x)
        x -= 1
else:
    while x != num + 1:
        print(x)
        x += 1

#2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    
    # *Примеры:*
    
    # - 6,78 -> 7
    # - 5 -> нет
    # - 0,34 -> 3

num = float(input('write number: '))
if int(num) == num:
    print('no')
else:
    print(int(num * 10) % 10)

#Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

number = int(input('write number: '))
if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number % 15 != 0:
    print('yes')
else:
    print('no') 
