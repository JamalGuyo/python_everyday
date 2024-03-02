# Day 6

#### Saturday, 2-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. syntax errors
   - This are errors you are supposed to fix
   ```python
    print("unclosed quote)
   ```
2. Runtime errors and exceptions

   - This are errors that occur after successfully running your code.

   ```python
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        print(x)

   ```

3. pass keyword
   ```python
    while True:
        try:
            x = int(input("What's x?"))
            break
        except ValueError:
            pass
    print(x)
   ```
