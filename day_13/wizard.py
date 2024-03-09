"""inheritance """


class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("misssing name")
        self.name = name


class Student(Wizard):
    def __init__(self, name, house) -> None:
        super().__init__(name)
        self.house = house
