"""
map in python
"""


def main():
    yell("This", "is", "cs50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
