import requests
import re
import json
from bs4 import BeautifulSoup

URL = 'https://www.threeriversparks.org/page/trail-conditions-cross-country-skiing'
page = requests.get(URL)

# Stores the names of all of the parks.
park_list = []

# Stores the content for the updates
status_info = []

#Stores the update times
time_list = []

# aggregates all of the park info into a dictionary, to be converted to JSON
status_dict = {}

# Notes:
# Condition Definitions:
# Good, Firm pack and fresh tracks, no bare spots and track is firm
# Fair, Miminal bare spots, minimal icy spots
# Poor, Skiability is questionable: track/pack has deteriorated, some parts of trails may be closed, icy spots and bare spots are possible
# Closed, Lack of snow, dangerous ice, or maintenance work active
condition_list = ["good","fair","poor","closed"]
# Grooming Definitions:
# Packed, packed for skate skiing
# Tracked, tracks are set for classic skiing
# Groomed Trails are packed for skate skiing and tracked for classic skiing
# Ungroomed, not packed or tracked.  Go trailblaze
grooming_condition_list = ["packed","tracked","groomed","ungroomed"]

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

# self explanitory, populates the list of all of the parks.  Takes in a BeautifulSoup4 object that has it's scope to the 'three rivers park district content'
def populate_park_list(threerivers_content):
    print('populating park list...')
    h3s = threerivers_content.find_all('h3')
    for tag in h3s:
        park_list.append(cleanhtml(str(tag.contents[0])))

# extracts the trail condition content from the trail paragraph
# note: I decided to separate the content and time content from a shared method to allow for more specialized parsing for data storage in the future
def extract_trail_conditions(trail_paragraph):
    content_list = list(trail_paragraph.children)
    if len(content_list) != 0:
        print('extracting page contents...')
        # We start at the 19th position for the list of the trail paragraph as there is a blurb on the webpage that does not contain relevant content.
        # In the future, it would be better to dynamically find this in the event that the website maintainers end up manually changing the contents, therefore ruining how this works
        for i in range(19, len(content_list)):
            if content_list[i].name == "p":
                tag_stripped_strings = list(content_list[i].stripped_strings)
                # list_length = len(tag_stripped_strings)
                # content_len = list_length - 2
                # Content printer:
                # Need a way to clean this up, but put all of the content into one big string and then ship it out for the dictionary.
                content_string = " ".join(tag_stripped_strings)
                status_info.append(content_string)
                print(content_string)
                # for string in range(0, content_len):
                #     print(f"Content: {tag_stripped_strings[string]}")

# extracts the time at which the trail conditions were updated
def extract_update_times(trail_paragraph):
    content_list = list(trail_paragraph.children)
    if len(content_list) != 0:
        print('extracting update times...')
        # We start at the 19th position for the list of the trail paragraph as there is a blurb on the webpage that does not contain relevant content.
        # In the future, it would be better to dynamically find this in the event that the website maintainers end up manually changing the contents, therefore ruining how this works
        for i in range(19, len(content_list)):
            if content_list[i].name == "p":
                tag_stripped_strings = list(content_list[i].stripped_strings)
                list_length = len(tag_stripped_strings)
                update_index = list_length - 1
                # Update Time printer:
                time_list.append(tag_stripped_strings[update_index])
                print(f"Updated at: {tag_stripped_strings[update_index]}")


def extract_dirty(trail_paragraph):
    content_list = list(trail_paragraph.children)
    if len(content_list) != 0:
        print('extracting dirty contents...')
        # We start at the 19th position for the list of the trail paragraph as there is a blurb on the webpage that does not contain relevant content.
        # In the future, it would be better to dynamically find this in the event that the website maintainers end up manually changing the contents, therefore ruining how this works
        for i in range(19, len(content_list)):
            if content_list[i].name == "p":
                tag_stripped_strings = list(content_list[i].stripped_strings)
                list_length = len(tag_stripped_strings)
                content_len = list_length - 2
                # Content printer:
                for string in range(0, content_len):
                    print(f"Content:{string} {tag_stripped_strings[string]}")

# takes a string input, will check if any of the condtions are found within the condition table
def populate_conditions(content_string):
    string = content_string.lower()
    if any(x in string for x in condition_list):
        print(f"condition found: {string}")

def populate_JSON():
    print('constructing JSON...')

soup = BeautifulSoup(page.content, 'html.parser')
subsection = soup.find(id='block-threerivers-content')

# traildiv gets the specific block of html which houses the terminology definitions, as well as all of the trails.
traildiv =  soup.find("div", {"class": "userContent"})

# gets us out of the trail div and into the main content
trail_paragraph = soup.find('p')

extract_trail_conditions(trail_paragraph)

extract_update_times(trail_paragraph)

populate_park_list(trail_paragraph)
for park in park_list:
    print(park)
