import requests

from bs4 import BeautifulSoup as b

URL = 'https://zaim.com/reestr-mfo/'
def parser(url):
    r = requests.get(URL)
    soup = b(r.text, 'html.parser')
    anekdots = soup.find_all('a', class_='zReestrItem_title nohref')# названия 
    return [c.text for c in anekdots]
    

list_of_jokes = parser(URL)
print(list_of_jokes)