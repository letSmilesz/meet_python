#3.11 Вводим с клавиатуры строку. Необходимо сказать, является ли эта строка дробным числом

def is_float(txt):
    try:
        float(txt)
        return True
    except ValueError: return False

text = input('Enter the text or number: ')
if is_float(text):
    num = float(text)
    if num % 1 == 0:
        num = int(text)
    print(f'You`re enter {type(num)} type.')
else: print('You`re enter string')
