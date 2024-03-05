"""
unit testing in python
This module contains functions to be tested
"""


def main():
    """main function"""
    x = int(input("What's x?"))
    print(f"x squared is {square(x)}")


def square(n):
    """square function"""
    return n + n


if __name__ == "__main__":
    main()
