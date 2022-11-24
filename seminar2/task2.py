# 2) Решить следующую задачу:Вывести на экран таблицу умножения на заданное число.

num = int(input('Write the number: '))
for i in range(1, 11):
    print(f'{i} x {num} = {i * num}')