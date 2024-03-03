# Day 7

#### Sunday, 3-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. libraries
   - This are code written in Python by other people
   - Libraries are made possible with Modules. Module is just a library that typically has one or more functions or features built into it
2. built-in modules
   - to use some built-in modules, you have to import them into your code e.g random module
   ```python
       import random
       coin = random.choice(['Heads', 'Tails'])
       print(coin)
   ```
   - you can import functions from a module using _from_ keyword
   ```python
      from random import choice
      coin = choice(['Heads', 'Tails'])
      print(coin)
   ```
