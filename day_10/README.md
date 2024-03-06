# Day 10

#### Wednesday, 6-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. File I/O

   - we can persist data into files using pythons file i/o
   - `a` will append to file, `w` will write to file, `r` will read from file

   ```python
   name = input("What's your name?")
   file = open("names.txt", "a")
   file.write("f{name}\n")
   file.close()
   ```

   - with can shorten the code and also delegate closing of file by using the _with_ keyword instead

   ```python
   with open("names.txt", "a") as file:
        file.write("f{name}\n")
   ```

   - we can read from files as well as follows

   ```python
   with open("names.txt", "r") as file:
       lines = file.readlines()

   for line in lines:
       print("Hello,",line.rstrip())

    # we can shorten the code above to
    with open("names.txt", "r") as file:
        for line in files:
            print("Hello,", line.rstrip())
   ```

   - we can read from csv files as follows

   ```python
   with open("students.txt") as file:
       for line in file:
           name, house = line.rstrip().split(",")
           print(name, house)
   ```
