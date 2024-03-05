def main():
    greeting = hello()
    print(greeting)


def hello(to="World"):
    return f"Hello, {to}"


if __name__ == "__main__":
    main()
