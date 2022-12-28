from bs4 import BeautifulSoup as bs
from requests import get

def get_soup(url: str):
    html = get(url).text
    return bs(html, 'html.parser')
    
def parse_anekdots(url: str):
    soup = get_soup(url)
    res = soup.find('div', class_ = "texts").findAll(class_ = "text")
    hrefs = soup.find('div', class_ = "texts").findAll('a', class_ ='next')
    return res, hrefs
