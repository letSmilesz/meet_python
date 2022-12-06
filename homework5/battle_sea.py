#Сделать игру морской бой
import random
import os

def print_field(arr, width, height, hide):
    for i in range(height):
        if i == 0 or i == height - 1: continue
        for j in range(width):
            if j == 0 or j == width - 1: continue
            elif arr[i][j] == 0: print('o', end = ' ')
            elif arr[i][j] == 1:
                if hide: print('o', end = ' ')
                else: print('W', end = ' ')
            elif arr[i][j] == 2: print('X', end = ' ')
            else: print(0, end = ' ')
        print()

def check_ships_around(field, i, j, decks):
    for l in range(i - 1, i + decks + 1, 1):
        if field[l][j - 1] != 0: return False
        elif field[l][j] != 0: return False
        elif field[l][j + 1] != 0: return False
    else: return True

complexity = {'easy': (1, 7, 10), 'medium': (3, 7, 8), 'hard': (5, 9, 10)}
for i in complexity:
    os.system('CLS')
    a, b, c = complexity[i]
    width, height = b, b
    field = [[0 for i in range(width)] for i in range(height)]
    for j in range(a): 
        while True:
            d, e = random.randint(1, height - 2), random.randint(1, width - 2)
            if check_ships_around(field, d, e, 1): 
                field[d][e] = 1
                break
    print(f'You started game at {i} complexity! You have {a} enemies and {c} shots. Good luck!')
    count = 0
    for j in range(c):
        print(f'You have {c - j} shots, {j} has been done.')
        while True:
            print_field(field, width, height, True)
            shoot = input('Enter your choise, comma separated row and cell("0,0" or "10,10"): ')
            os.system('CLS')
            shoot_i, shoot_j = shoot.split(',')
            shoot_i, shoot_j = int(shoot_i), int(shoot_j)
            if (0 < shoot_i < height) and (0 < shoot_j < width): break
            else: print('You entered irregular cell!') 
        if field[shoot_i][shoot_j] == 1: 
            field[shoot_i][shoot_j] = 2
            count += 1
        else: field[shoot_i][shoot_j] = 3
        if count == a: 
            print(f'You win at {j + 1} shoots!')
            print_field(field, width, height, False)
            break
    else: 
        print('You lose')
        print_field(field, width, height, False)
    input('Press "Enter" to continue')
