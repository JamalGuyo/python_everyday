# Day 1

#### Monday, 26-2-2024

Starting out with [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. Functions, arguments, and side effects

   - A function is a block of code that is executed as a group
   - A function takes arguments and may have a side effect returns a user name from the input  
     e.g `name = input('What's your name?')`

2. Comments

   - Note to yourself in your code (pseudocode)
   - The interpretor will ignore the commented texts
   - You can comment using the following syntax:
     - `#single line comments`
     - python doesn't support multiline comments. you can use the single line comment on multiple lines
   - python also has `"""docstrings"""` for documenting your code.
   - you can access the docstrings using `__doc__`

3. print function

   - takes variable comma separated values
   - by default the the arguments are separated by a single space. You can change the separator as follows: `print('This', 'is', 'python', sep="-")`
   - the `sep` keyword takes a custom separator
   - The print function also automatically ends the returned values in a new line. We can also change this by doing: `print('This', 'is', 'python', sep="-", end="")`
   - the `end` keyword takes a custom ending
   - Python has a readable way to print called _fStrings_. `print(f'Hello, {name}')`

4. Parameters
   - These are what we pass to functions
   - We have two types of parameters:
     - Positional parameters - These are the strings we passed to the print function above
     - Named parameters - These are optional parameters we passed to the print function above i.e **_end, sep_**
