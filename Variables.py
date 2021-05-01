## Initialization and printing values of variable

#creating variables

name = "PowerStar"
rollno = "966"
marks = "94.9"
#printing value of variables
print("Name:", name)
print("Roll:", rollno)
print("Marks:", marks)

**output**

Name: PowerStar
Roll: 966
Marks: 94.9

------------------------------------------------------------------------------------------------------------

## Assigning single value to multiple variable

#creating variables

x = y = z = "Orange"
#printing value of variables
print("x:",x)
print("y:",y)
print("z:",z)

**output**

x: Orange
y: Orange
z: Orange

---------------------------------------------------------------------------------------------------------------

## Assigning multiple values to multiple variables

#creating variables

x, y, z = "Orange", "Banana", "Cherry"
#printing value of variables
print("x:",x)
print("y:",y)
print("z:",z)

**output**

x: Orange
y: Banana
z: Cherry

------------------------------------------------------------------------------------------------------------------

## Local Variables

#function definition

def add():
#creating variable
x = 50
y = 30
Z = x + y
print("sum=",Z) 
#calling function
add ()
#This line will raise an error
#Because x is local variable
#and it can't be accessed
#outside function
print(x)

**output**

sum= 80
NameError: name 'x' is not defined

----------------------------------------------------------------------------------------------------------------

## Global Variables

#creating global variable

X=50
y=16
def add():
#accessing global variable #inside a function
print("Inside function Sum=",x+y)
#calling function
#outside a function
add()
print("Outside function Sum=",x+y)

**output**

Inside function Sum= 66
Outside function Sum= 66

--------------------------------------------------------------------------------------------------------------

## Using Global Keyword

def myfunc():
#To create a global variable inside a function, you can use the global keyword.
global x
X = "cool"
#calling function
#outside a function
my func()
print("Python is + x)

**output**

Python is cool

----------------------------------------------------------------------------------------------------------------