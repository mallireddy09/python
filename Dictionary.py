
## Dictionary
-> Dictionaries are used to store data values in key:value pairs.
-> A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
-> Dictionaries are written with curly brackets, and have keys and values.
-> Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#Create and print a dictionary:

dict = {
  "brand": "Tesla",
  "model": "SUV",
  "year": 2015
}
print(dict)
-> {'brand': 'Tesla', 'model': 'SUV', 'year': 2015}

-------------------------------------------------------------------------------------------------------------------

# Duplicates Not Allowed
-> Duplicate values will overwrite existing values.

dict = {
  "brand": "Tesla",
  "model": "SUV",
  "year": 2009,
  "year": 2015
}
print(dict)
-> {'brand': 'Tesla', 'model': 'SUV', 'year': 2015}


# Dictionary Items - Data Types
-> The values in dictionary items can be of any data type
dict = {
  "brand": "Tesla",
  "model": "SUV",
  "year": 2015,
  "colors": ["red", "white", "blue"]
}
print(dict)
print(len(dict))
print(type(dict))
-> {'brand': 'Tesla', 'model': 'SUV', 'year': 2015, 'colors': ['red', 'white', 'blue']}
-> 4
-> <class 'dict'>

-------------------------------------------------------------------------------------------------------------------

## Accessing Items
dict = {
  "brand": "Tesla",
  "model": "SUV",
  "year": 2015
}
# get() method will return a the value of the "model" key
x = dict["model"]   # same as x = dict.get("model")
# keys() method will return a list of all the keys in the dictionary.
y = dict.keys()
# tems() method will return each item in a dictionary, as tuples in a list.
z = dict.items()

print(x)
print(y)
print(z)

-> SUV
-> dict_keys(['brand', 'model', 'year'])
-> dict_items([('brand', 'Tesla'), ('model', 'SUV'), ('year', 2015)])

-------------------------------------------------------------------------------------------------------------------

