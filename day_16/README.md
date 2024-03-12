# Day 16

#### Tuesday, 12-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. docstrings

   - `pep-0257` standardizes how we write python documentation and semantics.

   ```python
   def meow(n:int) -> str:
    """
    Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raise TypeError:
    :return: A string of n meows, one per line.
    :rtype: str
    """
    return "meow"*n
   ```

2. `argparse` to document argv arguments

   ```python
   import argparse

   parser = argparse.ArgumentParser("Meow like a cat")
   parser.add_argument("-n", default=1, type=int, help="Number of times to meow")
   args = parser.parse_args()

   for _ in range(args.n):
       print("meow")
   ```
