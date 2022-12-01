# 2) Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)
import random

length = int(input('Enter length of the table: '))
height = int(input('Enter height of the table: '))

table = []
avg_lines = []
for i in range(height):
    table.append(list())
    summ = 0
    for j in range(length):
        table[i].append(random.randint(0, 10))
        summ += table[i][j]
    avg_lines.append(summ // length)
    print(f'{table[i]} - average is {avg_lines[i]}')

