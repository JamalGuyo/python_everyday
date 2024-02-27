"""
Day 2 of python everyday
 - string methods
 - int
"""

# ask user for their name
name = input("What's your name?").strip().title()

# split user's name into firstname and lastname
first, last = name.split(" ")

# say hello to user
print(f"hello, {first}")
