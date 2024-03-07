# Day 11

#### Thursday, 7-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1.  Regular Expressions

    - python has a regex library called `re`

    ```python
    re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE)
    ```

    - the first aregument is the regular expression, the second argument is the string to check and the third argument is regular expression flags
