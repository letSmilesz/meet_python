def user_enter_int(string):
    return int(input(string))

def user_enter_str(string):
    return input(string)

def print_to_user(data):
    print(data)

def print_full_readme():
    print('Hello! This is prototype of database. If you run it for the first time you must create file.'
    + '\n\nTo create file enter "create", then enter number of rows in the database.'
    + '\n\nTo print all database(you may open it in File Explorer) enter "find","all"'
    + '\n\nTo filter database enter what are you searching and where(ex. "find","cntr=usa,name-srnm-phon")'
    + '\n\nTo add something to database enter what you want add(ex. "add","(value)"'
    + '\n\nTo change some line enter "change" and what string you want change(ex. '
    + '\n\n"change","number of line(1,2,3...)"). After then either what you want change and value(ex. '
    + '"name=Kolya,srnm=Ivanov")\n\nTo delete some line enter "delete","number of line(1,2,3,4...)"'
    + 'To call this text enter "-H", to short version enter "-h". '
    + '\n\nTo change work file enter "-change","name of file". !If it isn`t in the folder with the programm, '
    + 'specify the full path\n\nTo exit enter "-close"\n')
    input('To continue press "Enter"')


def print_short_readme():
    print('"-H" - print full readme, "-h" - print short readme, "-close" - to exit, "-change" to change work-'
    + 'file name\n\nCommands of first level: "create", "find", "add", "change", "delete"\n\n "find" - find/'
    + '"all" or where(in name, in surname, in country, in phone)=request(what you want find), also may be '
    + '"what to add"(name, surname, country, phone) - these parameters been in table.\n\n"add" - add/(whole '
    + 'string what you want to add\n\n"change" - change/number_of_line,parameter=new_value('
    + 'may be several)\n\n"delete" - delete/number_of_line'
    + '\n\nCommands to work with database: "name" - name, "srnm" - surname, "cntr" - country, "phon" - phone '
    + 'number\n\nAll commands you must enter in lowercase letters separated by commas and the value should '
    + 'be as written. Commands and values are separated by an equal sign\n\n\n')
    input('To continue press "Enter"')
