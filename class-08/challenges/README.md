# Ops Challenge: Python Collections

## Overview

Python is known for its relevance to data science and consequently handles data quite well using collections (arrays). Today, you will be creating lists, tuples, sets and dictionaries.

## Lists

In Python, a list is a built-in data structure used to store a collection of items. Lists are ordered, mutable (modifiable), and can contain elements of different data types, including numbers, strings, and even other lists. Lists are defined using square brackets `[ ]` and can hold zero or more items separated by commas.

**Creating Lists**

  You can create a list by enclosing items in square brackets and separating them with commas. For example:

  ```python
  my_list = [1, 2, 3, 4, 5]
  empty_list = []
  ```

**Accessing Elements**

  List elements are accessed by their index, starting from 0 for the first element. You can use square brackets with the index to access an element. For example:

  ```python
  first_element = my_list[0]  # Retrieves the first element (1)
  ```

  You can also use negative indexing to access elements from the end of the list. `-1` refers to the last element, `-2` to the second-to-last, and so on.

**Slicing**

  You can extract a portion of a list using slicing. Slicing allows you to create a new list containing a subset of the elements from the original list. It is done by specifying a start index, an end index (exclusive), and an optional step value. For example:

  ```python
  sub_list = my_list[1:4]  # Creates a new list with elements [2, 3, 4]
  ```

**Modifying Lists**

  Lists are mutable, which means you can change their contents. You can assign new values to specific elements or use various methods to modify the list, such as `append()`, `insert()`, `remove()`, and `pop()`. For example:

  ```python
  my_list[2] = 10  # Modifies the third element to be 10
  my_list.append(6)  # Adds 6 to the end of the list
  my_list.remove(4)  # Removes the first occurrence of 4 from the list
  ```

**List Operations**

  Lists support various operations, such as concatenation (using `+`), repetition (using `*`), and checking for membership (using `in`). For example:

  ```python
  list1 = [1, 2]
  list2 = [3, 4]
  combined_list = list1 + list2  # Concatenates lists: [1, 2, 3, 4]
  repeated_list = list1 * 3      # Repeats list: [1, 2, 1, 2, 1, 2]
  is_element_present = 2 in list1  # Checks if 2 is in the list (True)
  ```

**Length of a List**

  You can find the number of elements in a list using the `len()` function. For example:

  ```python
  length = len(my_list)  # Returns 5 for the 'my_list' defined earlier
  ```

**Iterating Over Lists**

  You can use loops, like `for`, to iterate over the elements of a list. For example:

  ```python
  for item in my_list:
    print(item)
  ```

## Sets

In Python, a set is a built-in data type used to store a collection of unique and unordered elements. Unlike lists or tuples, sets do not allow duplicate values, and they are not indexed. Sets are defined using curly braces `{ }` or the `set()` constructor function.

**Creating Sets**

  You can create a set by enclosing unique elements within curly braces or by using the `set()` constructor. For example:

  ```python
  my_set = {1, 2, 3, 4, 5}
  empty_set = set()
  ```

  Note that if you want to create an empty set using curly braces, you would think that you could do `empty_set = {}`. However, this will create an empty dictionary, not an empty set. To create an empty set you have to use `set()`.

**Adding and Removing Elements**

  Sets are mutable, which means you can add and remove elements after creation. To add an element, use the `add()` method, and to remove an element, use the `remove()` method. For example:

  ```python
  my_set.add(6)     # Adds 6 to the set
  my_set.remove(3)  # Removes 3 from the set
  ```

  If you're uncertain whether an element exists in the set before removing it, you can use the `discard()` method. It won't raise an error if the element is not present.

