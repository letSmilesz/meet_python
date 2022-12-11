import data_base as db
import user_enter as ue
import work_with_file as file
from random import randint

def start():
    count = ue.user_enter()
    name_file = 'table.txt'
    file.create_file(name_file)
    lst_functions = [db.get_name, db.get_surname, db.get_country, db.get_phone]
    for i in range(count):
        rand = randint(0,1)
        sex = ('m','f')[rand]
        name = db.get_name(sex)
        name += ' ' + db.get_surname(sex)
        file.add_to_file(name_file, name)
        country = db.get_country()
        country += ' ' + db.get_phone(country)
        file.add_to_file(name_file, country, True)
    file.end_of_file(name_file)
        