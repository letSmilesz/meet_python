# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых 
# низкие оценки

from random import choice as ch
from random import randint as r

class Student:
    def __init__(self, name, group, progress) -> None:
        self.name = name
        self.group = group
        self.progress = progress

    def __str__(self) -> str:
        return f'{self.name}, group: {self.group}, success is {self.get_avg_p()}\nFull progress is {self.progress}'

    def get_name(self) -> str:
        return self.name

    def get_progress(self):
        return self.progress

    def get_avg_p(self):
        return sum(self.progress) / len(self.progress)

def sort_by_name(arr: list) -> list[str]:
    values = {'A': 0, 'K': 1, 'M': 2, 'N': 3, 'P': 4, 'S': 5, 'V': 6}
    length = len(arr) - 1 #len(arr) - 2                Как лучше?
    for i in range(length - 1): #length
        for j in range(0, length - 1): #length
            a = arr[j].get_name()[0]
            b = arr[j + 1].get_name()[0]
            if values[a] > values[b]: arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sort_by_progress(arr: list) -> list[str]:
    length = len(arr) - 1
    for i in range(length):
        ind_of_min = i
        for j in range(i + 1, length):
            a = arr[j].get_avg_p()
            b = arr[ind_of_min].get_avg_p()
            if a < b: ind_of_min = j
        arr[i], arr[ind_of_min] = arr[ind_of_min], arr[i]
    return arr

def print_losers(arr) -> None:
    arr = sort_by_progress(arr)
    print('This is worth students:')
    for i in range(5):
        print(arr[i])
    print()

def print_list_cl(arr: list) -> None:
    for i in arr:
        print(f'{i.get_name()} - {i.get_avg_p()}', end = ', ')
    print()

students = []
n = 10
names = ['Vasya', 'Kolya', 'Petya', 'Sasha', 'Masha', 'Kirill', 'Artem', 'Nikita']
groups = ['YuBOZ-', 'YuBOZU-', 'ZhUR-', 'EVM-', 'AES-']
for i in range(n):
    progress = []
    diligence = r(0,2) #предопределённая успеваемость, а то псевдорандом их всех троечниками да хорошистами сделает.
    for j in range(n):
        if diligence == 2: progress.append(r(2,5))
        elif diligence == 1: progress.append(r(3,5))
        else: progress.append(r(4,5))
    students.append(Student(ch(names), ch(groups)+str(r(1,22)), progress))

print_list_cl(students)
print_losers(students)
students = sort_by_name(students)
print_list_cl(students)