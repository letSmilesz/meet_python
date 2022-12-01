# 3) Вводим с клавиатуры целое число - это зарплата.
# Нужно вывести в консоль -  Минимальное кол-во  купюр, которыми можно выдать ЗП.
# И сколько, и каких бухгалтер выдаст 25 рублевых купюр,  10 рублевых, 5 рублевых и 1 рублевых

salary = int(input('Write salary: '))
salary_help = salary
bills = [0, 0, 0, 0]
# option 1
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

# option 2
# k = 0
# for j in 25, 10, 3, 1:
#     bills[k] = salary_help // j
#     salary_help -= bills[k] * j
#     if salary_help == 0:
#         break
#     k += 1
# count = 0
# for i in bills:
#     count += i
#print(f'Salary {salary} can be paid as: 25: {bills[0]}, 10: {bills[1]}, 3: {bills[2]}, 1: {bills[3]}')


# option 3
F = []
F.append(0)
bills_count = 4
bills_nominal = [1, 3, 10, 25]
n = salary
for i in range(1, n + 1, 1):
    F.append(100000)
    for j in range(bills_count):
        if i >= bills_nominal[j] and F[i - bills_nominal[j]] + 1 < F[i]:
            F[i] = F[i - bills_nominal[j]] + 1

while n > 0:
    for i in range(bills_count):
        if F[n - bills_nominal[i]] == F[n] - 1:
            bills[i] += 1
            n -= bills_nominal[i]
            break

print(f'Salary {salary} can be paid as: 25: {bills[3]}, 10: {bills[2]}, 3: {bills[1]}, 1: {bills[0]}')