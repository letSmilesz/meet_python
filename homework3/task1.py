#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих 
# на нечётной позиции.
#Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def create_list_of_numbers(length, min, max):
    nums = []
    for i in range(length):
        nums.append(random.randint(min, max))
    return nums

def find_sum_on_index (list, start_index: 0, step: 1):
    sum_on_index = 0
    for i in range(start_index, len(list), step):
       sum_on_index += list[i]
    return sum_on_index

def ask_parameters_to_list():
    length, min_el, max_el = map(int, input('Write the length of list, min and max element \
    in it(separated by commas): ').split(','))
    return length, min_el, max_el

length, min_element, max_element = ask_parameters_to_list()
numbers = create_list_of_numbers(length, min_element, max_element)
repeat = int(input('Write, which one to take(1 for even, 2 for odd, 3 for every third and so on):'))
begin = repeat - 1
sums = find_sum_on_index(numbers, begin, repeat)
print(numbers)
print(sums)
