# 3.7 Вводим строку с клавиатуры. Необходимо сказать, какой символ встречается чаще всего

text = input('Enter some text: ')
letters = {}
for i in range(len(text)):
    try:
        letters[text[i]] += 1
    except KeyError: letters[text[i]] = 1
letter_win = text[0]
for i in letters:
    if letters[i] > letters[letter_win]: letter_win = i
print(f'The "{letter_win}" is most popular in this text. It meets {letters[letter_win]} counts.') 