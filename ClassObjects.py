

# Create a class
class MyClass:
  x = 5
# Create Object
p1 = MyClass()
print(p1.x)

-> 5

---------------------------------------------------------------------------------------------------------------------

# self Parameter
-> self parameter is a reference to the current instance of the class, 
    and is used to access variables that belongs to the class.

#main class
class Car():

#init method to define object properties
    def __init__(self, color, types):
        self.color = color
        self.types = types

#methods to add functionality
    def brakes(self):
        print("Both of them have tow brakes")

#creating a object
car_1 = Car('Black', 'SUV')

#accessing it's properties
print(f"color of car_1: {car_1.color} and it's: {car_1.types}")

#accessing it's methods
car_1.brakes ()

->  color of car_1: Black and it's: SUV
    Both of them have tow brakes
   
---------------------------------------------------------------------------------------------------------------------

## The __init__() Function
-> All classes have a function called __init__(), 
   which is always executed when the class is being initiated.
-> Use the __init__() function to assign values to object properties, 
    or other operations that are necessary to do when the object is being created.

#main class
class Car():

#init method to define object properties
    def __init__(self, color, type):
        self.color = color
        self.type = type

#creating a object
car_1 = Car('Black', 'SUV')

print(car_1.color)
print(car_1.type)

->  Black
    SUV


