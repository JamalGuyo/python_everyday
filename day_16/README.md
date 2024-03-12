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
    print('meow')
   ```
