"""
fibonacci in python
"""

from functools import lru_cache

# fibonacci_cache = {}
# def fibonacci(n):
#     # check if value is in fibonacci_cache
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#
#     # compute the nth term and save to fibonacci_cache
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 2
#     elif n > 2:
#         value = fibonacci(n - 1) + fibonacci(n - 2)
#
#     # cache
#     fibonacci_cache[n] = value
#     return value


@lru_cache(maxsize=1000)
def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 101):
    print(n, ":", fibonacci(n))