**Set Operations**

  Sets support various set operations such as union, intersection, difference, and symmetric difference. These operations are useful for comparing and combining sets.

  - **Union (`|`):** Combines two sets and returns a new set with all unique elements from both sets.

  ```python
  set1 = {1, 2, 3}
  set2 = {3, 4, 5}
  union_set = set1 | set2  # Results in {1, 2, 3, 4, 5}
  ```

  - **Intersection (`&`):** Returns a new set containing elements that exist in both sets.

  ```python
  intersection_set = set1 & set2  # Results in {3}
  ```

  - **Difference (`-`):** Returns a new set containing elements from the first set that are not in the second set.

  ```python
  difference_set = set1 - set2  # Results in {1, 2}
  ```

  - **Symmetric Difference (`^`):** Returns a new set containing elements that are unique to each set.

  ```python
  symmetric_difference_set = set1 ^ set2  # Results in {1, 2, 4, 5}
  ```

**Set Membership and Size**

  You can check if an element is a member of a set using the `in` operator. To find the number of elements in a set, use the `len()` function.

  ```python
  is_member = 2 in my_set  # Checks if 2 is in the set (True)
  set_size = len(my_set)   # Returns the number of elements in the set
  ```

**Iterating Over Sets**

  You can use loops, like `for`, to iterate over the elements of a set. However, since sets are unordered, the order of elements during iteration is not guaranteed.

  ```python
  for item in my_set:
    print(item)
  ```

Sets are particularly useful when you need to work with unique elements and perform operations like set intersections and unions.

## Dictionaries

In Python, a dictionary is a built-in data structure used to store collections of key-value pairs. Dictionaries are also sometimes referred to as "dicts." They are unordered, mutable, and are designed for efficient retrieval of values based on their associated keys. Dictionaries are defined using curly braces `{ }` and consist of one or more key-value pairs separated by colons `:`.

**Creating Dictionaries**

  You can create a dictionary by enclosing key-value pairs within curly braces or by using the `dict()` constructor function. Each key-value pair consists of a key followed by a colon `:` and a corresponding value. For example:

  ```python
  my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
  empty_dict = {}
  ```

**Accessing Values**

  You can access the values in a dictionary by specifying the key inside square brackets `[]` or by using the `get()` method. For example:

  ```python
  name = my_dict['name']  # Retrieves the value associated with the 'name' key ('John')
  age = my_dict.get('age')  # Retrieves the value associated with the 'age' key (30)
  ```

  If the key doesn't exist in the dictionary, using square brackets to access it will raise a `KeyError` exception, whereas `get()` will return `None` (or a default value you can specify) without raising an error.

**Modifying Dictionaries**

  Dictionaries are mutable, so you can add, modify, or remove key-value pairs after creation. To add a new key-value pair, simply assign a value to a new key. To modify an existing value, access it using its key and assign a new value. To remove a key-value pair, use the `pop()` method or the `del` statement. For example:

  ```python
  my_dict['job'] = 'Engineer'  # Adds a new key-value pair
  my_dict['age'] = 31  # Modifies the value associated with the 'age' key
  my_dict.pop('city')  # Removes the 'city' key and its associated value
  ```

**Dictionary Methods**

  Dictionaries offer various methods for performing operations such as getting all keys, values, or items (key-value pairs), checking for key existence, and more. Common methods include `keys()`, `values()`, `items()`, `pop()`, and `clear()`, among others.

  ```python
  keys = my_dict.keys()      # Returns a list of all keys
  values = my_dict.values()  # Returns a list of all values
  items = my_dict.items()    # Returns a list of all key-value pairs
  ```

**Checking for Key Existence**

  You can use the `in` operator to check if a key exists in a dictionary.

  ```python
  if 'name' in my_dict:
    print("Name:", my_dict['name'])
  ```

**Iterating Over Dictionaries**

  You can loop through dictionaries using a `for` loop to iterate over keys or key-value pairs.

  ```python
  for key in my_dict:
    print(key, my_dict[key])

  for key, value in my_dict.items():
    print(key, value)
  ```

Dictionaries are widely used in Python for tasks that involve mapping keys to values. They provide fast and efficient access to values based on their keys, making them suitable for various applications, including storing configurations, organizing data, and representing data records.

## Resources

- [Python Lists](https://docs.python.org/3/tutorial/datastructures.html)

## Demonstration

Refer to [DEMO.md](DEMO.md)
