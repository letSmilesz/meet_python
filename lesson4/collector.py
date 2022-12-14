import data_base as db
import user_interface as ui
import work_with_file as file
from os import path as chkf
from random import randint

def create():
    count = ui.user_enter_int('Enter how many strings of data you need: ')
    name_file = ui.user_enter_str('Enter the name of file: ')
    file.create_file(name_file)
    for i in range(count):
        rand = randint(0,1)
        sex = ('m','f')[rand]
        name = db.get_name(sex)
        name += ' ' + db.get_surname(sex)
        file.add_to_file(name_file, name)
        country = db.get_country()
        country += ' ' + db.get_phone(country)
        file.add_to_file(name_file, country, True)
    return name_file

def change_file():
    path_file = ui.user_enter_str('Write the name of new work-file: ')
    res = 'Error'
    if chkf.exists(path_file): 
        if chkf.isfile(path_file): 
            name_file = path_file
            res = 'Succesfull'
    ui.print_to_user(res)

def find(name_file):
    request = input('Enter parameters of search(all/(where)name=Ivan,(!not necessary!what add)name-srnm):'
    + ' ').split(',')
    if request[0] == 'all': res = file.search_in_file(name_file)
    else: 
        value = request[0].split('=')
        if len(request) > 1:
            filter = request[1].split('-')
            res = file.search_in_file(name_file, value[1], value[0], filter)
        else: res = file.search_in_file(name_file, value[1], value[0])
    ui.print_to_user(res)

def add(name_file):
    string = ui.user_enter_str('Write whole string of data(name surname country phone) separated be space: ')
    file.add_to_file(name_file, string, True)

def change(name_file):
    line_to_change = int(input('What line you want change: '))
    parameters = ui.user_enter_str('Write parameters as "parameter=value"(may be several, separate by comma): ')
    res = file.change_file(name_file, line_to_change, parameters)
    ui.print_to_user(res)

def delete(name_file):
    line_to_delete = int(input('What line you want delete: '))
    res = file.delete_from_file(name_file, line_to_delete)
    ui.print_to_user(res)

def start():
    ui.print_full_readme()
    name_file = 'table.txt'
    while True:
        action = ui.user_enter_str('What you want to do? ')
        if action == '-h': ui.print_short_readme()
        elif action == '-H': ui.print_full_readme()
        elif action == '-close': break
        elif action == '-change': change_file()
        elif action == 'create': name_file = create()
        elif action == 'find': find(name_file)
        elif action == 'add': add(name_file)
        elif action == 'change': change(name_file)
        elif action == 'delete': delete(name_file)
    ui.print_to_user('\nThank you, for using this programm!')
        