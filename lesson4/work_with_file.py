values_of_what = {'name': 0, 'srnm': 1, 'cntr': 2, 'phon': 3}

def create_file(name = 'table.txt'):
    with open(name, 'w') as data:
        data.write('')

def add_to_file(name, add_data, end = False):
    with open(name, 'a') as data:
        if end: data.write(f'{add_data} \n')
        else: data.write(f'{add_data} ')

def find_value(line, strng, value, where = 'name', what = 'full'):
    if strng.find(value) == -1: return ''
    ans = ''
    string = strng.split()
    if string[values_of_what[where]].find(value) != -1:
        if what == 'full': ans += f'{line}) {strng}'
        else:
            ans += f'{line}) '
            for i in what:
                ans += f'{string[values_of_what[i]]} '
            ans += '\n'
    return ans

def search_in_file(name, value = None, where = 'name',what = 'full'):
    ans = ''
    with open(name, 'r') as data:
        try:
            peoples = data.readlines()
            for line, i in enumerate(peoples):
                if value == None: ans += f'{line + 1}) {i}'
                else: ans += find_value(line + 1, i, value, where, what)                    
            if ans == '': ans += 'None'
        except IndexError: ans = 'Error. Enter correct request'
    return ans
print(search_in_file('table.txt', 'Sara', what=['name','srnm']))

def change_file(name, num_of_line, request):
    arr_requests = request.split(',')
    values, what = [], []
    for i in arr_requests:
        one_request = i.split('=')
        what.append(one_request[0])
        values.append(one_request[1])
    with open(name, 'r+') as file:
        new_file = ''
        for index, line in enumerate(file):
            try:
                if index == num_of_line - 1:
                    string = line.split()
                    for i, wh in enumerate(what):
                        string[values_of_what[wh]] = values[i]
                    res = ' '.join(string)
                    line = line.replace(line, res)
                    line += '\n'
                new_file += line
            except IndexError: return 'Error'
        else: 
            create_file(name)
            add_to_file(name, new_file)
            return 'Succesfull'
        
def delete_from_file(name, num_of_line):
    with open(name, 'r+') as file:
        res = ''
        try:
            for i, line in enumerate(file):
                if i < num_of_line - 1 or i >= num_of_line: res += line
                else: continue
            else: 
                create_file(name)
                add_to_file(name, res)
                return 'Succesfull'
        except IndexError: return 'Error'
