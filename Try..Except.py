
# Try Except

1. The try block lets you test a block of code for errors.

2. The except block lets you handle the error.

3. The finally block lets you execute code, regardless of the 
result of the try- and except blocks.

#  Exception Handling

1. When an error occurs, or exception as we call it, 
   Python will normally stop and generate an error message.

2. These exceptions can be handled using the try statement.
------------------------------------------------------------------------------------------------------------------------------------------

Example:

try:
  print(x)
except:
  print("An exception occurred")

-> An exception occurred

 # Since the try block raises an error, the except block will be executed.
 #  Without the try block, the program will crash and raise an error.
------------------------------------------------------------------------------------------------------------------------------------------

# Else
else keyword to define a block of 
code to be executed if no errors were raised:

Example:
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
-> Hello
   Nothing went wrong
------------------------------------------------------------------------------------------------------------------------------------------

# Finally
The finally block, if specified, will be executed regardless 
if the try block raises an error or not.

Example:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

-> Something went wrong
   The 'try except' is finished
------------------------------------------------------------------------------------------------------------------------------------------

# Raise an exception
-> raise keyword is used to raise (throw) an exception.
-> we can define what kind of error to raise, 
   and the text to print to the user.

Example:
# Raise an error and stop the program if x is lower than 0:

x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")

-> Traceback (most recent call last):
  File "d:\Python\Try..Except.py", line 70, in <module>
    raise Exception("Sorry, no numbers below zero")
  Exception: Sorry, no numbers below zero
  ------------------------------------------------------------------------------------------------------------------------------------------
