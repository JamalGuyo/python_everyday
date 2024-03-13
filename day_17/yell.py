"""
map in python
"""


def main():
    students = [
        {"name": "Harry", "house": "Gryffindor"},
        {"name": "Ron", "house": "Gryffindor"},
        {"name": "Draco", "house": "Slytherine"},
    ]
    gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
    for g in gryffindors:
        print(g["name"])

    yell("This", "is", "cs50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
