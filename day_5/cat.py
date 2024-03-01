"""
loops in python
"""

# for loops in python
for _ in range(3):
    print("meow")


# loop a string by multiplying
print("meow\n" * 3, end="")

# loop though user defined number of times
while True:
    n = int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("meowing")

# loop through a list and also get their indexes
students = ["Hermione", "Ron", "Draco", "Harry"]
for i in range(len(students)):
    print(i + 1, students[i])

for i, student in enumerate(students):
    print(i, student)
