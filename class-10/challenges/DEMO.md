# Ops Challenge - Python File Handling

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

> This demo uses the variable name "notebook" to demonstrate an analogy but students may see "file" or "f" used in online documentation to represent the same value. The choice of variable naming here is subjective and can vary based on personal preference, coding style guidelines, or the specific requirements of a project or organization.

```python
#!/usr/bin/env python3
# Script:                       Ops Challenge 10
# Author:                       Hexx King
# Date of latest revision:      05/22/23
# Purpose:                      File Handling in Python

import os

# Variable Declarations

# Create a new notebook (file) named "my_notebook.txt"
notebook_path = "my_notebook.txt"

# Main

# Open the notebook with write permissions and assign it to the "notebook" variable
with open(notebook_path, "w") as notebook:
  # Write some lines (data) to the notebook
  notebook.write("First line\n")
  notebook.write("Second line\n")
  notebook.write("Third line\n")

# Read the contents of the notebook
with open(notebook_path, "r") as notebook:
  # Read the first five characters of the file
  print("First 5 Characters: ", notebook.read(5))

  # Read and print each line of the notebook
  for line in notebook:
    print("Line:", line.strip())  # Remove the newline character
  # Why does this start the print() at "line" and not "First"?
  # The reader picks up at the last character it read
  # Try the code below instead

# Read and print each line of the notebook
# with open(notebook_path, "r") as notebook:
#   for line in notebook:
#     print("Line:", line.strip())  # Remove the newline character

# Append a new line (data) to the notebook
with open(notebook_path, "a") as notebook:
  notebook.write("Fourth line")

# Split the contents of the notebook by lines
with open(notebook_path, "r") as notebook:
  lines = notebook.read().split("\n")
  print("Split lines: ", lines)

# Close the notebook
notebook.close()

# Rename the notebook to "renamed_notebook.txt"
renamed_notebook_path = "renamed_notebook.txt"
os.rename(notebook_path, renamed_notebook_path)

# Remove the notebook (file)
os.remove(renamed_notebook_path)

# End

```
