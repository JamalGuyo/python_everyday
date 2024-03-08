"""
classes in python
"""


class Student: 
    ...


def main():
    student = get_student()
    print(f"{student.name} is in {student.house}")


def get_student():
    student = Student()
    student.name = input("What's your name?")
    student.house = input("What's your house?")

    return student


if __name__ == "__main__":
    main()
