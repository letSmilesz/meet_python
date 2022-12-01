# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Enter the number:'))
nums = []
for i in range(1, n + 1):
    if i == 1: nums.append(i)
    else: nums.append(i * nums[i - 2])

print(nums)