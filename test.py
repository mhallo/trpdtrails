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
# there are 3 <h2> header tags, the last one leading before all of the <h3> tags which represent all of the parks and their trail status'
traildiv =  soup.find("div", {"class": "userContent"})
# the basic structure for all of the parks and their respective trails is:
#       <h3><href></h3> which lists the name of the park itself, and has a relative link to the specific parks information
#       <p></p> tags which populate the information about the trails, and also their conditions.

# gets us out of the trail div and into the main content
drilldown = soup.find('p')
# h2s = drilldown.find_all('h2')
# parks stores all of the bs4 tags of the park
# h3s = drilldown.find_all('h3')
# go through the park tags in the parks
# for tag in h3s:
#     parks.append(cleanhtml(str(tag.contents[0])))
populate_park_list(drilldown)
for i in parks:
    print(i)

# print(h2s)
# print(parks)
# print(drilldown)
# print(f"{len(list(drilldown.children))}")
# print(list(drilldown.children))
# print(f"{len(list(drilldown.descendants))}")
# for child in drilldown.descendants:
#     print(child)
# inner_block_children is a list of all of the contents within the parent paragraph
# god I hate parsing drupal websites
# inner_block_children = drilldown.contents
# print(f"Number of items: {len(inner_block_children)}")
# print(inner_block_children)

# print("cleaning newline characters from list...")
# get rid of annoying newlines in the list
# while '\n' in inner_block_children: inner_block_children.remove('\n')

# allparks = soup.find_all('h3').getText()
# print(f"Here's all of the parks: {allparks}")
# the actual 'stats' start after the 14th item in the list in this case I believe.  This is naive and will probably break, so we need to find a way to make sure we're always starting that the section that says
# 'Trail Condtitions'
# but for naive testing, 'Trail conditions' begins at the 7th index, so everything onward is our parks and trails
# for i in range(8, len(inner_block_children)):
#     print(inner_block_children[i])
