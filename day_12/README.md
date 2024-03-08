# Day 12

#### Friday, 8-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. Classes in python

   - defining a class

   ```python
   class Student:
       # use the three dots or pass keyword as placeholders for future code
       ...
   ```

   - class instance attributes

   ```python
   class Student:
        def __init__(self, name, house):
            self.name = name
            self.house = house

    student = Student("Harry", "Gryffindor")
   ```

   - raise errors from a class

   ```python
   class Student:
        def __init__(self, name, house):
            if not name:
                raise ValueError("Missing name")
            if house not in ["Gryffindor", "Ravenclaw", "Slytherine", "Hufflepuff"]
                raise ValueError("Invalid house")
            self.name = name
            self.house = house

    student = Student("Harry", "Nairobi")
   ```

   - show string representation of class instance using `__str__` method

   ```python
   class Student:
       def __init__(self, name, house):
           if not name:
               raise ValueError("Missing name")
           if house not in ["Gryffindor", "Ravenclaw", "Slytherine", "Hufflepuff"]
               raise ValueError("Invalid house")
           self.name = name
           self.house = house

       def __str__(self):
           return f"{self.name} is in {self.house}"

   student = Student("Harry", "Nairobi")
   print(student) # will print the str method return string instead of the address of the instance object
   ```

   - using setters and getters

   ```python
   class Student:
        def __init__(self, name, house):
            self.name = name
            self.house = house

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            if not name:
                raise ValueError("Missing name")
            self._name = name

        @property
        def house(self):
            return self._house

        @house.setter
        def house(self, house):
            if house not in ["Gryffindor", "Ravenclaw", "Slytherine", "Hufflepuff"]
              raise ValueError("Invalid house")
            self._house = house

        def __str__(self):
             return f"{self.name} is in {self.house}"

   student = Student("Harry", "Nairobi")
   print(student)
   ```
