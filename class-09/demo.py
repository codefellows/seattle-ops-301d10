#!/usr/bin/env python3

# Script: Logical Operators
# Author: Roger
# Date: 12/1/2020

child1 = 5
child2 = 8
child3 = 15
child4 = 28
child5 = 28
#      5  == 8
if child1 == child2:
  print('They are the same age!')
#      8    !=   15
elif child3 != child5:
  print('They are not the same age still!')
#      15 >= 15
elif child3 >= 16:
  print('The child is 15 years or older!')
elif child1 > 6 or child3 > 16:
  print('The children are getting older!')
elif child4 == child5 and child1 > child2:
  print('Alternating ages here!')
elif (child1 == child2 or child3 > child2) and (child4 == child5 and child4 < child3):
  print('waoh, this is blowing my mind')
else:
  print('They are different ages!')
