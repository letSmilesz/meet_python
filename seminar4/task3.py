# 3) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и 
# последний элемент, второй и предпоследний и т.д.
#     *Пример:*
#     - [2, 3, 4, 5, 6] => [12, 15, 4];
#     - [2, 3, 5, 6] => [12, 15]
import random

nums = []
for i in range(5):
    nums.append(random.randint(0, 15))

res = []
for i in range((len(nums) // 2) + len(nums) % 2):
    res.append(nums[i] * nums[len(nums) -1 - i])
if len(nums) // 2 != 0: res.append(nums[len(nums) // 2 + 1])

print(nums)
print(res)