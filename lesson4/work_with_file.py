from datetime import datetime as dt

def create_file(name):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    data = open(name, 'w')
    data.write(f'This file create at {time}.\n\n')
    data.close()

def add_to_file(name, add_data, end = False):
    data = open(name, 'a')
    if end: data.write(f'{add_data} \n\n')
    else: data.write(f'{add_data} ')
    data.close()

def end_of_file(name):
    time = dt.now().strftime('%d.%m.%Y %H:%M')
    data = open(name, 'a')
    data.write(f'This file was end at {time}.')
    data.close()