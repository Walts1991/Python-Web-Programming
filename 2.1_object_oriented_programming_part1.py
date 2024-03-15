#OOP is a programming paradigm/structure
#Helps make code more dynamic
#Python is interpreted line by line 
#Modules use OOP
#Develop creates classes which looks like functions but called methods
#Classes also referred to as an instance
#Classes can be modified / inherited from another class.
#First you have to define a class

class Program():   #This defines the class, not the function
    def __init__(self, *args, **kwargs):     #The init method is special and gets called when we create a new object of this class
        self.lang = input("What language?: ")
        self.version = float(input("What version?: "))
        self.skill = input("What skill level?: ")
        
p1 = Program()

print(p1)
print(p1.lang)
print(p1.version)
 
#
"""
    def __init__(self, *args, **kwargs):     #The init method is always first in any class definition and it's used for initializing
        pass
    def __sub__():     #Defines what happens when subtraction occurs with this class
"""