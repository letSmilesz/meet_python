# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibonacci(num):
    #F[n] = F[n - 1] + F[n - 2] +
    #F[n] = F[n + 1] - F[n + 2] -
    fib = []
    fib.append(0)
    fib.append(1)
    for i in range(2, num + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    fib.insert(0, 1)
    for i in range (1, num):
        fib.insert(0, fib[1] - fib[0])
    print(fib)

num = int(input('Write number: '))
fibonacci(num)
