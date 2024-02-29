"""
conditionals in python
"""

x = 0
y = 2

if x > y:
    print(f"{x} is greater than {y}")
if y < x:
    print(f"{y} is greater than {x}")
if x == y:
    print(f"{x} is equal to {y}")

if x > y:
    print(f"{x} is greater than {y}")
elif y < x:
    print(f"{y} is greater than {x}")
else:
    print(f"{x} is equal to {y}")


def main():
    """Main function"""
    name = input("What's your name?")
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherine")
        case _:
            print("who?")

    x = int(input("what's x?"))
    if is_even(x):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")


def is_even(n):
    """check if number is even"""
    # return True if n % 2 == 0 else False
    return n % 2 == 0


main()
