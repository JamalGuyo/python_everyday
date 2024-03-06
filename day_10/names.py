"""
File I/O
"""

# name = input("What's your name?")

# with open("name.txt", "a") as file:
# file.write(f"{name} \n")


with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.rstrip())
