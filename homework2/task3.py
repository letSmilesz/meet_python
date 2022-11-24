#3) Вводим с клавиатуры целое число - это зарплата.
#Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
#И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 5 рублевых и 1 рублевых

salary = int(input('Write salary: '))
salary_help = salary
twentifive = 0
ten = 0
five = 0
one = 0
while salary_help != 0:
    if salary_help % 25 == 0:
        twentifive += 1
        salary_help -= 25
    elif salary_help % 10 == 0:
        ten += 1
        salary_help -= 10
    elif salary_help % 5 == 0:
        five += 1
        salary_help -= 5
    else:
        one += 1
        salary_help -= 1

print(f'Salary {salary} can be paid as: 25 - {twentifive}, 10 - {ten}, 5 - {five}, 1 - {one}')