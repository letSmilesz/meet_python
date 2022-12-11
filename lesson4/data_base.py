from random import randint, choice

male_names = ['Mike', 'Nick', 'Phillip', 'Alexander', 'Dmitriy', 'Ivan', 'Bob', 'Daniel']
female_names = ['Sara', 'Liza', 'Chloe', 'Sally', 'Marina', 'Ella', 'Linda', 'Peneloppa', 'Beatrisss']
male_surnames = ['Lihachev', 'Ivanov', 'Sidorov', 'Petrov', 'Espinosa', 'Decker', 'Danilov']
female_surnames = ['Petrova', 'Sidorova', 'Decker', 'Martin', 'Lopez', 'Richards', 'Ivanova']
countries = ['USA', 'Germany', 'Britain', 'Russia', 'Brazil', 'UAE']
code_of_country = {'USA': ('+1 840 ', 7) , 'Germany': ('+49 ', 10), 'Britain': ('+44 ', 8), 'Russia': ('+7 ', \
    10), 'Brazil': ('+55 ', 10), 'UAE': ('+971 ', 8)}

def get_name(sex = 'm'):
    if sex == 'm': arr = male_names
    else: arr = female_names
    return arr[randint(0, len(arr) - 1)]

def get_surname(sex = 'm'):
    if sex == 'm': arr = male_surnames
    else: arr = female_surnames
    return arr[randint(0, len(arr) - 1)]

def get_country():
    return choice(countries)

def get_phone(country):
    code, count = code_of_country[country]
    for i in range(count):
        code += str(randint(0, 9))
    return code
