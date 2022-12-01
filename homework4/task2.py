# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
import random

length = 10#int(input('Enter length of the table: '))
height = 10#int(input('Enter height of the table: '))

table = []
sum_lines = []
for i in range(length):
    table.append(list())
    summ = 0
    for j in range(height):
        table[i].append(random.randint(0, 10))
        summ += table[i][j]
    sum_lines.append(summ)
    print(f'{table[i]} - sum is {sum_lines[i]}')

