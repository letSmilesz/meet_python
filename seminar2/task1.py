# 1) Решить следующую задачу:  генерируем среднее арифметическое последовательности дробных чисел, вводимых с клавиатуры.
# После того, как введем последнее число  - программа выводит среднее арифметическое, максимальное 
# и минимальное значение. (не пользуемся списками и встроенными функциями)
# Количество чисел задаётся в начале работы программы

count = int(input('Write how many numbers you will enter: '))
max_num = None
min_num = None
avrg = 0

for i in range(count):
    num = float(input('Write number: '))
    if max_num is None or num > max_num:
        if min_num is None:
            min_num = max_num
        max_num = num
    elif min_num is None or num < min_num:
        min_num = num
    avrg += num

avrg /= count

print(f'Min is {min_num}, max is {max_num}, average is {avrg}')

