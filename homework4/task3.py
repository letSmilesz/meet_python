# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию, методом сортировки выбором.
import random

nums = []
for i in range(30):
    nums.append(random.randint(0,100))
print(nums)

for i in range(len(nums)):
    min_index = i
    for j in range(i, len(nums)):
        if nums[j] < nums[min_index]: min_index = j
    nums[i], nums[min_index] = nums[min_index], nums[i]
print(nums)
print(len(nums))