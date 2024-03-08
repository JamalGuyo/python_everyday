"""
using @classmethod
"""

import random


class hat:
    houses = ["Gryffindor", "Slytherine", "Ravenclaw", "Hufflepuff"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


hat.sort("Jamal")
