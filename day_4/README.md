# Day 4

#### Thursday, 29-2-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. conditionals

   - comparison operators are `> >= < <= == !=`
   - logical operators are `and or not`
   - All logic below will run whether the condition finds the right answer or not

   ```python
      if x > y:
         print(f"{x} is greater than {y}")
      if y < x:
         print(f"{y} is greater than {x}")
      if x == y:
         print(f"{x} is equal to {y}")
   ```

   - we can improve on the code above by simply exiting if the statement evaluates to true

   ```python
      if x > y:
          print(f"{x} is greater than {y}")
      elif y < x:
          print(f"{y} is greater than {x}")
      else:
         print(f"{x} is equal to {y}")
   ```

2. Organizing code better with functions

   ```python
      def main():
         x = int(input("what's x?"))
         if is_even(x):
            print(f"{x} is even")
         else:
            print(f"{x} is odd")

      def is_even(n):
        <!-- return True if n % 2 == 0 else False -->
        return n % 2 == 0 # this is even more efficient

      main()
   ```

3. using match

   ```python
      name = input("What's your name?")

      if name=="Harry" or name == "Hermione" or name == "Ron":
         print("Gryffindor")
      elif name == "Draco":
         print("Slytherine")
      else:
         print("who?")
   ```

   - we can express the same thing as above but more compactly using match

   ```python
      match name:
         case "Hermione" | "Ron" | "Harry":
            print("Gryffindor")
         case "Ron":
            print("Slytherine")
         case _:
            print("who?")
   ```
