#сделать игру крестики-нолики
import os

def print_field(arr, size):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0: print(' ', end = '')
            elif arr[i][j] == 1: print('0', end = '')
            elif arr[i][j] == 2: print('X', end = '')
            if j != len(arr) - 1: print('|', end = '')
        print()
        if i < len(arr) - 1: print('--' * size)
        else: print()

def check_lines(arr):
    for i in range(len(arr)):
        x = 0
        o = 0
        for j in range(len(arr)):
            if arr[i][j] == 1: o += 1
            elif arr[i][j] == 2: x += 1
        if o == len(arr) or x == len(arr): return True
    else: return False

def check_colls(arr):
    for i in range(len(arr)):
        x = 0
        o = 0
        for j in range(len(arr)):
            if arr[j][i] == 1: o += 1
            elif arr[j][i] == 2: x += 1
        if o == len(arr) or x == len(arr): return True
    else: return False

def check_diag(arr):
    x1 = 0
    o1 = 0
    x2 = 0
    o2 = 0
    length = len(arr) - 1
    for i in range(len(arr)):
        if arr[i][i] == 1: o1 += 1
        if arr[length - i][i] == 1: o2 += 1
        if arr[i][i] == 2: x1 += 1
        if arr[length - i][i] == 2: x2 += 1
    if o1 == len(arr) or x1 == len(arr) or x2 == len(arr) or o2 == len(arr): return True
    else: return False

def check(arr):
    if check_lines(arr) or check_colls(arr) or check_diag(arr): return True
    else: return False

def correct_answer(ans: str):
    if ans.count(',') != 1 or len(ans) != 3 or ans[0].isdigit() == False or \
        ans[2].isdigit() == False: return False
    else: return True

def clear():
    os.system('CLS')

while True:
    while True:
        size = 3#int(input('Enter the size of field(standart and minimal is 3x3): '))
        if size > 2: break
    field = [[0 for i in range(size)] for i in range(size)]
    print('Rules:\n1) Player 1 - "0", Player 2 - "X".\n2) Answer is two numbers through comma. Begin from 1\
        \n3) The winner is the one who first builds a line in any direction \n4) To exit leave the field empty\
        (in game press "Enter"\n\nTo continue press "Enter"')
    input()
    clear()
    player = 0
    while True:
        if player == 1: player = 2
        else: player = 1
        while True:
            print_field(field, size)
            answer = input(f'Player {player}, enter your cell(-1,-1): ')
            clear()
            if answer == '':
                break
            elif correct_answer(answer) == True:
                i, j = answer.split(',')
                i, j = int(i) - 1, int(j) - 1
                if field[i][j] == 0: 
                    field[i][j] += player
                    break
                else: 
                    print('You choose wrong cell, it`s busy. Repeat!')
            else: print('You entered incorrect answer. Repeat!')
        if check(field): 
            print(f'Winner is Player {player}!')
            print_field(field, size)
            break
    exit = input('Do you want one more game? Enter "yes" or "no": ')
    exit = exit.lower()
    if exit == 'no': break
    else: clear()
