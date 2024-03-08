"""
classes in python
"""


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in [
            "Gryffindor",
            "Ravenclaw",
            "Slytherine",
            "Hufflepuff",
        ]:
            raise ValueError("Invalid house")
        self._house = house

    def __str__(self) -> str:
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("What's your name?")
    house = input("What's your house?")
    student = Student(name, house)

    return student


if __name__ == "__main__":
    main()
