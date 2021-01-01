
# there are 3 <h2> header tags, the last one leading before all of the <h3> tags which represent all of the parks and their trail status'

# the basic structure for all of the parks and their respective trails is:
#       <h3><href></h3> which lists the name of the park itself, and has a relative link to the specific parks information
#       <p></p> tags which populate the information about the trails, and also their conditions.

# h2s = drilldown.find_all('h2')
# parks stores all of the bs4 tags of the park
# h3s = drilldown.find_all('h3')
# go through the park tags in the parks
# for tag in h3s:
#     parks.append(cleanhtml(str(tag.contents[0])))

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

# test_list = list(drilldown.children)
# for i in range(19, len(test_list)):
#     if test_list[i].name == "p":
#         # print(f"{i}: {test_list[i]}")
#         tag_stripped_strings = list(test_list[i].stripped_strings)
#         list_length = len(tag_stripped_strings)
#         content_len = list_length - 2
#         update_index = list_length - 1
#         # Content printer:
#         # for string in range(0, content_len):
#         #     print(f"Content: {tag_stripped_strings[string]}")
#         # Update Time printer:
#         print(f"Updated at: {tag_stripped_strings[update_index]}")
#         # for string in tag_stripped_strings:
#         #     print(string)

# for uhh in drilldown.children:
#     # each paragraph can be a list of contents
#     if uhh.name == "p":
#         # tell beautiful soup to get the non-html filled tags of the page
#         # for string in uhh.stripped_strings:
#         #     print(string)
#         # print('=====')
#         string_list = list(uhh.stripped_strings)
#         if 'Updated' in string_list:
#             print('yup buddy')
#         # for string in string_list:
#         #     print(string)
#         # print('xxxxx')
#         # length of the stripped string list, aka the information which tells us the contidion of each trails, and also any other notes TRPD provides
#         list_length = len(string_list)
#         # The update time information is the last two items in the stripped string list, all the rest is the content we want!
#         content_len = list_length - 2
#         update_index = list_length - 1
#         # print('NOW PRINTING UPDATE CONTENTS')
#         # for string in range(0, content_len):
#         #     print(string_list[string])
#         # print()
#         # print('NOW PRINTING WHEN STUFF WAS UPDATED')
#         update_time = string_list[update_index]
#         print("My result? " + update_time)

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
