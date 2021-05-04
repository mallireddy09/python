# Scope
-> A variable is only available from inside the region it is created.

# Local Scope
-> A variable created inside a function belongs to the local scope 
   of that function, and can only be used inside that function.

def myfunc():
    x = 300
    print(x)
myfunc()

-> 300

------------------------------------------------------------------------------------------------------------------------------

# Function Inside Function
-> The local variable can be accessed from a function within the function:

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

-> 300

---------------------------------------------------------------------------------

# Global Scope
-> A variable created outside of a function is global and can be used by anyone.
-> Global variables are available from within any scope, global and local.

x = 300
def myfunc():
    print(x)
myfunc()
print(x)
-> 300
   300

------------------------------------------------------------------------------------------------------------------------------

# Global Keyword
-> The global keyword makes the variable global.
-> If you use the global keyword, the variable belongs to the global scope.

def myfunc():
    global x
    x = 300
myfunc()
print(x)
-> 300

-----------------------------------------------------------------------

-> To change the value of a global variable inside a function, 
   refer to the variable by using the global keyword.

x = 300
def myfunc():
    global x
    x = 200
myfunc()
print(x)
-> 200

------------------------------------------------------------------------------------------------------------------------------
