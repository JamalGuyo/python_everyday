# Day 13

#### Saturday, 9-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. inheritance

   ```python
   class Wizard:
        def __init__(self, name):
            if not name:
                raise ValueError("misssing name")
            self.name = name

   class Student(Wizard):
       def __init__(self, name, house) -> None:
           super().__init__(name)
           self.house = house
   ```
