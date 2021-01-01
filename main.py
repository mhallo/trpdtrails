import requests
import re
from bs4 import BeautifulSoup

URL = 'https://www.threeriversparks.org/page/trail-conditions-cross-country-skiing'
page = requests.get(URL)

# Stores the names of all of the parks.
parks = []
trail_status = []

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
drilldown_list = list(drilldown)
dll = len(drilldown_list)
# for i in range(0, len(drilldown_list)):
#     print(f"{i}: {drilldown_list[i]}: {type(drilldown_list[i])}")
# The bit we care about starts at the 15th bs4 element, and we'll be naive and this will likely have a potential to break in the future.
test = len(list(drilldown.children))
print(f"number of items in drilldown just as plain ol list {dll}")
print(f"number of items in children {test}")
for uhh in drilldown.children:
    # each paragraph can be a list of contents
    if uhh.name == "p":
        # tell beautiful soup to get the non-html filled tags of the page
        # for string in uhh.stripped_strings:
        #     print(string)
        # print('=====')
        string_list = list(uhh.stripped_strings)
        if 'Updated' in string_list:
            print('yup buddy')
        # for string in string_list:
        #     print(string)
        # print('xxxxx')
        # length of the stripped string list, aka the information which tells us the contidion of each trails, and also any other notes TRPD provides
        list_length = len(string_list)
        # The update time information is the last two items in the stripped string list, all the rest is the content we want!
        content_len = list_length - 2
        update_index = list_length - 1
        # print('NOW PRINTING UPDATE CONTENTS')
        # for string in range(0, content_len):
        #     print(string_list[string])
        # print()
        # print('NOW PRINTING WHEN STUFF WAS UPDATED')
        update_time = string_list[update_index]
        print("My result? " + update_time)

# populate_park_list(drilldown)
# for park in parks:
#     print(park)
