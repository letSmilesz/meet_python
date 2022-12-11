# 2) Требуется по запросу выдавать N различных паролей длиной M символов, состоящих из строчных
# и прописных латинских букв # и цифр, кроме тех, которые легко перепутать между собой: «l» (L маленькое),
# «I» (i большое), «1» (цифра), «o» и «O» # (большая и маленькая буквы) и «0» (цифра).
# Решение должно содержать две функции: вспомогательную generate_password(m), возвращающую случайный пароль
# длиной m символов, и основную main(n, m), возвращающую список из n различных паролей, каждый длиной m 
# символов.

from random import choice, randint

def generate_password(m, letters):
    password = ''
    what_was = []
    for i in range(m):
        what_is = randint(0, 2)
        what_was.append(what_is)
        if i == m - 3 and 0 not in what_was or 1 not in what_was or 2 not in what_was:
            if 0 not in what_was: what_is = 0
            elif 1 not in what_was: what_is = 1
            else: what_is = 2
            what_was[len(what_was) - 1] = what_is 
        if what_is == 0: password += str(randint(2, 9))
        elif what_is == 1: password += (str(choice(letters))).upper()
        else: password += choice(letters)
    return password

def main(n, m, arr):
    passwords = []
    for i in range(n):
        passwords.append(generate_password(m, arr))
    return passwords

def print_arr(arr):
    for i in arr:
        print(i)

count = int(input('Enter, how many passwords you need: '))
length = int(input('Enter, how long passwords must been: '))
letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'z', 'x', 'c', \
    'v', 'b', 'n', 'm']
print_arr(main(count, length, letters))
