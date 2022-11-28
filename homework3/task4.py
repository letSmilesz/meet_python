# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert_to_binary(num):
    answer = ""
    while num > 0:
        answer = str(num % 2) + answer
        num //= 2
    return answer

def recursion_convert_to_binary(num):
    if num == 0: return ""
    else: return recursion_convert_to_binary(num // 2) + str(num % 2)

number = int(input('Enter the number you want to convert to binary: '))
print(convert_to_binary(number))
print(recursion_convert_to_binary(number))
