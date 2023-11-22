# Ops Challenge: Directory Creation

## Overview

Functions are an essential concept in programming because they allow you to organize and modularize your code, making it more readable, maintainable, and easier to debug. Today, you will be creating a Python script that utilizes a function from the `os` library to generate directory information.

## Functions in Python

In Python, a function is a reusable block of code that performs a specific task or set of tasks. Python provides built-in functions like `print()` and `len()`, but you can also create your own custom functions to perform specific tasks.

**Defining a Function**

  To create a function, you use the `def` keyword, followed by the function's name, parentheses, and a colon. The function's name should follow the same naming rules as variable names. Because functions are actions, they should be named using a verb.

  ```python
  def my_function():
    # Function code goes here
  ```

**Function Parameters (Arguments)**\

  Functions can accept zero or more input values called parameters or arguments. Parameters are defined within the parentheses and allow you to pass data into the function. An argument is the value that is passed to the function to fulfill the parameter when it is invoked.

  ```python
  def greet(name):
    print(f"Hello, {name}!")
  ```

**Function Body**

  The function body contains the code that defines what the function does. It's indented and typically includes one or more statements.

  ```python
  def add(a, b):
    result = a + b
    return result
  ```

**Function Invocation (Calling a Function)**

  To use a function, you "call" it by using its name followed by parentheses. You can pass arguments to the function when you call it.

  ```python
  result = add(3, 5)
  ```

**Return Statement**

  Functions can return values using the `return` statement. This statement exits the function and returns a value to the caller.

  ```python
  def multiply(a, b):
    return a * b
  ```

  In Python, functions do not automatically return a value. If you don't explicitly use the `return` statement within a function, it will implicitly return `None`. `None` is a special Python value that represents the absence of a value or a null data type.

**Function Documentation (Docstrings)**

  You can add a docstring, a string enclosed in triple quotes, at the beginning of a function to provide information about its purpose and usage.

  ```python
  def my_function():
    """
    This is a sample function with a docstring.
    It does nothing.
    """
    pass
  ```

**Function Scope**

  Variables defined inside a function are usually local to that function and cannot be accessed from outside. Global variables can be accessed both inside and outside functions.

**Default Arguments**

  You can provide default values for function parameters, allowing the caller to omit those arguments if desired.

  ```python
  def greet(name="User"):
    print(f"Hello, {name}!")
  ```

**Keyword Arguments**

  When calling a function, you can specify arguments by name, which can be especially useful when a function has many parameters.

  ```python
  greet(name="Alice")
  ```

**Lambda Functions (Anonymous Functions)**

  Python also supports lambda functions, which are small, anonymous functions defined using the `lambda` keyword. They are often used for simple operations.

  ```python
  double = lambda x: x * 2
  ```

## Scripts, Modules, Packages, and Libraries in Python

In Python, the terms "scripts," "modules," "packages," and "libraries" refer to different components of code organization. Each serves a distinct purpose in structuring and managing Python code.

**Scripts:**
  - Scripts are typically small, standalone programs designed to perform a specific task or solve a particular problem.
  - They are usually executed from the command line or by running the script file directly.
  - Scripts often contain the main program logic and are meant to be run as the entry point of an application.
  - Python scripts typically have the `.py` file extension.

  Example:
  ```python
  # my_script.py
  def main():
      print("Hello, world!")

  if __name__ == "__main__":
      main()
  ```

**Modules:**
  - Modules are Python files containing functions, classes, and variables that can be reused in other Python scripts or modules.
  - They help organize code into smaller, manageable files by grouping related functionality together.
  - Modules are imported using the `import` statement in other Python scripts or modules.
  - Python modules also have the `.py` file extension.

  Example:
  ```python
  # my_module.py
  def greet(name):
      return f"Hello, {name}!"
  ```

**Packages:**
  - Packages are a way to organize related modules into a directory hierarchy, creating a namespace for Python code.
  - A package is a directory that contains an `__init__.py` file (which can be empty) and one or more module files. These module files can themselves be sub-packages.
  - Packages and their modules are imported using dot notation.
  - Packages do not have a specific file extension; they are represented as directories.

  Example:
  ```
  my_package/
  ├── __init__.py
  ├── module1.py
  ├── module2.py
  └── sub_package/
      ├── __init__.py
      ├── submodule1.py
      └── submodule2.py
  ```

**Libraries:**
  - The term "library" is often used interchangeably with "package" or "module." It refers to collections of reusable code and functionality.
  - Libraries can encompass a wide range of Python code, including packages, modules, and scripts. They serve as a way to provide pre-written code for specific tasks or domains.
  - Developers can use libraries to access pre-existing solutions for common problems, which can significantly speed up development.

  Example:
  - The Python Standard Library is a collection of built-in libraries and modules that provide a wide range of functionality for various tasks, such as file handling (`os`, `io`), math operations (`math`), and working with data structures (`collections`).

## Tuples in Python

In Python, a tuple is an ordered, immutable collection of elements. Tuples are very similar to lists, but with one crucial difference: once you create a tuple, you cannot modify its contents, it's said to be "immutable". This immutability makes tuples useful for situations where you want to ensure that the data remains constant throughout the program's execution.

**Syntax**

  - Tuples are defined using parentheses `()` or the `tuple()` constructor.
  - Elements within a tuple are separated by commas.

  ```python
  my_tuple = (1, 2, 3)
  another_tuple = tuple(("apple", "banana", "cherry"))
  ```

**Ordered**

  - Like lists, tuples are ordered collections, meaning that the order of elements is preserved.
  - You can access tuple elements using indexing, starting from 0 for the first element.

  ```python
  my_tuple = (1, 2, 3)
  print(my_tuple[0])  # Output: 1
  ```

**Immutable**

  - Tuples are immutable, which means you cannot change, add, or remove elements once a tuple is created.
  - You cannot use methods like `append()`, `insert()`, or `remove()` on tuples.

**Heterogeneous**

  - Tuples can contain elements of different data types, including numbers, strings, lists, other tuples, etc.

  ```python
  mixed_tuple = (1, "apple", [2, 3], ("a", "b"))
  ```

**Length and Membership**

  - You can find the length of a tuple using the `len()` function.
  - You can check if an element exists in a tuple using the `in` keyword.

  ```python
  my_tuple = (1, 2, 3)
  print(len(my_tuple))  # Output: 3
  print(2 in my_tuple)  # Output: True
  ```

**Tuple Packing and Unpacking**

  - You can create a tuple by simply separating values with commas, without parentheses. This is called tuple packing.
  - You can also assign the elements of a tuple to variables, which is known as tuple unpacking.

  ```python
  # Tuple packing
  my_tuple = 1, 2, 3

  # Tuple unpacking
  a, b, c = my_tuple
  ```

**Iterating Over Tuples**

  - You can iterate through the elements of a tuple using loops, such as `for`.

  ```python
  my_tuple = (1, 2, 3)
  for element in my_tuple:
    print(element)
  ```

## Resources

- [Python Functions](https://www.learnpython.org/en/Functions){:target="blank"}
- [`os.walk()` Documentation](https://docs.python.org/3/library/os.html){:target="blank"}
- [Tuple Objects in Python](https://docs.python.org/3/c-api/tuple.html){:target="blank"}
- [Real Python: Scripts, Modules, Packages, and Libraries](https://realpython.com/lessons/scripts-modules-packages-and-libraries/){:target="blank"}

## Demonstration

Refer to [DEMO.md](DEMO.md)
