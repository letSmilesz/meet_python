def user_enter():
    count = int(input('Enter, how many passwords you need: '))
    length = int(input('Enter, how long passwords must been: '))
    return (count, length)

def output_on_display(txt: str, arr: list):
    print(txt)
    for i in arr:
        print(i)