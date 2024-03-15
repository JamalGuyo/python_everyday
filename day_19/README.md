# Day 19

#### Friday, 15-3-2024

Going through [ Python series by socratis]('https://www.youtube.com/watch?v=iAzShkKzpJo&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=3')

## concepts covered

1. strings in python
2. numbers in python
   - 4 types in python 2: int, long, float and complex
   - 3 types in python 3: int, float and complex
   - python automatically switches to long if int has an overflow
   ```python
    a = 123
    b = 2.718281828
    z =2 - 6.1j
    print(type(a), type(b), type(c)) # int, float, complex
   ```
3. Arithmetic in python

   - any int can be represented as float but not the other way round

   ```python
   x = 28 #int
   y = 28.0 or float(x) #float

   a = 3.14 #float
   int(3.14) # 3
   ```

   - any float can be represented as a complex number but not vice versa

   ```python
   x = 3.14
   y = x +0j or complex(3.14)#complex

   float(y) # type error, can't convert complex to float
   ```

   - when perfoming arithmetic operations, python first converts the numbers to be of the same type and then calculates.
   - for instance,
     - an int and float calculation will result in a float because first python converts all the numbers to floats.
     - a float and complex calculation will result in a complex because first python converts all the numbers to complex.

   ```python
   x = 3.14
   y = 4
   x + y # 7.14, y is converted to float first 4.0
   ```

   - python handles division by
     - `//` - returns quotient
     - `%` - returns remainder
     - `/` - returns the result as float
     - python returns `zero division error` if you divide by zero
