import requests
from bs4 import BeautifulSoup as BS

url = 'https://rp5.ru/Погода_в_Иркутске'
class_ = 'ArchiveTemp'

r = requests.get(url)
html = BS(r.text, 'html.parser')
t = html.find(class_=class_).find(class_='t_0').text

print(t)