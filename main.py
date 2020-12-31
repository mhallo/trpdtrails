import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.threeriversparks.org/page/trail-conditions-cross-country-skiing'
page = requests.get(URL)

# Stores the names of all of the parks.
parks = []

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

# self explanitory, populates the list of all of the parks.  Takes in a BeautifulSoup4 object that has it's scope to the 'three rivers park district content'
def populate_park_list(threerivers_content):
    print('populating park list...')
    h3s = threerivers_content.find_all('h3')
    for tag in h3s:
        parks.append(cleanhtml(str(tag.contents[0])))


soup = BeautifulSoup(page.content, 'html.parser')
subsection = soup.find(id='block-threerivers-content')

# traildiv gets the specific block of html which houses the terminology definitions, as well as all of the trails.
traildiv =  soup.find("div", {"class": "userContent"})

# gets us out of the trail div and into the main content
drilldown = soup.find('p')

populate_park_list(drilldown)
for park in parks:
    print(park)
