
# Inheritance

-> A class that inherits all the methods and properties from another class.
-> Parent class is the class being inherited from, 
    also called base class or super class.
-> Child class is the class that inherits from Parent class, 
   also called derived class or sub class.

# Super Class / Parent Class / Base Class
class Animal:
  def __init__(self, name, type):
    self.name = name
    self.type = type

# Sub Class / Child Class / Derived Class 
class Fish(Animal):
    def swim(self):
        print(self.name, self.type)

# Inheritance
V = Fish("Nemo", "Aquatic")

V.swim()
-> Nemo Aquatic

---------------------------------------------------------------------------------------------------------------------------------------------------------

# super() Function
-> super() function that will make the child class 
   inherit all the methods and properties from its parent.


# Super Class / Parent Class / Base Class
class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    # method
    def kingdom(self):
        print(self.name, self.type)

# Sub Class / Child Class / Derived Class 
class Fish(Animal):
    def swim(self):
        print(self.name, self.type)
        # super method
        super().kingdom()

# Inheritance
V = Fish("Nemo", "Aquatic")

V.kingdom()
-> Nemo Aquatic

