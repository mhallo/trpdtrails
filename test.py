import requests
from bs4 import BeautifulSoup

URL = 'https://www.threeriversparks.org/page/trail-conditions-cross-country-skiing'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
subsection = soup.find(id='block-threerivers-content')
print(subsection)
