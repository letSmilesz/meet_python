#3) Вводим с клавиатуры целое число - это зарплата.
#Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
#И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 5 рублевых и 1 рублевых

salary = int(input('Write salary: '))
salary_help = salary
bills = [0, 0, 0, 0]

#option 1
# while salary_help != 0:
#     if salary_help % 25 == 0:
#         bills[0] += 1
#         salary_help -= 25
#     elif salary_help % 10 == 0:
#         bills[1] += 1
#         salary_help -= 10
#     elif salary_help % 5 == 0:
#         bills[2] += 1
#         salary_help -= 5
#     else:
#         bills[3] += 1
#         salary_help -= 1

#option 2
i = 0
for j in 25, 10, 5, 1:
    bills[i] = salary_help // j
    salary_help -= bills[i] * j
    if salary_help == 0: break
    i += 1

print(f'Salary {salary} can be paid as: 25 - {bills[0]}, 10 - {bills[1]}, 5 - {bills[2]}, 1 - {bills[3]}')