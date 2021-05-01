
##Tuple
-> Tuples are used to store multiple items in a single variable.
-> A tuple is a collection which is ordered , unchangeable and
   allow duplicate values.
-> Tuples are written with round brackets.

#Create a Tuple:
tuple = ("puppy", "zoombie", "chicha")
print(tuple)
-> ('puppy', 'zoombie', 'chicha')

----------------------------------------------------------------------------------------------------

# Allow Duplicates
tuple = ("puppy", "zoombie", "chicha", "puppy")
print(tuple)
-> ('puppy', 'zoombie', 'chicha', 'puppy')

# Tuple Length
tuple = ("puppy", "zoombie", "chicha")
print(len(tuple))
-> 3

----------------------------------------------------------------------------------------------------

# Create Tuple With One Item
-> To create a tuple with only one item, you have to add a comma 
   after the item, otherwise Python will not recognize it as a tuple.

tuple = ("Zoombie",)
print(type(tuple))
print(tuple)
-> <class 'tuple'>
-> ('Zoombie',)

# Tuple Items - Data Types
-> Tuple items can be of any data type

tuple = ("Me", 20, True, "male")
print(tuple)
-> ('Me', 20, True, 'male')

----------------------------------------------------------------------------------------------------

# tuple() Constructor
-> use the tuple() constructor to make a tuple.

tuple1 = tuple(("puppy", "zoombie", "chicha"))
print(tuple1)
-> ('puppy', 'zoombie', 'chicha')

----------------------------------------------------------------------------------------------------

# Access Tuple Items
-> You can access tuple items by referring to the index number, 
   inside square brackets:

tuple = ("puppy", "zoombie", "chicha")
print(tuple[0])
-> puppy

----------------------------------------------------------------------------------------------------

# Negative Indexing
tuple = ("puppy", "zoombie", "chicha")
print(tuple[-1])
-> chicha

# Range of Indexes
tuple = ("puppy", "zoombie", "chicha" ,"raki" ,"yuvi")
print(tuple[1:4])
-> ('zoombie', 'chicha', 'raki')

tuple = ("puppy", "zoombie", "chicha" ,"raki" ,"yuvi")
print(tuple[:4])
-> ('puppy', 'zoombie', 'chicha', 'raki')

tuple = ("puppy", "zoombie", "chicha" ,"raki" ,"yuvi")
print(tuple[2:])
-> ('chicha', 'raki', 'yuvi')

# Range of Negative Indexes
-> Specify negative indexes if you want to start
   the search from the end of the tuple:

tuple = ("puppy", "zoombie", "chicha" ,"raki" ,"yuvi")
print(tuple[-4:-1])
-> ('zoombie', 'chicha', 'raki')

----------------------------------------------------------------------------------------------------

# Check if Item Exists
-> To determine if a specified item is present
   in a tuple use the in keyword.

tuple = ("puppy", "kanna", "mummy")
if "kanna" in tuple:
    print("Yes, 'kanna' is in the name tuple")
-> Yes, 'kanna' is in the name tuple

----------------------------------------------------------------------------------------------------

# Change Tuple Values
-> Tuples are unchangeable, or immutable. But
   You can convert the tuple into a list, change the list, 
    and convert the list back into a tuple.

x = ("Ema Watson", "Jennifer", "Naomi Watts")
y = list(x)
y[1] = "kanna"
x = tuple(y)
print(x)
-> ('Ema Watson', 'kanna', 'Naomi Watts')

x = ("Ema Watson", "Jennifer", "Naomi Watts")
y = list(x)
y.append("kanna")
x = tuple(y)
print(x)
-> ('Ema Watson', 'Jennifer', 'Naomi Watts', 'kanna')

x = ("Ema Watson", "Jennifer", "Naomi Watts" ,"kanna")
y = list(x)
y.remove("Jennifer")
x = tuple(y)
print(x)
-> ('Ema Watson', 'Naomi Watts', 'kanna')

----------------------------------------------------------------------------------------------------

# Tuple Delete
-> The del keyword can delete the tuple completely:

tuple1 = ("Ema Watson", "Jennifer", "Naomi Watts")
del tuple1
print(tuple1)

-> Traceback (most recent call last):
  File "d:\Python\Tuples.py", line 123, in <module>
    print(tuple1)
NameError: name 'tuple1' is not defined

----------------------------------------------------------------------------------------------------

##Loop Tuples
# Loop Through a Tuple

tuple = ("puppy", "kanna", "mummy")
for x in tuple:
    print(x)
-> puppy
   kanna
   mummy

# Loop Through the Index Numbers  
-> Use the range() and len() functions to 
   create a suitable iterable. 

tuple = ("puppy", "kanna", "mummy")
for x in range(len(tuple)):
    print(tuple[x])
-> puppy
   kanna
   mummy

----------------------------------------------------------------------------------------------------

