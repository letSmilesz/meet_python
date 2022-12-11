from random import randint, choice

letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'z', 'x', 'c', \
    'v', 'b', 'n', 'm']

def generate_password(m):
    letters
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

def create_passwords(n, m):
    passwords = []
    for i in range(n):
        passwords.append(generate_password(m))
    return passwords