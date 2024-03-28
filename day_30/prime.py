"""
prime numbers
"""


def is_prime(n):
    """returns prime numbers between 0 and n"""
    if n == 1:
        return False

    for d in range(2, n):
        if n % d == 0:
            return False

    return True


for n in range(1, 21):
    print(n, is_prime(n))
