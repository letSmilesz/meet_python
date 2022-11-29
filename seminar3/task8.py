# 3.8 Написать программу, которая скажет в веденной строке индекс второго символа "v"
def find_second_letter(txt: str, letter):
    count = 0
    for i in range(len(text)):
        if text[i] == letter:
            count += 1
        if count == 2: return i
    return None

text = input('Enter some text: ')
letter = input('Enter the letter we are looking for: ')
index = find_second_letter(text, letter)
if index is None: print(f'The letter "{letter}" is not repeats')
else: print(f'The second time the letter "{letter}" occurs at {index} index')