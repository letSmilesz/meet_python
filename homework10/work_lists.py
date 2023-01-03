from parser import main as pars


result_of_parse = []
showed = []
liked = []


def add_result(url):
    res = pars(url)
    if len(result_of_parse) > 0: result_of_parse.clear()
    for i in res:
        result_of_parse.append(i)
    

def next():
    if result_of_parse[0] not in showed: showed.append(result_of_parse[0])
    return result_of_parse.pop(0)


def previous():
    return showed[-2] if len(showed) > 1 else 'No joke was shone'


def like():
    liked.append(showed[-1])


def get_liked():
    return liked


