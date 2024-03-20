# Day 24

#### Wednesday, 20-3-2024

Going through [ Python series by socratis]('https://www.youtube.com/watch?v=iAzShkKzpJo&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=3')

## concepts covered

1.Dictionaries

- dictionaries are used to store key value pairs
- you can create a dictionary using the short-hand `{"name":"Jamal"}` or using the constructor `dict(name="Jamal"")`
- you can assign key value pairs using `person["name"]="Jamal"`
- attempting to access a key that doesn't exist results in `KeyError`. We can handle this by:
  - either checking if the exists before acccessing it.
  ```Python
  if 'name' in person:
    print(person['name'])
  else:
    print(f'key {name} does not exist')
  ```
  - or you can use a `try` `catch` statement
  ```Python
  try:
    print(person['name'])
  except KeyError:
    print(f'key {name} does not exist')
  ```
- we can check dictionary methods and properties available to us using `dir(person)`
- we can iterate over the dictionary using:
  - `for key in person.keys():` will iterate over the keys
  - `for key, value in person.items()` will iterate over both the key and value
- to remove items from a dictionary we can use: -`clear` to remove all items -`pop` or `popitems` to remove a single item
