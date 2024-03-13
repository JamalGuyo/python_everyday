# Day 17

#### Wednesday, 13-3-2024

Going through [Havard's cs50 introduction to programming in python]('https://www.youtube.com/watch?v=nLRL_NcnK-4')

## concepts covered

1. map

   - we can traverse an iterable and change the items using `map` function

   ```python
   words = ['This', 'is', 'cs50']
   uppercased = map(str.upper, words)
   ```

2. list comprehension

   - we can traverse through a list and change the items using list comprehension as well

   ```python
   uppercased = [word.upper() for word in words]
   ```

3. filter
   - we can filter iterables using the filter function
   ```python
   students = [
      {"name": "Harry", "house": "Gryffindor"},
      {"name": "Ron", "house": "Gryffindor"},
      {"name": "Draco", "house": "Slytherine"}
   ]
   gryffindors = filter(lambda s: s['house'] == 'Gryffindor',students)
   ```
