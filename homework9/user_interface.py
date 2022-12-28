from tqdm import tqdm as tq

def user_print(text: str) -> None:
    print(text)

def user_print_result(arr: list):
    for i in arr:
        print(i, end = '\n\n')

def user_enter_str(txt: str) -> str:
    return input(txt)

def user_enter_int(txt:str) -> int:
    return int(input(txt))