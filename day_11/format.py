"""
formatting users data using regex
"""

import re

name = input("What's your name?").strip()
if matches := re.search(r"^(.+), (.+)$", name):
    fname, lname = matches.groups()
    name = f"{fname} {lname}"

print(name)
