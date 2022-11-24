#4) Вводим с клавиатуры многозначное число
#Необходимо узнать и сказать последовательность цифр этого числа при просмотре слева направо 
# упорядочена по возрастанию или нет.
#Например 1579 - да ( 1 меньше 5, 5 меньше 7, а 7 меньше 9), 1427 - нет

num = int(input('Write multi-digit number: '))
ascending = False

#option 1
while num > 9:
    num_help = num
    div = 1
    while num_help > 9:
        div *= 10
        num_help //= 10
    if num // div > (num / (div / 10)) % 10:
        ascending = False
        break
    else:
        num %= div
        ascending = True
    
#option 2
numbers = []
while num > 0:
    numbers.append(num % 10)
    num //= 10
for i in range(len(numbers) - 1):
    if numbers[i] < numbers[i + 1]:
        ascending = False
    else:
        ascending = True

print(ascending)