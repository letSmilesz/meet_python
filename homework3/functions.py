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