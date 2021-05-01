##Strings

Strings in python are surrounded by either single quotation marks,
or double quotation marks.

e.g., 'hello' is the same as "hello".

print('Hi Friends')
print("Hi Friends")
print(""""Hi Friends"""")

*** Output ***

Hi Friends
Hi Friends
Hi Friends

-----------------------------------------------------------------------------------------------

##Strings are Arrays

Strings in Python are arrays of bytes representing unicode characters.
Square brackets can be used to access elements of the string.

a = "Hello Friends.!"
print(a[4])
-> o

---------------------------------------------------------------------------------------------

##Looping Through a String

Strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "rat":
  print(x) 

*** Output ***
r
a
t

-------------------------------------------------------------------------------------------------

##String Length
The len() function returns the length of a string:

v = "Hello Amma.!"
print(len(v))

-> 12

------------------------------------------------------------------------------------------------

##Check String
To check if a certain phrase or character is present in a string,
we can use the keyword in.

txt = "love is free!"
if "free" in txt:
    print("Yup, 'free' is present.")

  -> Yup, 'free' is present.

-----------------------------------------------------------------------------------------------

## Slice to the End

v = "Hello Amma.!"
print(v[6:])
-> Amma.!

## Slice From the Start

v = "Hello Amma.!"
print(v[:5])
-> Hello

## Slice specified position

v = "Hello Amma.!"
print(v[2:5])
-> llo

## Negative Indexing
Use negative indexes to start the 
slice from the end of the string:

v = "Hello Amma.!"

print(v[-8:-2])
->o Amma

print(v[:-2])
->Hello Amma

print(v[-11:])
-> ello Amma.!

## Reverse the string
print(v[::-1])
-> !.ammA olleH

-------------------------------------------------------------------------------------------------

## Modify Strings

v = "Hello Amma.!"

print(v.upper()) # Upper Case
-> HELLO AMMA.!

print(v.lower()) # Lower case
-> hello amma.!

#Remove Whitespace
The strip() method removes any whitespace from 
the beginning or the end:

v = "  Hello Amma.!  "
print(v.strip()) # returns "Hello Amma.!"
-> Hello Amma.!

# Replace String
The replace() method replaces a string with another string:

v = "Hello Amma.!"
print(v.replace("H", "C"))
-> Cello Amma.! 

#Split String
The split() method splits the string into substrings 
if it finds instances of the separator.

v = "Hello, Amma.!"
print(v.split(",")) 
-> ['Hello', ' Amma.!']

----------------------------------------------------------------------------------------------

##String Concatenation
#To concatenate, or combine, two strings you can use the + operator.

a = "Hello"
b = "World"
c = a + b
print(c)
-> HelloWorld

#To add a space between them, add a " ":

a = "Hello"
b = "World"
c = a + " " + b
print(c)
-> Hello World

-----------------------------------------------------------------------------------------------

#String Format
1. we can combine strings and numbers by using the format() method!

age = 20
txt = "My name is Mava, and I am {}"
print(txt.format(age))

-> My name is Mava, and I am 20

2. The format() method takes unlimited number of arguments,
and are placed into the respective placeholders:

quantity = 15
itemno = 15419
price = 49.66
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

-> I want 15 pieces of item 15419 for 49.66 dollars.

3. Use index numbers {0} to be sure the arguments 
are placed in the correct placeholders:

quantity = 15
itemno = 15419
price = 49.66
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

-> I want to pay 49.66 dollars for 15 pieces of item 15419.

-------------------------------------------------------------------------------------------------

# Method	    Description

capitalize()	Converts the first character to upper case
casefold()	    Converts string into lower case
center()	    Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()	    Returns an encoded version of the string
endswith()  	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()      	Searches the string for a specified value and returns the position 
                of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position 
                of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()	        Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position 
                of where it was found
rindex()	    Searches the string for a specified value and returns the last position 
                of where it was found
rjust()     	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	        Returns a trimmed version of the string
swapcase()  	Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
zfill()     	Fills the string with a specified number of 0 values at the beginning

------------------------------------------------------------------------------------------------