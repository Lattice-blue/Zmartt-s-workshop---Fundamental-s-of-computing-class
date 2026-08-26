#Medium difficulty
#So the rules are:
#Remove duplicate values
#no using of a set
#preserving the first occurence order.
#What is first occurence order?
#The first duplicate value must be the one kept.


random_items = [
    "laptop", "smartphone", "headphones", "backpack",
    "laptop", "coffee mug", "desk lamp", "notebook",
    "smartphone", "water bottle", "running shoes", "sunglasses",
    "backpack", "wrist watch", "notebook", "charging cable"
]

# How do I do this? I could try a for loop
# Loop through each element
#   for the current  

#What happens when I modify a list as I'm going through in a loop?

# test_list = [1,2,3,4,5,6]

# for elem in test_list:
#     if elem == 2:
#         test_list.pop(len(test_list) - 1)
#     print(elem)

# Output is 1 to 5

# So it doesn't break so the for loop probably looks at the list a new after every iteration
# So it doesn't just look up the length at the beginning and just use that length to iterate through
# the list

# Marry the night

# I could just do a index find first and then figure out a more hacky way to do it.

# wait does it have a built in find method

# Loop through each element:
    # For this element create a copy of the list exluding the element and left elements
    # look through the slice and find a duplicate
    # if a duplicate is found remove it
    # continue to the next element