# -> Add a new item to the original dictionary, and see that 
#    the keys, values, items(keys, values),list gets updated and check item is in dictionary.
car = {
"brand": "Tesla",
"model": "SUV",
"year": 2009
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

y = car.values()
print(y) ##before the change
car["year"] = 2020
print(y) #after the change

z = car.items()
print(z) #before the change
car["year"] = 2021
print(z) #after the change

v = car.items()
print(v) #before the change
car["color"] = "red"
print(v) #after the change

if "model" in car:
  print("Yes, 'model' is one of the keys in the car dictionary")

->  dict_keys(['brand', 'model', 'year'])
    dict_keys(['brand', 'model', 'year', 'color'])
->  dict_values(['Tesla', 'SUV', 2009, 'white'])
    dict_values(['Tesla', 'SUV', 2020, 'white'])
->  dict_items([('brand', 'Tesla'), ('model', 'SUV'), ('year', 2020), ('color', 'white')])
    dict_items([('brand', 'Tesla'), ('model', 'SUV'), ('year', 2021), ('color', 'white')])
->  dict_items([('brand', 'Tesla'), ('model', 'SUV'), ('year', 2021), ('color', 'white')])
    dict_items([('brand', 'Tesla'), ('model', 'SUV'), ('year', 2021), ('color', 'red')])
->  Yes, 'model' is one of the keys in the car dictionary

-------------------------------------------------------------------------------------------------------------------

## Change Dictionary Items

dict = {
  "brand": "Tesla",
  "model": "SUV",
  "year": 2009
}
print(dict)  #before the change
# change the value of a specific item by referring to its key name.
dict["year"] = 2018  
print(dict) 
# update() method will update the dictionary with the items from the given argument.
dict.update({"year": 2020})
print(dict)

-> {'brand': 'Tesla', 'model': 'SUV', 'year': 2009}
-> {'brand': 'Tesla', 'model': 'SUV', 'year': 2018}
-> {'brand': 'Tesla', 'model': 'SUV', 'year': 2020}

-------------------------------------------------------------------------------------------------------------------

## Remove Dictionary Items

dict1 = {
  "brand": "Tesla",
  "model": "SUV",
  "year": 2009
}
print(dict1)  #before the change
## pop() method removes the item with the specified key name.
dict1.pop("model")
print(dict1)
## popitem() method removes the last inserted item.
dict1.popitem()
print(dict1)
## clear() method empties the dictionary.
dict1.clear()
print(dict1)
## del keyword removes the item with the specified key name.
##del keyword can also delete the dictionary completely.
#this will cause an error because "thisdict" no longer exists.
del dict1
print(dict1)

-> {'brand': 'Tesla', 'model': 'SUV', 'year': 2009}
-> {'brand': 'Tesla', 'year': 2009}
-> {'brand': 'Tesla'}
-> {}
-> Traceback (most recent call last):
   File "d:\Python\Dictionary.py", line 150, in <module>
   print(dict1)
   NameError: name 'dict1' is not defined

-------------------------------------------------------------------------------------------------------------------

## Loop Dictionaries

dict = {
  "brand": "Tesla",
  "model": "SUV",
  "year": 2009
}
# Print all key names in the dictionary, one by one.
for x in dict:    
    print(x)
# Print all values in the dictionary, one by one.
for x in dict:
    print(dict[x])
# keys() method to return the keys of a dictionary.
for x in dict.keys():
    print(x)
# values() method to return values of a dictionary.
for x in dict.values():
    print(x)
# Loop through both keys and values, by using the items() method.
for x, y in dict.items():
  print(x, y)

->  brand
    model
    year

->  Tesla
    SUV
    2009

->  brand
    model
    year

->  Tesla
    SUV
    2009

->  brand Tesla
    model SUV
    year 2009

-------------------------------------------------------------------------------------------------------------------

## Copy a Dictionary
-> You cannot copy a dictionary simply by typing dict2 = dict1,
   because: dict2 will only be a reference to dict1, and changes 
   made in dict1 will automatically also be made in dict2.

-> There are ways to make a copy, one way is 
   to use the built-in Dictionary method copy().

dict1 = {
  "brand": "Tesla",
  "model": "SUV",
  "year": 2009
}
# Make a copy of a dictionary with the copy() method:
mydict = dict1.copy()
print(mydict)

# make a copy is to use the built-in function dict().
mydict = dict(dict1)
print(mydict)

-> {'brand': 'Tesla', 'model': 'SUV', 'year': 2009}
-> {'brand': 'Tesla', 'model': 'SUV', 'year': 2009}

-------------------------------------------------------------------------------------------------------------------

## Nested Dictionaries
-> A dictionary can contain dictionaries.

# Create a dictionary that contain two dictionaries:
Tollywood = {
  "Hero1" : {
    "Name" : "SSMB",
    "Year" : 1999
  },
  "Hero2" : {
    "Name" : "PSPK",
    "Year" : 1996
  },
}
print(Tollywood)

-> {'Hero1': {'Name': 'SSMB', 'Year': 1999}, 'Hero2': {'Name': 'PSPK', 'Year': 1996}}

-------------------------------------------------------------------------------------------------------------------

# If you want to add two dictionaries into a new dictionary:
-> Create two dictionaries, then create 
 one dictionary that will contain the other two dictionaries:
 
Hero1 = {
    "Name" : "SSMB",
    "Year" : 1999
  },
Hero2 = {
    "Name" : "PSPK",
    "Year" : 1996
  }
Tollywood = {
      "Hero1" : Hero1,
      "Hero2" : Hero2
  }
print(Tollywood)

-> {'Hero1': ({'Name': 'SSMB', 'Year': 1999},), 'Hero2': {'Name': 'PSPK', 'Year': 1996}}

-------------------------------------------------------------------------------------------------------------------

# Dictionary Methods

# Method	    Description

clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: 
                insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary

-------------------------------------------------------------------------------------------------------------------