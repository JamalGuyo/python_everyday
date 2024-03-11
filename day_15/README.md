# Day 15

#### Monday, 11-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. sets

   - this a list of unique items

   ```python
       students = [
           {"name": "Harry", "house": "Gryffindor"},
           {"name": "Ron", "house": "Gryffindor"},
           {"name": "Draco", "house": "Slytherine"},
           {"name": "Padma", "house": "Ravenclaw"},
       ]
       houses = set()
       for student in students:
           houses.add(student["house"])

       print(houses)
   ```

2. global variables

   - python allows you to read the global variables but not write to them in function scope.
   - To write the global variables you have to use the `global` keyword.

   ```python
   balance = 0

   def deposit(n):
       global balance
       balance += n
   ```

   - Using the `global` keyword is frowned upon. For such use cases its better to use classes instead

   ```python
   class Bank:
        def __init__(self):
            self._balance = 0

        @property
        def balance(self):
            return self._balance

        def deposit(self, n):
            self._balance += n
   ```
