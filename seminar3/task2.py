# 3.2 Вводим любую строку текста (на русском). Необходимо посчитать количество гласных и согласных букв.

text = input('Write some text in English: ')
vowels_letters = ['e', 'y', 'u', 'i', 'o', 'a']
text = text.lower()
text = text.replace(' ', '')
vowels = 0
for i in vowels_letters:
    vowels += text.count(i)
consonants = len(text) - vowels
print(text)
print(vowels)
print(consonants)