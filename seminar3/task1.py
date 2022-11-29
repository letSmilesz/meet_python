# 3.1 Вводим с клавиатуры десятичное число. Необходимо перевести его  в двоичную систему счисления.
num = int(input('Write number: '))

def to_binary(num):
    ans = ''
    while num > 0:
        help = num % 2
        ans = str(help) + ans
        num //= 2
    return ans

print(to_binary(num))