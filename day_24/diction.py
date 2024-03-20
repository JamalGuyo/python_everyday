"""
    dictionaries in pytc zon
"""

person = dict(name="Jamal")

try:
    person["surname"] = "John"
    print(person["lastname"])
except KeyError:
    print("key does not exist")

for key, value in person.items():
    print(key, value)

print(person)
