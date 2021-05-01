##List
Lists are used to store multiple items in a single variable.
Lists are created using square brackets.

#Create a List:

list = ["Yuvraj", "Dhoni", "Jadeja"]
print(list)
-> ['Yuvraj', 'Dhoni', 'Jadeja']

#List Items
-> List items are ordered, changeable, and allow duplicate values.
-> List items are indexed, the first item has index [0], 
   the second item has index [1] etc.

---------------------------------------------------------------------------------------------------

# Allow Duplicates

list = ["Yuvraj", "Dhoni", "Jadeja","Dhoni"]
print(list)
-> ['Yuvraj', 'Dhoni', 'Jadeja', 'Dhoni']

# Length

list = ["Yuvraj", "Dhoni", "Jadeja"]
print(len(list))
-> 3

# List Items - Data Types

-> List items can be of any data type.
-> A list with strings, integers and boolean values:

list1 = ["Dhoni", 7, True, 39, "male"]
print(list1)
-> ['Dhoni', 7, True, 39, 'male']

---------------------------------------------------------------------------------------------------

## list() Constructor
-> It is also possible to use the list() 
   constructor when creating a new list.

list = list(("Yuvraj", "Dhoni", "Jadeja"))
# note the double round-brackets
print(list)
-> ['Yuvraj', 'Dhoni', 'Jadeja']

---------------------------------------------------------------------------------------------------

##Access Items
-> List items are indexed and you can access them by referring to the index number:

list = ["Yuvraj", "Dhoni", "Kane Mawa", "David Bhai", "Sam Curran"]

print(list[1]) 
-> Dhoni

print(list[-1]) #Negative Indexing
-> Tahir

print(list[2:5]) #Range of Indexes
-> ['Jadeja', 'Kane Mawa', 'David Bhai']

print(list[:4]) 
-> ['Yuvraj', 'Dhoni', 'Jadeja', 'Kane Mawa']

print(list[2:])
-> ['Jadeja', 'Kane Mawa', 'David Bhai', 'Sam Curran', 'Tahir'] 

print(list[-4:-1]) #Range of Negative Indexes
-> ['Kane Mawa', 'David Bhai', 'Sam Curran']

---------------------------------------------------------------------------------------------------

## Check if Item Exists
-> To determine if a specified item is present in a list use the in keyword:

list = ["Yuvraj", "Dhoni", "Jadeja"]
if "Dhoni" in list:
    print("Yes, 'Dhoni' is in the cricketer list")
-> Yes, 'Dhoni' is in the cricketer list

---------------------------------------------------------------------------------------------------

## Change List Items
-> To change the value of items within a specific range, define a list with the new values,
   and refer to the range of index numbers where you want to insert the new values:
   
list = ["Yuvraj", "Dhoni", "Kane Mawa", "David Bhai", "Sam Curran"]
list[3] = "Mr.360"  #Change Item Value
print(list)
-> ['Yuvraj', 'Dhoni', 'Kane Mawa', 'Mr.360', 'Sam Curran']

list = ["Yuvraj", "Dhoni", "Kane Mawa", "David Bhai", "Sam Curran"]
list[1:3] = ["Moen Ali", "Raina"] #Change a Range of Item Values
print(list)
-> ['Yuvraj', 'Moen Ali', 'Raina', 'David Bhai', 'Sam Curran']

list = ["Yuvraj", "Dhoni", "Kane Mawa", "David Bhai", "Sam Curran"]
list.insert(2, "Virat") #insert() method inserts an item at the specified index
print(list)
->['Yuvraj', 'Dhoni', 'Virat', 'Kane Mawa', 'David Bhai', 'Sam Curran']

list = ["Yuvraj", "Dhoni", "Jadeja"]
list.append("Sam")  #To add an item to the end of the list, use the append() method
print(list)
-> ['Yuvraj', 'Dhoni', 'Jadeja', 'Sam']

