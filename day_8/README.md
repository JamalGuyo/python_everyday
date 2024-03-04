# Day 8

#### Monday, 4-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. Sys module

   - command line arguments using _argv_

   ```python
   import sys
    if len(sys.argv) < 2:
        sys.exit("too few arguments")
    for arg in sys.argv[1:]:
        print(f"Hello, {arg}")
   ```

2. Packages
   - These are modules implemented in a folder
   - You can get 3rd party packages from pypi
   - python has a package manager called _pip_ that enables you to get 3rd party packages
   - To install packages with pip use `pip install cowsay`
   ```python
    import cowsay
    if len(sys.argv) === 2:
        cowsay.cow(f"Hello, {sys.argv[1]}")
   ```
