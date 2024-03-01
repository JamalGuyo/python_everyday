"""
looping through dictionaries in python
"""

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Syltherine",
}

# by default looping thro' dictionaries outputs the keys
for student in students:
    print(student, students[student], sep=",")

print("================================================")

students2 = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Draco", "house": "Syltherine", "patronus": None},
]

for student in students2:
    print(student["name"], sep=",")
