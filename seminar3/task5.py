# 3.5 Вводим любую строку и нужно посчитать кол-во символов в верхнем регистре

text = input('Enter some text: ')
count = 0
for i in range(len(text)):
    if text[i].isupper(): count += 1
print(count)