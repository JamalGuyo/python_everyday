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
