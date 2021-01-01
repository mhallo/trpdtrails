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
                list_length = len(tag_stripped_strings)
                content_len = list_length - 2
                # Content printer:
                for string in range(0, content_len):
                    print(f"Content: {tag_stripped_strings[string]}")

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
                print(f"Updated at: {tag_stripped_strings[update_index]}")


soup = BeautifulSoup(page.content, 'html.parser')
subsection = soup.find(id='block-threerivers-content')

# traildiv gets the specific block of html which houses the terminology definitions, as well as all of the trails.
traildiv =  soup.find("div", {"class": "userContent"})

# gets us out of the trail div and into the main content
trail_paragraph = soup.find('p')

extract_trail_conditions(trail_paragraph)

extract_update_times(trail_paragraph)

populate_park_list(trail_paragraph)
for park in parks:
    print(park)
