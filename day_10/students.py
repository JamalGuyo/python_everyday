"""
FIle I/O from csv files
"""

import csv

students = []

with open("students.csv") as file:
    # for line in file:
    #     name, house = line.rstrip().split(",")
    #     student = {"name": name, "house": house}
    #     students.append(student)
    #     print(f"{name} is in {house}")
    reader = csv.reader(file)
    for name, house in reader:
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
