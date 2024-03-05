# Day 9

#### Tuesday, 5-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. unit testing

   - we can test a function that takes a single integer argument and returns square of the argument as follows

   ```python
   def test_square():
       if square(2) != 4:
           print("2 squared is not equal to 4")
       if square(3) != 9:
           print("3 squared is not equal to 9")
   ```

   - it is advisable to write more than one tests to capture any corner cases. For instance, `2+2=4` hence the first test will pass if the square function did summation but the second test will fail

   - using `assert` keyword

   ```python
   def test_square():
        try:
            assert square(2) == 4
        except AssertionError:
            print("2 squared is not 4")
        try:
            assert square(3) == 9
        except AssertionError:
            print("3 squared is not 9")
   ```

   - The above example is still to verbose.
