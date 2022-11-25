#2) Вводим с клавиатуры целое число X
#Далее вводим Х целых чисел.
#Необходимо вывести на экран максимальное и второе максимальное число из введенных чисел.

count_numbers = int(input('Write how much numbers you were write: '))
max_number = None
second_max = None

for i in range(count_numbers):
    number = (int(input('Write the number: ')))
    if max_number is None or number > max_number:
        second_max = max_number
        max_number = number
    elif second_max is None or number > second_max:
        second_max = number

print(f'Max number is {max_number}, second max number is {second_max}')