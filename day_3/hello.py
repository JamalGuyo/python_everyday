"""
    - fstrings and format specifiers
    - functions in python
"""


def main():
    """main function running everything"""
    x = 12345.234234
    print(f"{x:,.2f}")
    name = "Jesus"
    hello(name)


def hello(to="world"):
    """says hello to Jesus or the world"""
    print("Hello", to)


main()
