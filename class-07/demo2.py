#!/usr/bin/env python3

# function stuff
#                 1    2
#                2      5
def add_numbers(num1=0, num2=0):
    # This function is expecting 2 parameters
    # num1
    # num2

#     # This will return the sum of num1 and num2
#     print('I am running')
#     return num1 + num2

# this calls the add_numbers function and passes 1 and 2 as arguments, then prints the result
# print(add_numbers(1, 2)) # -> 3

# this calls the add_numbers function and passes 2 and 5 as arguments, then prints the result
# print(add_numbers(2, 5)) # -> 7

# print(add_numbers(3, 8)) # -> 11

# add_numbers() # -> 0


# Tuple stuff
# this is a array / list
# list_stuff = ['thing1', 'thing2', 'thing3']
# new_tuple = tuple(list_stuff)
# print(list_stuff[1])
# list_stuff.append('thing4')
# print(list_stuff[3])

# tuple
# stuff = ("thing1", "thing2", "thing3")
# stuff.append('thing4')
# new_stuff = list(stuff)
# new_stuff.append('thing4')

# for item1, item2, item3 in (stuff,):
#     print(item1)
#     print(item2)
#     print(item3)
#     print("")


# for item in stuff:
#     print(item)

import os
stuff = ("thing1", "thing2", "thing3")

# for thing in stuff:
#     print(thing)

for (item1, item2, item3) in ((stuff,)):
    print(item1)
    print(item2)
    print(item3)
    print("")

for (root, dirs, files) in os.walk("testdir"):
    ### Add a print command here to print ==root==
    print(root)
    ### Add a print command here to print ==dirs==
    print(dirs)
    ### Add a print command here to print ==files==
    print(files)
