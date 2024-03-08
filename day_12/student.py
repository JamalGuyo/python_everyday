"""
classes in python
"""


def main():
    student = get_student()
    print(f"{student['name']} is in {student['house']}")


def get_student():
    name = input("What's your name?")
    house = input("What's your house?")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
