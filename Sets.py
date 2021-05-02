
# Set
-> Sets are used to store multiple items in a single variable.
-> A set is a collection which is both unordered and unindexed.
-> Sets are written with curly brackets.
-> Set items are unordered, unchangeable, and do not allow duplicate values.
-> Duplicate values will be ignored.
-> Sets are unordered, so you cannot be sure in which order the items will appear.

#Create a Set:
set = {"pspk", "ssmb", "prabhas"}
print(set)
-> {'pspk', 'prabhas', 'ssmb'}

# Length of a Set
set = {"pspk", "ssmb", "prabhas"}
print(len(set))
-> 3
---------------------------------------------------------------------------------------------------------------------------------------------

# Set Items - Data Types
-> Set items can be of any data type.

set = {"Me", 20, True, "male"}
print(set)
-> {True, 'male', 20, 'Me'}

# set() Constructor
set1 = set(("pspk", "ssmb", "prabhas"))
# note the double round-brackets
print(set1)
-> {'pspk', 'ssmb', 'prabhas'}

## Access Items

-> You cannot access items in a set by referring to an index or a key.
-> loop through the set items using a for loop, or ask if a specified 
    value is present in a set, by using the in keyword.
    
set = {"pspk", "ssmb", "prabhas"}
for x in set:
    print(x)
-> pspk
   prabhas
   ssmb

set = {"pspk", "ssmb", "prabhas"}
print("ssmb" in set)
-> True

---------------------------------------------------------------------------------------------------------------------------------------------

## Add Set Items
# Add Items
-> To add one item to a set use the add() method.

set = {"pspk", "ssmb", "prabhas"}
set.add("rapo")
print(set)
-> {'ssmb', 'pspk', 'prabhas', 'rapo'}

# Add Sets
-> To add items from another set into the current set, 
use the update() method.

set = {"pspk", "ssmb", "prabhas"}
set1 = {"rapo" ,"rc"}
set.update(set1)
print(set)
-> {'pspk', 'ssmb', 'rapo', 'rc', 'prabhas'}

# Add Any Iterable
-> The object in the update() method does not have be a set, 
   it can be any iterable object (tuples, lists, dictionaries etc.).

set = {"pspk", "ssmb", "prabhas"}
list = ["kanna", "mummy"]
set.update(list)
print(set)
-> {'mummy', 'ssmb', 'pspk', 'prabhas', 'kanna'}

---------------------------------------------------------------------------------------------------------------------------------------------

# union() method returns a new set with all items from both sets.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
-> {2, 'a', 1, 'c', 3, 'b'}

# Keep ONLY the Duplicates
-> The intersection_update() method will keep only the items 
   that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
-> {'apple'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
-> {'apple'}

---------------------------------------------------------------------------------------------------------------------------------------------

# Keep All, But NOT the Duplicates
-> The symmetric_difference_update() method will keep only 
   the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
-> {'google', 'banana', 'microsoft', 'cherry'}

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
-> {'google', 'banana', 'microsoft', 'cherry'}

---------------------------------------------------------------------------------------------------------------------------------------------

# Remove Item
-> use the remove(), or the discard() method.
-> If the item to remove does not exist, remove() will raise an error.
-> If the item to remove does not exist, discard() will NOT raise an error.

set = {"pspk", "ssmb", "prabhas"}
set.remove("prabhas")
print(set)
-> {'ssmb', 'pspk'}

set = {"pspk", "ssmb", "prabhas"}
set.discard("prabhas")
print(set)
-> {'ssmb', 'pspk'}

# pop() method:
-> Sets are unordered, so when using the pop() method, 
   you do not know which item that gets removed.

set = {"pspk", "ssmb", "prabhas"}
x = set.pop()
print(x) #removed item
print(set) #the set after removal
-> ssmb
   {'pspk', 'prabhas'}

---------------------------------------------------------------------------------------------------------------------------------------------

# clear() method empties the set
set = {"pspk", "ssmb", "prabhas"}
set.clear()
print(set)
-> set()

# del keyword will delete the set completely
set1 = {"pspk", "ssmb", "prabhas"}
del set1
print(set1)
-> Traceback (most recent call last):
  File "d:\Python\Sets.py", line 114, in <module>
    print(set1)
  NameError: name 'set1' is not defined

---------------------------------------------------------------------------------------------------------------------------------------------

## Set Methods

# Method	            Description
add()	                        Adds an element to the set
clear()	                        Removes all the elements from the set
copy()	                        Returns a copy of the set
difference()	                Returns a set containing the difference between two 
                                or more sets
difference_update()	            Removes the items in this set that are also included 
                                in another, specified set
discard()	                    Remove the specified item
intersection()  	            Returns a set, that is the intersection of two other sets
intersection_update()	        Removes the items in this set that are not present
                                in other, specified set(s)
isdisjoint()	                Returns whether two sets have a intersection or not
issubset()	                    Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                        Removes an element from the set
remove()	                    Removes the specified element
symmetric_difference()	        Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others

---------------------------------------------------------------------------------------------------------------------------------------------