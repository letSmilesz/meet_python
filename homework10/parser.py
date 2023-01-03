from bs4 import BeautifulSoup as bs
from requests import get

def get_soup (url: str) -> bs:
    html = get(url).text
    return bs(html, 'html.parser')


def parse(url: str) -> bs:
    soup = get_soup(url)
    res = soup.find('div', class_ = 'col-left col-left-margin').findAll(class_ = 'text')
    return res


def split_text(soup: bs) -> list:
    text = list(map(str, soup))
    text = ''.join(text)
    text_arr = text.split('</div>')
    return text_arr


def formatting_text(arr: list) -> list:
    for i, item in enumerate(arr):
        while item.count('<') > 0:
            left = item.find('<')
            right = item.find('>') + 1
            if item[left + 1] == 'b': item = item[:left] + '\n' + item[right:]
            else: item = item[:left] + item[right:]
        arr[i] = item
    return arr


def main(url):
    soup = parse(url)
    text = split_text(soup)
    return formatting_text(text)


if __name__ == '__main__':
    url = 'https://www.anekdot.ru/last/poems/'
    soup = parse(url)
    text = split_text(soup)
    result = formatting_text(text)
