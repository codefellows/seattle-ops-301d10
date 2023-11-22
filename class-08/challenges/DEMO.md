# Ops Challenge - Python Collections

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```python
#!/usr/bin/env python3

# How to create and print a list

thislist = ["apple", "banana", "cherry"]
print(thislist)
# Output: ['apple', 'banana', 'cherry']

# How to print the first item only

thislist = ["apple", "banana", "cherry"]
print(thislist[0])
# Output: apple

# How to print the last item only by counting backwards

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# Output: cherry

# How to print a subsequence by slicing the original list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Output: ['cherry', 'orange', 'kiwi']

# How to print the beginning to a specific element number

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# Output: ['apple', 'banana', 'cherry', 'orange']

# How to print a slice of elements with a step value

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "grapes", "figs", "grapefruit"]
print(thislist[1:9:2])
# Output: ['banana', 'orange', 'melon', 'grapes']

# How to add an item to a list

thislist = ["apple", "banana", "cherry"]
thislist.append("peach")
print(thislist)
# Output: ['apple', 'banana', 'cherry', 'peach']

```
