# 3.6 Безопасный пароль. Пользователь вбивает пароль. Нужно сказать - безопасный он или нет. 
# Безопасным считается, если он от 8 символов, есть верхний и нижний регистр. А так же цифры. 
# Можеет, при желании, добавить и спец. символы

password = input('Write your NEW password(I don`t need actual): ')
categories = ['weak', 'strong']
strong = 0
if len(password) > 7:
    up = 0
    down = 0
    digit = 0
    for i in range(len(password)):
        if password[i].isdigit(): digit += 1
        elif password[i].isupper(): up += 1
        elif password[i].islower(): down += 1
    if up != 0 and down != 0 and digit != 0: strong = 1

print(f'Password is {categories[strong]}')