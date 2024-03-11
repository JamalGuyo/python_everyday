"""
sets in python
"""

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
