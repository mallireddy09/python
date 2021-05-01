## Arithmetic Operaators
# 1. Addition
x=5
y=4
print(x+y)

# 2. Subtraction
x=5
y=4
print(x-y)

# 3. Multiplication
x=5
y=4
print(x*y)

# 4. Division
x=5
y=4
print(x/y)

# 5. Floor Division
x=5
y=4                                                                     
print(x//y)

#6. Modulus 
x=5
y=4
print(x%y)

# 7. Exponentiation (power)
x=5
y=4
print(x**y)

*** Output ***
9
1
20
1.25
1
1
625

--------------------------------------------------------------------------------------------

## Assignment Operators

x=15
y=9

x += y
print(x)

x -= y
print(x)

x *= y
print(x)

x /= y
print(x)

x %= y
print(x)

x //= y
print(x)

x **= y
print(x)

x = x & y
print(x)

x = x | y
print(x)

x = x ^ y
print(x)

x = x >> y
print(x)

x = x << y
print(x)

*** Output ***
24
15
135
15.0
6.0
0.0
0.0
9
9
0
0
0

-------------------------------------------------------------------------------------------------------

## Comparison Operators

# 1. Equal
x = 5
y = 3
print(x == y)
# returns False because 5 is not equal to 3

# 2. Not equal
x = 5
y = 3
print(x != y)
# returns True because 5 is not equal to 3

# 3. Greater than
x = 5
y = 3
print(x > y)
# returns True because 5 is greater than 3

# 4. Less than
x = 5
y = 3
print(x < y)
# returns False because 5 is not less than 3

# 5. Greater than or equal to
x = 5
y = 3
print(x >= y)
# returns True because five is greater, or equal, to 3

# 6. Less than or equal to
x = 5
y = 3
print(x <= y)
# returns False because 5 is neither less than or equal to 3

*** Output ***
False
True
True
False
True
False

-----------------------------------------------------------------------------------------

## Logical Operators

# 1. And 
# Returns True if both statements are true

x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10

# 2. Or 
# Returns True if one of the statements is true

x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true 
# (5 is greater than 3, but 5 is not less than 4)

# 3. Not
# Reverse the result, returns False if the result is true

x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result

-------------------------------------------------------------------------------------------------

# Identity Operators
 # 1. is
 # Returns True if both variables are the same object

 x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, 
# even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": 
# this comparison returns True because x is equal to y

# 2. is not 
# Returns True if both variables are not the same object

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, 
# even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": 
# this comparison returns False because x is equal to y

---------------------------------------------------------------------------------------------------

# Membership Operators

# 1. in
# Returns True if a sequence with the specified value 
# is present in the object

x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value 
# "banana" is in the list

# 2. not in
# Returns True if a sequence with the 
# specified value is not present in the object

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value 
# "pineapple" is not in the list

-------------------------------------------------------------------------------------------------------

## Bitwise Operators

# 1. AND (&)
# Sets each bit to 1 if both bits are 1

# 2. OR (|)
# Sets each bit to 1 if one of two bits is 1

# 3. XOR (^)
# Sets each bit to 1 if only one of two bits is 1

# 4. NOT 
# Inverts all the bits

# 5. Zero fill left shift (<<)
# Shift left by pushing zeros in from the right 
# and let the leftmost bits fall off.

# 6. Signed right shift (>>)
# Shift right by pushing copies of the leftmost bit 
# in from the left, and let the rightmost bits fall off

--------------------------------------------------------------------------------------------------------