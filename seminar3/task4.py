# 3.4 Напишем программу, которая из введённой строки пользователя, поделит её пополам и поменяет половинки местами

def replace_half_text(text: str):
    half = len(text) // 2
    if len(text) % 2 != 0: half += 1
    return text[half: len(text)] + text[0: half]

text = input('Enter some text: ')
print(replace_half_text(text))