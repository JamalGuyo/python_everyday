"""This is a docstring example
   you can access the docstring on __dict__
   This file contains examples of comments, and variables
"""

# this is a single line comment
# the single line comment can be used as a multiline

name = input("What's your name? ")
print("Hello", name)
print("Helo", name, sep="-")

print(__doc__)
