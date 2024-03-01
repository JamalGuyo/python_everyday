# Day 5

#### Friday, 1-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1.  loops

    - while loop

    ```python
        i = 0
        while i < 3:
            print("meow")
            i += 1
    ```

    - for loop

    ```python
        for _ in range(3):
            print("meow")
    ```

            - the underscore indicates that we are not using the iterated value

    - string multiplication
      ```python
          print("meow\n" * 3, end="")
      ```
    - looping through a list

      ```python
          students = ["Hermione", "Ron", "Draco", "Harry"]
          for i in range(len(students)):
              print(i + 1, students[i])

          for i, student in enumerate(students,100):
              print(i, student)
      ```
