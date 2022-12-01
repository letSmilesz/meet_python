# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

lenth = int(input('Enter the length of list: '))
nums = []
for i in range(lenth):
    nums.append(random.randint(0, 10))

summ = 0
for i in range(1, len(nums), 2):
    summ += nums[i]

print(nums)
print(summ)
