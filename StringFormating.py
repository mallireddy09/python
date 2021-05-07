#String Format

1. we can combine strings and numbers by using the format() method.
2. format() method allows you to format selected parts of a string.
3. To control such values, add placeholders (curly brackets {}) 
   in the text, and run the values through the format() method.
# Example

age = 20
txt = "My name is MaVa, and I am {}"
print(txt.format(age))

-> My name is MaVa, and I am 20
---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Using different placeholder values:

txt1 = "My name is {fname}, I'm {age}".format(fname = "MaVa", age = 20)
txt2 = "My name is {0}, I'm {1}".format("MaVa",20)
txt3 = "My name is {}, I'm {}".format("MaVa",20)

-> My name is MaVa, I'm 20
---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Multiple Values
-> To use more values, just add more values to the format() method:

 # print(txt.format(price, itemno, count)) #

# Example

quantity = 15
itemno = 15419
price = 49.66
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

-> I want 15 pieces of item 15419 for 49.66 dollars.
---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Index Numbers
-> use index numbers (a number inside the curly brackets {0}) 
   to be sure the values are placed in the correct placeholders.

# Example

quantity = 15
itemno = 150419
price = 49.66
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

-> I want to pay 49.66 dollars for 15 pieces of item 150419.
---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Named Indexes.
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Tesla", model = "SUV"))

-> I have a Tesla, it is a SUV. 
---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Formatting Types
-> Inside the placeholders you can add a formatting type to format the result.

:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers 
        (and a minus sign befor negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show ma and va as MA and VA)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format

####### for code go through github. link in the bio #######
---------------------------------------------------------------------------------------------------------------------------------------------------------------

1. #Use "<" to left-align the value:

# we insert the number 8 to set the available space for the value to 8 characters.
txt = "We have {:<8} chickens."
print(txt.format(49))
-> We have 49       chickens.

2. #Use ">" to right-align the value:

# we insert the number 8 to set the available space for the value to 8 characters.
txt = "We have {:>8} chickens."
print(txt.format(49))
-> We have       49 chickens.

3. #Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))
-> We have    49    chickens.

4. #Use "=" to place the plus/minus sign at the left most position:

txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))
-> The temperature is -      5 degrees.

5. #Use "+" to always indicate if the number is positive or negative:

txt = "The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))
-> The temperature is between -3 and +7 degrees celsius.

6. #Use "-" to always indicate if the number is negative (positive numbers are displayed without any sign):

txt = "The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))
-> The temperature is between -3 and 7 degrees celsius.

7. #Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:

txt = "The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))
-> The temperature is between -3 and  7 degrees celsius.

8. #Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."
print(txt.format(13800000000))
-> The universe is 13,800,000,000 years old.

9. #Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."
print(txt.format(13800000000))
-> The universe is 13_800_000_000 years old.

10. #Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"
print(txt.format(15))
-> The binary version of 15 is 1111

11. #Use "d" to convert a number, in this case a binary number, into decimal number format:

txt = "We have {:d} chickens."
print(txt.format(0b101))
-> We have 5 chickens.

12. #Use "e" to convert a number into scientific number format (with a lower-case e):

txt = "We have {:e} chickens."
print(txt.format(5))
-> We have 5.000000e+00.

13. #Use "E" to convert a number into scientific number format (with an upper-case E):

txt = "We have {:E} chickens."
print(txt.format(5))
-> We have 5.000000E+00.

14. #Use "f" to convert a number into a fixed point number, default with 6 decimals, but use a period followed by a number to specify the number of decimals:

txt = "The price is {:.2f} dollars."
print(txt.format(49))
#without the ".2" inside the placeholder, this number will be displayed like this:
txt = "The price is {:f} dollars."
print(txt.format(49))
-> The price is 49.00 dollars.
-> The price is 49.000000 dollars.

15. #Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')
txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:
txt = "The price is {:f} dollars."
print(txt.format(x))
-> The price is INF dollars.
-> The price is inf dollars.

16. #Use "o" to convert the number into octal format:

txt = "The octal version of {0} is {0:o}"
print(txt.format(15))

-> The octal version of 15 is 17

17. #Use "x" to convert the number into Hex format:

txt = "The Hexadecimal version of {0} is {0:x}"
print(txt.format(255))
-> The Hexadecimal version of 255 is ff

18. #Use "X" to convert the number into upper-case Hex format:

txt = "The Hexadecimal version of {0} is {0:X}"
print(txt.format(255))
-> The Hexadecimal version of 255 is FF

19. #Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.66))

#Or, without any decimals:
txt = "You scored {:.0%}"
print(txt.format(0.66))
-> You scored 66.000000%
-> You scored 66%

---------------------------------------------------------------------------------------------------------------------------------------------------------------