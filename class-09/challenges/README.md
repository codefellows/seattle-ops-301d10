# Ops Challenge: Python Conditionals

## Overview

Conditionals are an important tool in any language and see plenty of use in Python. Today, you will be using "if statements" in Python.

## Booleans in Python

Booleans in Python represent one of two values: `True` or `False`. These Boolean values are primarily used for logical operations, comparisons, and making decisions in your code. Booleans are fundamental to programming because they help control the flow of a program by determining which code blocks should be executed based on conditions.

**True and False**

  - `True` and `False` are two built-in constant values in Python.
  - `True` represents a logical true condition, while `False` represents a logical false condition.
  - These values are case-sensitive, so you must use `True` and `False` with an uppercase initial letter.

**Boolean Expressions**

  - Boolean expressions are expressions that evaluate to either `True` or `False`.
  - They typically involve comparison operators, logical operators, or the result of other Boolean operations.

  Example:

  ```python
  x = 5
  y = 10
  is_greater = x > y  # is_greater will be False
  ```

**Boolean Variables and Assignments**

  - You can create Boolean variables and assign `True` or `False` values to them.

  Example:

  ```python
  is_sunny = True
  is_raining = False
  ```

**Boolean Functions and Methods**

  - Many functions and methods in Python return Boolean values.
  - For example, the `isalpha()` method on a string returns `True` if all characters in the string are alphabetic, and `False` otherwise.

  Example:

  ```python
  text = "Hello123"
  is_alpha = text.isalpha()  # is_alpha will be False
  ```

## Comparison Operators in Python

Comparison operators in Python are used to compare values and return Boolean results, either `True` or `False`, based on the relationship between the values being compared. These operators are fundamental for creating conditional statements and evaluating expressions. Here are the commonly used comparison operators in Python:

**Equality Operator (`==`)**

  - Checks if two values are equal.
  - Returns `True` if the values are equal, `False` otherwise.

  ```python
  x == y  # Returns True if x is equal to y
  ```

**Inequality Operator (`!=`)**

  - Checks if two values are not equal.
  - Returns `True` if the values are not equal, `False` otherwise.

  ```python
  x != y  # Returns True if x is not equal to y
  ```

**Greater Than Operator (`>`)**

  - Checks if the left operand is greater than the right operand.
  - Returns `True` if the left operand is greater, `False` otherwise.

  ```python
  x > y  # Returns True if x is greater than y
  ```

**Less Than Operator (`<`)**

  - Checks if the left operand is less than the right operand.
  - Returns `True` if the left operand is less, `False` otherwise.

  ```python
  x < y  # Returns True if x is less than y
  ```

**Greater Than or Equal To Operator (`>=`)**

  - Checks if the left operand is greater than or equal to the right operand.
  - Returns `True` if the left operand is greater than or equal to, `False` otherwise.

  ```python
  x >= y  # Returns True if x is greater than or equal to y
  ```

**Less Than or Equal To Operator (`<=`)**

  - Checks if the left operand is less than or equal to the right operand.
  - Returns `True` if the left operand is less than or equal to, `False` otherwise.

  ```python
  x <= y  # Returns True if x is less than or equal to y
  ```

These comparison operators can be used with various data types, including numbers (integers, floats), strings, and other objects that support comparison. When comparing non-numeric types, such as strings, the operators check the lexicographic order.

## Logical Operators in Python

Logical operators in Python are used to perform logical operations on Boolean values or expressions. These operators allow you to combine and manipulate Boolean values to make more complex decisions in your code. Python provides three primary logical operators: `and`, `or`, and `not`.

**`and` Operator**

  - The `and` operator returns `True` if both operands are `True`. Otherwise, it returns `False`.
  - It requires both conditions on either side of it to be true for the overall expression to be true.

  Example:

  ```python
  x = True
  y = False
  result = x and y  # result will be False
  ```

  In this example, since `y` is `False`, the result of `x and y` is `False`.

**`or` Operator**

  - The `or` operator returns `True` if at least one of the operands is `True`. It returns `False` only if both operands are `False`.
  - It requires only one condition on either side of it to be true for the overall expression to be true.

  Example:

  ```python
  x = True
  y = False
  result = x or y  # result will be True
  ```

  In this example, since `x` is `True`, the result of `x or y` is `True`.

**`not` Operator**

  - The `not` operator is a unary operator that negates (inverts) the value of a Boolean expression. If the expression is `True`, `not` makes it `False`, and if it's `False`, `not` makes it `True`.

  Example:

  ```python
  x = True
  result = not x  # result will be False
  ```

  In this example, `not x` inverts the value of `x`, making it `False`.

**Combining Logical Operators**

  - Logical operators can be combined to create more complex conditions. Parentheses can be used to control the order of operations, just like in arithmetic expressions.

  ```python
  x = True
  y = False
  z = True

  result = x and (y or z)  # result will be True

  # In this case, (y or z) evaluates to True because z is True, and x and True results in True.
  ```

Logical operators are essential for building conditional statements that depend on multiple conditions and for making decisions based on the combined evaluation of Boolean expressions.

## Conditionals in Python

In Python, conditionals are used to control the flow of a program based on certain conditions or boolean expressions. They allow you to make decisions in your code by executing different blocks of code depending on whether a condition is true or false.

**if statement**

The `if` statement is used to execute a block of code if a specified condition is true. If the condition is false, the code block is skipped.

  ```python
  if condition:
    # Code to execute if the condition is true
  ```

  Example:

  ```python
  x = 10
  if x > 5:
    print("x is greater than 5")
  ```

**if-else statement**

The `if-else` statement allows you to execute one block of code if a condition is true and another block if it is false.

  ```python
  if condition:
    # Code to execute if the condition is true
  else:
    # Code to execute if the condition is false
  ```

  Example:

  ```python
  age = 25
  if age >= 18:
    print("You are an adult")
  else:
    print("You are a minor")
  ```

**if-elif-else statement**

The `if-elif-else` statement allows you to check multiple conditions in a sequence and execute the code block associated with the first true condition. If none of the conditions are true, the code block in the `else` clause is executed.

  ```python
  if condition1:
      # Code to execute if condition1 is true
  elif condition2:
      # Code to execute if condition2 is true
  else:
      # Code to execute if no conditions are true
  ```

  Example:

  ```python
  score = 85
  if score >= 90:
    print("A")
  elif score >= 80:
    print("B")
  elif score >= 70:
    print("C")
  else:
    print("D")
  ```

**Nested conditionals**

You can also nest conditional statements within each other to create more complex logic.

  ```python
  if condition1:
    if condition2:
      # Code to execute if both condition1 and condition2 are true
    else:
      # Code to execute if condition1 is true but condition2 is false
  else:
    # Code to execute if condition1 is false
  ```

  Example:

  ```python
  x = 10
  y = 5
  if x > 5:
    if y > 3:
      print("Both conditions are true")
    else:
      print("First condition is true, second is false")
  else:
    print("First condition is false")
  ```

## Resources

- [Python Conditionals](https://realpython.com/python-conditional-statements/)
- [Python Docs: If Statements](https://docs.python.org/3/tutorial/controlflow.html)
- [Operators and Expressions in Python](https://realpython.com/python-operators-expressions/)

## Demonstration

Refer to [DEMO.md](DEMO.md)
