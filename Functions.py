
# Functions
-> A function is a block of code which only runs when it is called.
-> You can pass data, known as parameters, into a function.
-> A function can return data as a result.

# Creating a Function
-> function is defined using the def keyword.

def my_function():
    print("Hello")

# Calling a Function
-> To call a function, use the function name followed by parenthesis.

def my_function():
  print("Hello")
my_function()
-> Hello

--------------------------------------------------------------------------------------------------------------------------------------------------

# Parameters or Arguments
-> parameter and argument can be used for the same thing: 
   information that are passed into a function.
-> From a function's perspective:
1. A parameter is the variable listed inside the parentheses in the function definition.
2. An argument is the value that is sent to the function when it is called.

# Arguments
-> Arguments are specified after the function name, inside the parentheses. 
-> You can add as many arguments as you want, just separate them with a comma.
-> Arguments are often shortened to args in Python documentations.

def my_function(fname):
    print(fname + " suv")
my_function("Safari")
my_function("Tesla")
my_function("Suzuki")

->  Safari suv
    Tesla suv
    Suzuki suv

--------------------------------------------------------------------------------------------------------------------------------------------------

# Number of Arguments
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Safari", "suv")

-> Safari suv

# Arbitrary Arguments, *args
-> If the number of arguments is unknown, add a * before the parameter name.
-> This way the function will receive a tuple of arguments, 
   and can access the items accordingly.
  
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Ram", "Ravi", "Raj")

-> The youngest child is Raj

--------------------------------------------------------------------------------------------------------------------------------------------------

# Keyword Arguments
-> You can also send arguments with the key = value syntax.
-> This way the order of the arguments does not matter.

def my_function(child2, child1):
    print("The youngest child is " + child2)
my_function(child1 = "Linux", child2 = "Windows")

-> The youngest child is Windows

--------------------------------------------------------------------------------------------------------------------------------------------------

# Arbitrary Keyword Arguments, **kwargs
-> If the number of keyword arguments is unknown, 
   add a double ** before the parameter name.
-> This way the function will receive a dictionary of arguments, 
   and can access the items accordingly.

def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Robert", lname = "Junior")

-> His last name is Junior

--------------------------------------------------------------------------------------------------------------------------------------------------

# Default Parameter Value
-> If we call the function without argument, 
   it uses the default value.

def my_function(country = "India"):
    print("I am from " + country)
my_function("Austrila")
my_function("South Africa")
my_function()
my_function("England")

->  I am from Austrila
    I am from South Africa
    I am from India
    I am from England

--------------------------------------------------------------------------------------------------------------------------------------------------

# Passing a List as an Argument
->  You can send any data types of argument to a function 
    (string, number, list, dictionary etc.), and it will 
    be treated as the same data type inside the function.

def my_function(food):
    for x in food:
        print(x)
fruits = ["Apple", "Mango"]
my_function(fruits)

->  Apple
    Mango
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Return Values
-> To let a function return a value, use the return statement:

def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))

->  15
    25

# pass Statement
def myfunction():
    pass

--------------------------------------------------------------------------------------------------------------------------------------------------

# Recursion
-> Recursion is the process of defining something in terms of itself.
-> Python also accepts function recursion, which means
   a defined function can call itself.

#  recursive function
   to find the factorial of an integer.

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 3
print("The factorial of", num, "is", factorial(num))

-> The factorial of 3 is 6

--------------------------------------------------------------------------------------------------------------------------------------------------