# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import functions

def find_multiplication_on_pairs(list):
    result = []
    count = len(list) // 2 if len(list) % 2 == 0 else len(list) // 2 + 1
    for i in range(count):
        result.append(list[i] * list[len(list) - 1 - i])
    return result

length, min_el, max_el = functions.ask_parameters_to_list()
numbers = functions.create_list_of_numbers(length, min_el, max_el)
res = find_multiplication_on_pairs(numbers)
print(numbers)
print(res)
