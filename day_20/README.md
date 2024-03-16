# Day 20

#### Saturday, 16-3-2024

Going through [ Python series by socratis]('https://www.youtube.com/watch?v=iAzShkKzpJo&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=3')

## concepts covered

1. builtin object

   - a file in python has access to builtin objects like `print`, `input` and so on. we can check them by

   ```python
   dir() # this shows a list of modules available to our file
   dir(__builtin__) # this accesses all the objects available to us

   help(print) # use help to learn about the builtin objects
   ```

2. builtin modules

   - we can also access builtin modules.
   - To use the object within builtin modules you have to import it.

   ```python
   help('modules') # this will display all the builtin modules

   import math # imports the math module
   dir() # this shows a list of modules available, use this to confirm
   ```

3. booleans
   - python uses `True` and `False` as booleans
