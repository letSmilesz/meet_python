#Проверить правильную скобочную последовательность

def check(txt: str):
    if txt.count('(') != txt.count(')'): return False
    else:
        parentheses = 0
        for i in txt:
            if i == ')': parentheses += 1
            elif i == '(': parentheses += 1
            if parentheses < 0: return False
        else: return True

string = input('Enter string: ')
ans = check(string)
if ans == True: print('Normal')
else: print('Bad')
