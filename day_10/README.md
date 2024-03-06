# Day 10

#### Wednesday, 6-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. File I/O

   - we can persist data into files using pythons file i/o

   ```python
   name = input("What's your name?")
   file = open("names.txt", "a")
   file.write("f{name}\n")
   file.close()
   ```

   - with can shorten the code and also delegate closing of file by using the _with_ statement instead

   ```python
   with open("names.txt", "a") as file:
        file.write("f{name}\n")
   ```
