# Math
# Built-in Math Functions

-> min() and max() functions can be used to find the 
   lowest or highest value in an iterable.

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)   # 5 
print(y)   # 25
-----------------------------------------------------------------------------------

-> abs() function returns the absolute (positive) 
   value of the specified number.

x = abs(-7.25)
print(x)  # 7.25
-----------------------------------------------------------------------------------

-> pow(x, y) function returns the value 
    of x to the power of y (xy).

x = pow(4, 3)
print(x)  # 64

----------------------------------------------------------------------------------------------------------------------------------------------

# Math Module
-> Python has also a built-in module called math, 
   which extends the list of mathematical functions.
-> To use it, you must import the math module:
# import math
-----------------------------------------------------------------------------------

-> math.sqrt() method, returns the square root of a number.

import math
x = math.sqrt(81)
print(x)  # 9.0
-----------------------------------------------------------------------------------

-> math.ceil() method rounds a number upwards to its nearest integer.
-> math.floor() method rounds a number downwards to its nearest integer.

import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)   # 2
print(y)   # 1

----------------------------------------------------------------------------------------------------------------------------------------------

# Math Constants

-> math.pi constant, returns the value of PI (3.14...)

import math
x = math.pi
print(x) # 3.141592653589793
-----------------------------------------------------------------------------------

-> math.e constant returns the Eular's number: 2.718281828459045.

import math
x = math.e
print(x)  # 2.718281828459045

----------------------------------------------------------------------------------------------------------------------------------------------