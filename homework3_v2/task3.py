# 3.12 Вводим с клаиватуры строку. Необходимо вывести строку, где развернём подстроку между первой 
# и последней буквой "о" из исходной строки. Если она только одна или её нет - то сообщить, что буква 
# "о" - одна или не встречается.

def reverse_between_letter(text: str, letter):
    start = text.find(letter)
    end = text.rfind(letter)
    if start == -1: return (f'In this text noone letter "{letter}"')
    elif start == end: return (f'In this text only one letter "{letter}"')
    else: return text[0:start] + text[end:start:-1] + text[end:len(text)]

text = input('Enter the text: ')
print(reverse_between_letter(text.lower(), 'o'))