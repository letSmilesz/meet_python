from user_interface import user_print_result as usr
from user_interface import user_print as usp
from html_url_work import parse_anekdots as parser
from work_with_lists import catch_jokes

def main():
    usp('This is the parser of anekdots!')
    url = 'https://anekdot.ru'
    anekdots, hrefs = parser(url)
    result = catch_jokes(anekdots, hrefs)
    usr(result)
    
