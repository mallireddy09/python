#strings data type(str)

#String are identified as a contiguous set of characters represented in the quotation mark.
# Python allows for either pairs of single or double quotes.
# Strings are immulatable sequence data type,i.e each time one make many changes to string,
# completely new object string is created.

x = "Hi Friends"
#display x:
print(x)
#display the data type of x:
print(type(x)) 

*** Output ***
Hi Friends
<class 'str'>

---------------------------------------------------------------------------------------------------

#Numeric data type (int)

x = 20
#display x:
print(x)
#display the data type of x:
print(type(x)) 


*** Output ***
20
<class 'int'>

---------------------------------------------------------------------------------------------------

#Numeric data type (float)

x = 49.6
#display x:
print(x)
#display the data type of x:
print(type(x)) 

*** Output ***
49.6
<class 'float'>

---------------------------------------------------------------------------------------------------


#Numeric data type (complex)

x = 1j
#display x:
print(x)
#display the data type of x:
print(type(x))


*** Output ***
1j
<class 'complex'>

-----------------------------------------------------------------------------------------------------

#Sequence data type (list)

#Lists are enclosed in brackets[] and their elements and size can be changed.
#Lists are Mutable

x = ["apple", "banana", "cherry"]
#display x:
print(x)
#display the data type of x:
print(type(x)) 

*** Output ***
['apple', 'banana', 'cherry']
<class 'list'>

-------------------------------------------------------------------------------------------------------

#Sequence data type (tuple) 

#Tuples are enclosed in parenthesis () and cannot be updated.
#Tuples are innmutable.

x = ("apple", "banana", "cherry")
#display x:
print(x)
#display the data type of x:
print(type(x)) 

*** Output ***
('apple', 'banana', 'cherry')
<class 'tuple'>

------------------------------------------------------------------------------------------------------

#Sequence data type (range)

x = range(9)
#display x:
print(x)
#display the data type of x:
print(type(x)) 


*** Output ***
range(0, 9)
<class 'range'>

-----------------------------------------------------------------------------------------------------

#Mapping data type (dict)
#Dictionary consist of key value-pairs.
# It is enclosed by curly braces{} and values can be assigned and accessed using square brackets[].

x = {"name" : "Robo", "age" : 19}
#display x:
print(x)
#display the data type of x:
print(type(x)) 


*** Output ***
{'name': 'Robo', 'age': 19}
<class 'dict'>

-----------------------------------------------------------------------------------------------------

#Set data type (set)
#   Sets are unordered collection of unique objects, there are two types of set:
#   a. Sets-They are mutable and new elements can be added once sets are allowed

x = {"apple", "banana", "cherry"}
#display x:
print(x)
#display the data type of x:
print(type(x)) 

*** Output ***
{'banana', 'apple', 'cherry'}
<class 'set'>

-----------------------------------------------------------------------------------------------------

#Frozen set data type (frozenset)
#   b. Frozen Sets-They are immutable and new elements cannot be added after its defined.

x = frozenset({"apple", "banana", "cherry"})
#display x:
print(x)
#display the data type of x:
print(type(x)) 

*** Output ***
frozenset({'apple', 'banana', 'cherry'})
<class 'frozenset'>

-----------------------------------------------------------------------------------------------------

#Boolean data type (bool)

x = True
#display x:
print(x)
#display the data type of x:
print(type(x)) 

*** Output ***
True
<class 'bool'>

----------------------------------------------------------------------------------------------------

#Binary data type (bytes)

x = b"Hello"
#display x:
print(x)
#display the data type of x:
print(type(x)) 

*** Output ***
b'Hello'
<class 'bytes'>

-----------------------------------------------------------------------------------------------------

#Binary data type (bytearray)

x = bytearray(9)
#display x:
print(x)
#display the data type of x:
print(type(x)) 

*** Output ***
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00')
<class 'bytearray'>

--------------------------------------------------------------------------------------------------------

#Binary data type (memoryview)

x = memoryview(bytes(9))
#display x:
print(x)
#display the data type of x:
print(type(x)) 


*** Output ***
<memory at 0x000002DF7F776DC0>
<class 'memoryview'>