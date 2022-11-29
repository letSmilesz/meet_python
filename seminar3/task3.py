# 3.3 Вводим любое слово\словочетание - определить, является ли оно палиндромом
text = input('Enter a word or phrase: ')
text.lower()
if text == text[:: -1]: print('It`s palindrom!')
else: print('It isn`t palindrom')