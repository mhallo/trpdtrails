import requests
from bs4 import BeautifulSoup

URL = 'https://www.threeriversparks.org/page/trail-conditions-cross-country-skiing'
page = requests.get(URL)

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

# inner_block_children is a list of all of the contents within the parent paragraph
# god I hate parsing drupal websites
inner_block_children = drilldown.contents
# print(f"Number of items: {len(inner_block_children)}")
# print(inner_block_children)

# print("cleaning newline characters from list...")
# get rid of annoying newlines in the list
while '\n' in inner_block_children: inner_block_children.remove('\n')

# the actual 'stats' start after the 14th item in the list in this case I believe.  This is naive and will probably break, so we need to find a way to make sure we're always starting that the section that says
# 'Trail Condtitions'
# but for naive testing, 'Trail conditions' begins at the 7th index, so everything onward is our parks and trails
for i in range(8, len(inner_block_children)):
    print(inner_block_children[i])
