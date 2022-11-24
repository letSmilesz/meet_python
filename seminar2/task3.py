import random
# 3) Решить следующую задачу, проверки знания таблицы умножения. Программа выводит 10 примеров 
# и выставляет за 10 правильных ответов - пять, за 9 и 8 - 4 балла, за меньше - три. 
# Если пользователь ошибся в каком-то ответе - сообщаем ему об этом
# В итоге выводим количество верных ответов и оценку

correct_answer = 0
for i in range (10):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = int(input(f'{a} x {b} = ?'))
    if answer == a * b: correct_answer += 1
    else: print(f'You wrong. Correct answer is {a * b}')

if correct_answer == 10: print(f'You answer right at {correct_answer} questions, your grade is five')
elif correct_answer > 7: print(f'You answer right at {correct_answer} questions, your grade is four')
else: print(f'You answer right at {correct_answer} questions, your grade is three')