list = ["Yuvraj", "Dhoni", "Jadeja"]
list1 = ["Maxwel", "Jhony", "Sam"]
list.extend(list1) #To append elements from another list to the current list, 
                    #use the extend() method.
print(list)
-> ['Yuvraj', 'Dhoni', 'Jadeja', 'Maxwel', 'Jhony', 'Sam']

list = ["Yuvraj", "Dhoni", "Jadeja"]
tuple = ("Maxwel", "Jhony", "Sam")
list.extend(tuple) #extend() method does not have to append lists, 
                   #you can add any iterable object (tuples, sets, dictionaries etc.).
print(list)
-> ['Yuvraj', 'Dhoni', 'Jadeja', 'Maxwel', 'Jhony', 'Sam']

---------------------------------------------------------------------------------------------------

## Remove List Items

list = ["Yuvraj", "Dhoni", "Jadeja"]
list.remove("Jadeja")  # remove() method removes the specified item.
print(list)
-> ['Yuvraj', 'Dhoni']

list = ["Yuvraj", "Dhoni", "Jadeja"]
list.pop(2)  # pop() method removes the specified index
print(list)
-> ['Yuvraj', 'Dhoni']

list = ["Yuvraj", "Dhoni", "Jadeja"]
del list[2]  # del keyword also removes the specified index:
print(list)
-> ['Yuvraj', 'Dhoni']

list = ["Yuvraj", "Dhoni", "Jadeja"]
list.clear()  # clear() method empties the list.
print(list)
-> []

---------------------------------------------------------------------------------------------------

## Sort List Alphanumerically
-> sort() method that will sort the list alphanumerically, ascending, by default.
list = ["Yuvraj", "Dhoni", "Jadeja"]
list.sort()  
print(list)
-> ['Dhoni', 'Jadeja', 'Yuvraj']

# Sort the list numerically:
list = [8,12,7]
list.sort()
print(list)
-> [7, 8, 12]

## Sort Descending
-> To sort descending, use the keyword argument reverse = True:

list = ["Yuvraj", "Dhoni", "Jadeja"]
list.sort(reverse = True)  
print(list)
-> ['Yuvraj', 'Jadeja', 'Dhoni']

list = [8,12,7]
list.sort(reverse = True)  
print(list)
-> [12, 8, 7]

---------------------------------------------------------------------------------------------------

##Case Insensitive Sort
-> sort() method is case sensitive,resulting in 
   all capital letters being sorted before lower case letters:

list = ["Yuvraj", "dhoni", "jadeja"]
list.sort()  
print(list)
-> ['Yuvraj', 'dhoni', 'jadeja']


-> if you want a case-insensitive sort function, 
    use str.lower as a key function:
list = ["Yuvraj", "dhoni", "jadeja"]
list.sort(key = str.lower)  
print(list)
-> ['dhoni', 'jadeja', 'Yuvraj']

---------------------------------------------------------------------------------------------------

## Reverse Order

-> reverse() method reverses the current sorting 
   order of the elements.

list = ["Yuvraj", "Dhoni", "Jadeja"]
list.reverse()  
print(list)
-> ['Jadeja', 'Dhoni', 'Yuvraj']

---------------------------------------------------------------------------------------------------

##Copy Lists

-> Make a copy of a list with the copy() method.

list = ["Yuvraj", "Dhoni", "Jadeja"]
list1 = list.copy()  
print(list1)
-> ['Yuvraj', 'Dhoni', 'Jadeja']

-> Make a copy of a list with the list() method.

list1 = ["Yuvraj", "Dhoni", "Jadeja"]
list2 = list(list1)  
print(list2)
-> ['Yuvraj', 'Dhoni', 'Jadeja']

---------------------------------------------------------------------------------------------------

##List Methods
-> Python has a set of built-in methods that you can use on lists.

#Method  	Description

append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), 
            to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list

---------------------------------------------------------------------------------------------------