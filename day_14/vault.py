"""
operator overloading
"""


class Vault:
    def __init__(self, money):
        self.money = money

    def __str__(self) -> str:
        return f"balance {self.money}"

    def __add__(self, other):
        total = self.money + other.money
        return Vault(total)


donation1 = Vault(100)
print(donation1)

donation2 = Vault(500)
print(donation2)

total = donation1 + donation2
print(total)
