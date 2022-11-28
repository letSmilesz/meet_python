# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def ask_numbers():
    nums = []
    i = 1
    while True:
        num = input(f'Write {i} fractional number: ')
        if num == "": break
        else: nums.append(float(num))
        i += 1
    return nums

def find_difference_of_fractional(list):
    min_el, max_el = list[0] % 1, list[0] % 1
    for i in list:
        if i % 1 > max_el: max_el = i % 1
        elif i % 1 < min_el: min_el = i % 1
    return max_el - min_el

print('     In this programm you can enter as many number as you like. When You want to stop, leave\n \
    the line empty. Then the programm will be find a difference between the minimum fractional\n \
    value and the maximum.')
numbers = ask_numbers()
print(numbers)
print(round(find_difference_of_fractional(numbers), 3)) #Станислав, вот об этом я говорил на прошлом занятии.
#Я прошу 3 числа, а round оставляет 1 после запятой
print(find_difference_of_fractional(numbers))
