#3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.

def convert_to_hexademical(num):
    ans = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f']
    while num > 0:
        char = num % 16
        if char < 10: ans = str(char) + ans
        else:
            ans = letters[char - 10] + ans
        num //= 16
    return ans

num = int(input('Enter the number: '))
print(convert_to_hexademical(num))

