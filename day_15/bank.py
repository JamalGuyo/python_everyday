"""
global vs local variables
"""

balance = 0


def main():
    """main function"""
    print("Balance", balance)
    deposit(100)
    withdraw(50)
    print("Balance", balance)


def deposit(n):
    """deposit to bank"""
    global balance
    balance += n


def withdraw(n):
    """withdraw from bank"""
    global balance
    balance -= n


if __name__ == "__main__":
    main()
