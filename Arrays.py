# Arrays
-> An array is a special variable, which can hold more 
   than one value at a time.
-> Arrays are used to store multiple values in 
   one single variable.
-> An array can hold many values under a single name, and 
   you can access the values by referring to an index number.

cars = ["Ford", "Volvo", "BMW"]
print(cars)
-> ['Ford', 'Volvo', 'BMW']

------------------------------------------------------------------------------------------------------------------------------

# Access the Elements of an Array

cars = ["Ford", "Volvo", "BMW"]
# Get the value of the first array item
x = cars[0] 
print(x)
-> Ford

------------------------------------------------------

# Modify the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
-> ['Toyota', 'Volvo', 'BMW']

-------------------------------------------------------------------------------------------------------------------------------

#Length of an Array
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)
-> 3

-----------------------------------------------------

# Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)
->  Ford
    Volvo
    BMW

-------------------------------------------------------------------------------------------------------------------------------

# Adding Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
-> ['Ford', 'Volvo', 'BMW', 'Honda']

------------------------------------------------------

# Removing Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1) # cars.remove("Volvo")
print(cars)
-> ['Ford', 'BMW']

------------------------------------------------------------------------------------------------------------------------------

# Array Methods

#Method	        Description
append()	    Adds an element at the end of the list
clear()	        Removes all the elements from the list
copy()	        Returns a copy of the list
count()	        Returns the number of elements with the 
                specified value
extend()	    Add the elements of a list (or any iterable), 
                to the end of the current list
index()	        Returns the index of the first element with the 
                specified value
insert()	    Adds an element at the specified position
pop()	        Removes the element at the specified position
remove()	    Removes the first item with the specified value
reverse()	    Reverses the order of the list
sort()	        Sorts the list

------------------------------------------------------------------------------------------------------------------------------
