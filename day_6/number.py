"""
Exceptions in python
"""

try:
    x = int(input("what's x?"))
except ValueError:
    print("x is not an integer")
else:
    print(x)
