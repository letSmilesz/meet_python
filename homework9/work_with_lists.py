from html_url_work import get_soup
def catch_links(arr: list):
    for i, item in enumerate(arr):
        left = item.find('/')
        right = item.find('#') + 2
        arr[i] = item[left:right]
    return arr

def convert_list_to_str(arr: list):
    return list(map(str, arr))

def delete_chars(arr: list, hrefs: list):
    j = 0
    for i, item in enumerate(arr):
        while item.count('>') > 0:
            left = item.find('<') + 1
            right = item.find('>') + 1
            if item[left] == 'a':
                href = 'https://anekdot.ru' + hrefs[j]
                item = f'The joke is too long. To see it go to {href}'
                j += 1
            elif item[left] == 'd' or item[left] == '/':
                item = item[:left - 1] + item[right:]
            elif item[left] == 'b':
                item = item[:left - 1] + '\n' + item[right:]
        arr[i] = item
    return arr

# soup = get_soup('https://anekdot.ru')
# res = soup.find('div', class_ = "texts").findAll(class_ = "text")
# hrefs = soup.find('div', class_ = "texts").findAll('a', class_ ='next')

def catch_jokes(soup: list, hrefs: list):
    hrefs = catch_links(convert_list_to_str(hrefs))
    soup = convert_list_to_str(soup)
    return delete_chars(soup, hrefs)

