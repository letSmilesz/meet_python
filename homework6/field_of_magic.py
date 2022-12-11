#Сделать поле чудес

from random import randint, choice
from os import system
from time import sleep

def clear(): system('CLS')

def plug(): pass

def print_game(word, know_letters, theme = '', points = 0):
    if theme != '': print(f'The theme of game: {theme}!             You have {points} points!')
    print()
    print('---' * len(word))
    for i in range(len(word)):
        if i == 0: print('| ', end = '')
        if i == len(word): print(' |')
        elif know_letters[i] == 1: print('  ', end = '|')
        elif know_letters[i] == 2: print(f'{word[i]} ', end = '|')
        else: print('* ', end = '|')
    print('\n' + '---' * len(word))

def animation(txt: str, bool = False, f = plug, word = '', know_letters = [], points = 0):
    clear()
    for i in range(5):
        if i < 3: print(txt + '.' * i)
        else: print(txt + '.' * (i - 3))
        if bool: f(word, know_letters)
        sleep(0.5)
        clear()

def animation2(word, know_letters, letter):
    clear()
    for i in range(len(word)):
            if word[i] == letter:
                for j in range(3):
                    print_game(word, know_letters)
                    if j < 2: know_letters[i] += 1
                    sleep(1)
                    clear()

def create_list(word):
    arr = [0 for i in range(len(word))]
    return arr

def print_rules(theme):
    print(f'Rules: \nThe theme of game is "{theme}"!\nYour task is as soon as possible guess the word!'
    + 'You have 15 attempts.\nYou must enter the letter that you think is present in the word. '
    + '\nEach turn the drum will spin, which will show how many points you get for guessing the '
    + '\nletter, and there is also a chance to get a bonus sector! \nAlso, if you know the word, you '
    + 'can enter in its entirety! \nTo exit the game, leave the line blank and press "Enter".'
    + ' \n\nTo continue press "Enter"')
    input()
    clear()

def drum(turn):
    values = [1, 3, 5, 8, 10, 15, 30, 40, 50, 60, 70, 80, 90, 100, 999]
    prizes = ['x', 'b', 'p']
    animation('The drum is revolving.')
    if turn > 2: 
        value = values[randint(0, len(values) - 1)]
        if value == 999: value = choice(prizes)
    else: value = values[randint(0, len(values) - 2)]
    if value == 'p': print('You have sector "Plus", you can open any letter!')
    elif value == 'x': print('Lucky! How many letters you guess - so many times the number of'
        + 'points will increase!')
    elif value == 'b': print('Bad luck :(\nYou caught sector "Bankrupt". All your points are gone')
    else: print(f'You will have {value} points if you quess the letter!')
    return value

def end_of_game(bool, word, know_letters, points):
    if bool: print('You quessed!')
    else: print('I`m sorry, you lost :(')
    print_game(word, know_letters)
    print(f'At the end of game you had {points} points.')

def check_num_letter(num_letter, word, know_letters):
    if 0 > num_letter or num_letter > len(word): 
            for i in range(len(word)):
                if know_letters[i] == 0: 
                    num_letter = i
                    break
    return num_letter

dictionary = {'art': ('brightness', 'illustration'), 'birds': ('flycatcher', 'grosbeak'),
    'computers': ('cyberspace', 'development'), 'driving': ('expressway', 'cloverleaf')}
themes = ['art', 'birds', 'computers', 'driving']
entered_letters = []
theme = choice(themes)
word = str(dictionary.get(theme)[randint(0,1)])
know_letters = create_list(word)
points = 0

print_rules(theme)
for i in range(15):
    value = drum(i)
    print_game(word, know_letters, theme, points)
    if value == 'p': 
        num_letter = int(input('Which letter do you choose? Enter it`s number: '))
        num_letter = check_num_letter(num_letter, word, know_letters)
        animation2(word, know_letters, word[num_letter - 1])
        print_game(word, know_letters, theme, points)
    if value == 'b': 
        points = 0
        continue
    else: letter = input('Which letter do you choose? Enter it: ')
    if len(letter) > 1: 
        answer = input('Are you sure you want to enter the whole word? Enter "yes" or "no": ').lower()
        if answer == 'yes': 
            animation('You.', True, print_game, word, know_letters)
            know_letters = [2 for i in range(len(know_letters))]
            if letter == word:
                end_of_game(True, word, know_letters, points)
                break
            else: 
                end_of_game(False, word, know_letters, points)
                break
        else: 
            letter = input('Which letter do you choose? Enter it: ')
            if len(letter) > 1: letter = letter[0]
    elif letter == '': 
        clear()
        print('You are out of the game :(')
        break
    if letter in entered_letters:
        clear()
        print('You already mentioned this letter!')
        sleep(3)
        continue
    else: entered_letters.append(letter)
    animation('You.', True, print_game, word, know_letters)
    if word.count(letter) > 0:
        print('You guessed!')
        sleep(3)
        animation2(word, know_letters, letter)
        if value == 'x': points *= word.count(letter) + 1
        else: points += value
        if not(0 in know_letters): 
            clear()
            end_of_game(True, word, know_letters, points)
            break
    else: 
        print('You didn`t guess :(')
        sleep(3)
else: end_of_game(False, word, know_letters, points)