import time
'''
for h in range(10000, 15000):

    salary = h
    salary_help = salary
    bills1 = [0, 0, 0, 0]
    # option 2
    start_time = time.time()
    k = 0
    for j in 25, 10, 3, 1:
        bills1[k] = salary_help // j
        salary_help -= bills1[k] * j
        if salary_help == 0:
            break
        k += 1
    count = 0
    for i in bills1:
        count += i
    time1 = time.time() - start_time

    bills2 = [0, 0, 0, 0]
    # option 3
    start_time = time.time()
    F = []
    F.append(0)
    bills_count = 4
    bills_nominal = [25, 10, 3, 1]
    n = salary
    for i in range(1, n + 1, 1):
        F.append(100000)
        for j in range(bills_count):
            if i >= bills_nominal[j] and F[i - bills_nominal[j]] + 1 < F[i]:
                F[i] = F[i - bills_nominal[j]] + 1

    while n > 0:
        for i in range(bills_count):
            if F[n - bills_nominal[i]] == F[n] - 1:
                bills2[i] += 1
                n -= bills_nominal[i]
                break
    time2 = time.time() - start_time

if (count - F[len(F) - 1]) > 1:
    print(f'1) Salary {salary}. {count} bills')
    print(f'2) Salary {salary}. {F[len(F) - 1]} bills')
else:
    print('end')
'''

salary = int(input('Write salary: '))
salary_help = salary
bills1 = [0, 0, 0, 0]
# option 2
start_time = time.time()
k = 0
for j in 25, 10, 3, 1:
    bills1[k] = salary_help // j
    salary_help -= bills1[k] * j
    if salary_help == 0:
        break
    k += 1
count = 0
for i in bills1:
    count += i
time1 = time.time() - start_time

bills2 = [0, 0, 0, 0]

# option 3
start_time = time.time()
F = []
F.append(0)
bills_count = 4
bills_nominal = [25, 10, 3, 1]
n = salary
for i in range(1, n + 1, 1):
    F.append(100000)
    for j in range(bills_count):
        if i >= bills_nominal[j] and F[i - bills_nominal[j]] + 1 < F[i]:
            F[i] = F[i - bills_nominal[j]] + 1
while n > 0:
    for i in range(bills_count):
        if F[n - bills_nominal[i]] == F[n] - 1:
            bills2[i] += 1
            n -= bills_nominal[i]
            break
time2 = time.time() - start_time

print(f'1) Salary {salary}. {count} bills, time for first option - {time1}')
print(
    f'2) Salary {salary}. {F[len(F) - 1]} bills, time for second option - {time2}')
