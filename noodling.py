
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
